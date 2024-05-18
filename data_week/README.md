# Data Week (May 10th - 16th 2024)

This directory contains the data and Python scripts used for visualizing various datasets using Streamlit and Folium.

## Files

- [`aa_flight_paths.py`](./aa_flight_paths.py): Contains functions to visualize American Airlines flight paths on a map. Uses data from [`aa_flight_paths_data.csv`](./aa_flight_paths_data.csv).
- [`global_companies_map.py`](./global_companies_map.py): Contains a function to visualize the global distribution of top companies on a map. Uses data from [`companies_data.csv`](./companies_data.csv).
- [`state_city_map.py`](./state_city_map.py): Contains functions to visualize the state and capital cities of India. Uses data from [`state_city_data.json`](./state_city_data.json) and [`indian_map_coordinates.geojson`](./indian_map_coordinates.geojson).
- [`main.py`](./main.py): The main file to run the Streamlit app. It uses the functions defined in the other Python scripts in this directory.

## Data

- [`aa_flight_paths_data.csv`](./aa_flight_paths_data.csv): Contains data about American Airlines flight paths.
- [`companies_data.csv`](./companies_data.csv): Contains data about the global distribution of top companies.
- [`state_city_data.json`](./state_city_data.json): Contains data about the state and capital cities of India.
- [`indian_map_coordinates.geojson`](./indian_map_coordinates.geojson): Contains geographical coordinates for the map of India.

## Usage

To run the Streamlit app, navigate to this directory in your terminal and run the following command:

```sh
streamlit run main.py
```

This will start the Streamlit server and open the app in your default web browser.

## Dependencies

This project uses the following Python libraries:

- Streamlit
- Folium
- pandas
- plotly
- geopy
- streamlit_folium

Make sure to install these libraries using pip:

```sh
pip install streamlit folium pandas plotly geopy streamlit_folium
```

### Link to videos

1. [GHW Data Week] Interactive Maps Visualisation Part 1 - [https://youtu.be/s6WuhLG2gA8](https://youtu.be/s6WuhLG2gA8)

2. [GHW Data Week] Interactive Maps Visualisation Part 2 - [https://youtu.be/fDKkmuZfxZc](https://youtu.be/fDKkmuZfxZc)

3. [GHW Data Week] Interactive Maps Visualisation Part 3 - [https://youtu.be/63iik32X7fk](https://youtu.be/63iik32X7fk)
