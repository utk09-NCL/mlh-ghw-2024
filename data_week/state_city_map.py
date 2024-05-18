# state_city_map.py is a separate file that contains the functions to visualize the state and capital cities of India.

import json
import streamlit as st
import pandas as pd
import plotly.express as px

# Paths to data sources
PATH_TO_DATA = "data_week/state_city_data.json"
PATH_TO_GEOJSON = "data_week/indian_map_coordinates.geojson"


def load_json_data(path):
    """
    Load data from a JSON file.
    """
    try:
        return pd.read_json(path)
    except Exception as e:
        st.error(f"Error loading JSON data: {e}")
        return pd.DataFrame()


def state_city_scatter_mapbox():
    """
    Visualizes State and Capital Cities of India using a Scatter Map.
    """
    st.subheader("Visualizing State and Capital Cities of India")
    state_city_data = load_json_data(PATH_TO_DATA)

    if state_city_data.empty:
        return

    fig = px.scatter_mapbox(
        state_city_data,
        lat="lat",
        lon="long",
        hover_name="state",
        hover_data=["capital"],
        color="capital",
        color_discrete_sequence=px.colors.qualitative.Plotly,
        zoom=3,
        height=600,
        center={"lat": 20.5937, "lon": 78.9629}
    )
    # other mapbox styles: "carto-positron", "carto-darkmatter", "open-street-map", "stamen-terrain", "stamen-toner"
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)


def state_city_choropleth_mapbox():
    """
    Visualizes some data metric across Indian states using a Choropleth Map.
    """
    st.subheader("Choropleth Map of Indian States")
    state_city_data = load_json_data(PATH_TO_DATA)

    if state_city_data.empty:
        return

    try:
        with open(PATH_TO_GEOJSON) as f:
            geojson = json.load(f)
    except Exception as e:
        st.error(f"Error loading GeoJSON data: {e}")
        return

    fig = px.choropleth_mapbox(
        state_city_data,
        geojson=geojson,
        locations="state",
        featureidkey="properties.ST_NM",
        color="capital",
        hover_name="state",
        hover_data=["capital"],
        color_continuous_scale="Viridis",
        zoom=3,
        height=600,
        center={"lat": 20.5937, "lon": 78.9629}
    )
    # other mapbox styles: "carto-positron", "carto-darkmatter", "open-street-map", "stamen-terrain", "stamen-toner"
    fig.update_layout(mapbox_style="carto-positron")
    st.plotly_chart(fig, use_container_width=True)
