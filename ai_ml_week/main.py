import streamlit as st
from data_utils import load_and_process_csv
from visualizations import (
    plot_market_cap_distribution, plot_market_cap_distribution_wrapped,
    sector_wise_donut_chart, industry_wise_donut_chart, country_wise_donut_chart, sector_wise_treemap,
    plot_sector_market_cap_boxplot,
    plot_sector_market_cap_boxplot_2,
    plot_sector_market_cap_boxplot_log_transformed,
    plot_sector_market_cap_violin, plot_companies_count_by_sector, plot_companies_count_by_industry,
    plot_market_cap_sector_scatter, plot_market_cap_vs_count_by_sector, create_global_distribution_map,
    plot_stacked_bar_chart_by_country_and_sector,
    plot_stacked_bar_chart_by_country_and_industry)
import warnings

warnings.filterwarnings('ignore')
st.set_page_config(layout="wide")


def filter_dataframe(df, exclude_companies):
    """Filter the dataframe to exclude specified companies."""
    if exclude_companies:
        exclude_list = [name.strip() for name in exclude_companies.split(',')]
        return df[~df['Company'].isin(exclude_list)]
    return df


def main():
    st.title("Company Data Visualization")

    # Sidebar for chart type selection
    chart_type = st.sidebar.radio("Select chart type:", [
        "View Data Table",
        "Market Cap Distribution",
        "Sector-wise Distribution",
        "Industry-wise Distribution",
        "Country-wise Distribution",
        "Market Cap Distribution by Sector",
        "Market Cap Distribution by Sector (Boxplot)",
        "plot_sector_market_cap_boxplot_2",
        "Market Cap Distribution by Sector (Violin)",
        "Number of Companies by Sector",
        "Number of Companies by Industry",
        "Market Cap Distribution by Sector Scatter",
        "Market Cap vs Count by Sector Scatter",
        "Global Distribution of Top Companies",
        "Stacked Bar Chart By Country and Sector",
        "Stacked Bar Chart By Country and Industry",
    ])

    # Load and process the dataset
    df = load_and_process_csv('companies_data.csv')

    # Text input for excluding companies
    exclude_companies = st.text_input(
        "Enter company names to exclude (comma separated):")

    # Filter dataframe based on excluded companies
    df_filtered = filter_dataframe(df, exclude_companies)

    if chart_type == "Market Cap Distribution":
        top_n = st.slider("Select number of top companies:", 10, 100, 20, 10)
        fig = plot_market_cap_distribution(df_filtered, top_n)
        st.pyplot(fig)
    elif chart_type == "Market Cap Distribution (Wrapped)":
        top_n = st.slider("Select number of top companies:", 10, 100, 20, 10)
        fig = plot_market_cap_distribution_wrapped(df_filtered, top_n)
        st.pyplot(fig)
    elif chart_type == "Sector-wise Distribution":
        fig = sector_wise_donut_chart(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "Industry-wise Distribution":
        fig = industry_wise_donut_chart(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "Country-wise Distribution":
        fig = country_wise_donut_chart(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "Market Cap Distribution by Sector":
        fig = sector_wise_treemap(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "View Data Table":
        st.dataframe(df_filtered, height=700, width=1200)
    elif chart_type == "Market Cap Distribution by Sector (Boxplot)":
        fig = plot_sector_market_cap_boxplot(df_filtered)
        st.pyplot(fig)
    elif chart_type == "plot_sector_market_cap_boxplot_2":
        fig = plot_sector_market_cap_boxplot_2(df_filtered)
        st.pyplot(fig)
    elif chart_type == "Market Cap Distribution by Sector (Boxplot) Log Transformed":
        fig = plot_sector_market_cap_boxplot_log_transformed(df_filtered)
        st.pyplot(fig)
    elif chart_type == "Market Cap Distribution by Sector (Violin)":
        fig = plot_sector_market_cap_violin(df_filtered)
        st.pyplot(fig)
    elif chart_type == "Number of Companies by Sector":
        fig = plot_companies_count_by_sector(df_filtered)
        st.pyplot(fig)
    elif chart_type == "Number of Companies by Industry":
        fig = plot_companies_count_by_industry(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "Market Cap Distribution by Sector Scatter":
        fig = plot_market_cap_sector_scatter(df_filtered)
        st.pyplot(fig)
    elif chart_type == "Market Cap vs Count by Sector Scatter":
        fig = plot_market_cap_vs_count_by_sector(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "Global Distribution of Top Companies":
        fig = create_global_distribution_map(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == "Stacked Bar Chart By Country and Sector":
        fig = plot_stacked_bar_chart_by_country_and_sector(df_filtered)
        st.pyplot(fig)
    elif chart_type == "Stacked Bar Chart By Country and Industry":
        fig = plot_stacked_bar_chart_by_country_and_industry(df_filtered)
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
