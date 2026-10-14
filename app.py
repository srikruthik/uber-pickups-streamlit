import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Uber Pickups in NYC",
    page_icon="🚕",
    layout="wide",
)

st.title("Uber pickups in NYC")
st.write(
    "Explore New York City Uber pickups from September 2014. "
    "Use the hour slider to filter the map, and the checkbox to inspect the raw data."
)

DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)


@st.cache_data
def load_data(nrows=10000):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(columns=lambda column: str(column).lower(), inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


with st.spinner("Loading Uber pickup data..."):
    data = load_data(10000)

st.success(f"Loaded {len(data):,} pickup records.")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.dataframe(data, use_container_width=True)

st.subheader("Number of pickups by hour")
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour,
    bins=24,
    range=(0, 24),
)[0]
hourly = pd.DataFrame({
    "Hour": [f"{hour:02d}:00" for hour in range(24)],
    "Pickups": hist_values,
}).set_index("Hour")
st.bar_chart(hourly)

st.subheader("Map of pickups")
hour_to_filter = st.slider(
    "Choose an hour",
    min_value=0,
    max_value=23,
    value=17,
    format="%d:00",
)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.caption(f"Showing {len(filtered_data):,} pickups at {hour_to_filter:02d}:00.")
st.map(filtered_data)

st.caption("Data source: Streamlit's public Uber NYC pickups tutorial dataset.")
