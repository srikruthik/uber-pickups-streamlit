# Uber Pickups in NYC

A Streamlit app based on the official Streamlit "Create an app" tutorial.

## Features
- Loads the public Uber NYC September 2014 pickup dataset.
- Caches data loading with `st.cache_data`.
- Displays raw data behind a checkbox.
- Shows a histogram of pickups by hour.
- Displays pickup locations on a map.
- Filters the map using an hour slider.

## Run locally
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Deploy
Push these files to a public GitHub repository, then deploy `app.py` using Streamlit Community Cloud.
