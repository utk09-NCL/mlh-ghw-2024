# main.py is the main file to run the Streamlit app.

import streamlit as st
from state_city_map import state_city_scatter_mapbox, state_city_choropleth_mapbox
from global_companies_map import global_companies_map
from aa_flight_paths import aa_flight_paths, aa_flight_paths_with_icon

# Set the page layout to wide
st.set_page_config(layout="wide")

# Set the title of the Streamlit app
st.title("GHW Data Week")

# Dictionary to map sidebar options to functions
SIDEBAR_OPTIONS = {
    "STATE-CITY SCATTER MAP": state_city_scatter_mapbox,
    "STATE-CITY CHOROPLETH MAP": state_city_choropleth_mapbox,
    "GLOBAL COMPANIES MAP": global_companies_map,
    "AA FLIGHT PATHS": aa_flight_paths,
    "AA FLIGHT PATHS WITH ICON": aa_flight_paths_with_icon,
}


def main():
    """
    Main function to run the Streamlit app.
    """
    try:
        # Display a radio button in the sidebar for chart type selection
        chart_type = st.sidebar.radio(
            "Select chart type:", list(SIDEBAR_OPTIONS.keys()))
        # Call the selected function
        SIDEBAR_OPTIONS[chart_type]()
    except Exception as e:
        st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
