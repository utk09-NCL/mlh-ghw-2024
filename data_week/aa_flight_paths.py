# aa_flight_paths.py is a Python file that contains two functions to visualize American Airlines flight paths on a map. The first function, aa_flight_paths, creates a map with flight paths between airports. The second function, aa_flight_paths_with_icon, adds icons to the map to represent the midpoint of each flight path.

import streamlit as st
import pandas as pd
import folium
from folium import features
from streamlit_folium import st_folium

# Path to data source
PATH_TO_DATA = "data_week/aa_flight_paths_data.csv"


def load_csv_data(path):
    """
    Load data from a CSV file.
    """
    try:
        return pd.read_csv(path)
    except Exception as e:
        st.error(f"Error loading CSV data: {e}")
        return pd.DataFrame()


def aa_flight_paths():
    """
    Visualizes American Airlines flight paths.
    """
    st.subheader("American Airlines Flight Paths")
    flight_paths = load_csv_data(PATH_TO_DATA)

    st.dataframe(flight_paths)

    if flight_paths.empty:
        return

    map_ = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    for index, row in flight_paths.iterrows():
        folium.PolyLine(
            locations=[(row['start_lat'], row['start_lon']),
                       (row['end_lat'], row['end_lon'])],
            weight=2,
            color='blue',
            popup=f"{index}: {row['airport1']} to {row['airport2']}: {row['count']} flights"
        ).add_to(map_)

    st_folium(map_, width=900, height=750)


def random_color_generator():
    """
    Generate a random color for the flight path.
    """
    import random
    set_of_colours = set()
    for _ in range(160):
        # create a unique random color
        def r(): return random.randint(0, 255)
        set_of_colours.add('#%02X%02X%02X' % (r(), r(), r()))
    return list(set_of_colours)


colors = random_color_generator()  # Generate random colors for flight paths


def aa_flight_paths_with_icon():
    """
    Visualizes American Airlines flight paths with icons.
    """
    st.subheader("American Airlines Flight Paths with Icons")
    flight_paths = load_csv_data(PATH_TO_DATA)

    st.dataframe(flight_paths)

    if (flight_paths.empty):
        return

    # you can also set tiles='cartodb positron' or 'cartodb dark_matter'
    #  map_ = folium.Map(location=[37.0902, -95.7129], zoom_start = 4, tiles = 'cartodb dark_matter')
    map_ = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

    icon_url = "https://cdn.iconscout.com/icon/free/png-512/free-plane-3802463-3168528.png"

    for idx, row in flight_paths.iterrows():
        start_coords = (row['start_lat'], row['start_lon'])
        end_coords = (row['end_lat'], row['end_lon'])
        color = colors[idx % len(colors)]

        folium.PolyLine(
            locations=[start_coords, end_coords],
            weight=2,
            color=color,
            popup=f"{idx}:{row['airport1']} to {row['airport2']}: {row['count']} flights"
        ).add_to(map_)

        midpoint = [(start_coords[0] + end_coords[0]) / 2,
                    (start_coords[1] + end_coords[1]) / 2]

        folium.Marker(
            location=midpoint,
            icon=features.CustomIcon(icon_url, icon_size=(24, 24)),
            popup=f"{idx}:{row['airport1']} to {row['airport2']}: {row['count']} flights"
        ).add_to(map_)

    st_folium(map_, width=950, height=750)
