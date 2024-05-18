# global_companies_map.py is a Python file that contains a function to visualize the global distribution of top companies on a map.

import streamlit as st
import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderQuotaExceeded
from folium.plugins import MarkerCluster
import time
import streamlit.components.v1 as components

# File path to the CSV data
PATH_TO_DATA = "data_week/companies_data.csv"


def normalize_text(text):
    """
    Normalize text to lowercase and strip leading/trailing whitespace.
    """
    return text.strip().lower()


def load_data(path):
    """
    Load company data from a CSV file.
    """
    try:
        return pd.read_csv(path, index_col="Ranking")
    except Exception as e:
        st.error(f"Error loading CSV data: {e}")
        return pd.DataFrame()


def geocode_country(geolocator, country):
    """
    Geocode a country name to its latitude and longitude.
    """
    try:
        location = geolocator.geocode(country, timeout=20, language='en')
        if location and normalize_text(country) in normalize_text(location.address):
            return location.latitude, location.longitude, location.address
    except (GeocoderTimedOut, GeocoderQuotaExceeded) as e:
        st.error(f"Geocoding error for {country}: {e}")
    except Exception as e:
        st.error(f"Unexpected error for {country}: {e}")
    return None, None, None


def create_map(companies_data):
    """
    Create a folium map with markers for each company's headquarters.
    """
    geolocator = Nominatim(user_agent="ghw_dataweek_ut", timeout=10)
    map_ = folium.Map(location=[20, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(map_)

    for index, row in companies_data.iterrows():
        country_query = row['Country']
        lat, lon, address = geocode_country(geolocator, country_query)
        if lat and lon:
            popup_message = f"{row['Company']} ({row['Country']})"
            folium.Marker(
                location=[lat, lon],
                popup=popup_message,
            ).add_to(marker_cluster)
            st.write(
                f"{index}: {row['Company']} - Geocoded and plotted at {address}")
        else:
            st.error(f"{index}: Geocoding failed for {country_query}")
        time.sleep(0.5)  # To respect the rate limits

    return map_


def global_companies_map():
    """
    Main function to generate and display the global companies map.
    """
    st.subheader("Global Distribution of Top Companies")
    companies_data = load_data(PATH_TO_DATA)

    if companies_data.empty:
        return

    # Display a subset of the data for inspection
    companies_subset = companies_data[450:488]
    st.write(companies_subset[["Company", "Country"]])

    # Create and display the map
    map_ = create_map(companies_subset)
    map_.save('companies_map.html')
    HtmlFile = open('companies_map.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height=650)
