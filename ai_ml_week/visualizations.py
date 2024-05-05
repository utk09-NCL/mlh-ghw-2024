import matplotlib.pyplot as plt
import textwrap
import plotly.express as px
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def plot_market_cap_distribution(df, top_n=20):
    # Function definition: Plots a horizontal bar chart showing top companies by market cap.
    # df: DataFrame containing company data, top_n: number of top companies to display.

    # Sort the DataFrame by 'Market Cap (USD) Numerical' column in descending order.
    df_sorted = df.sort_values(
        by='Market Cap (USD) Numerical', ascending=False)

    # Select the top 'n' companies based on market cap after sorting.
    top_companies = df_sorted.head(top_n)

    # Create a Matplotlib figure and axes object with a specified size.
    fig, ax = plt.subplots(figsize=(20, 30))

    # Plot a horizontal bar chart using the top companies' names and their market cap.
    ax.barh(top_companies['Company'],
            top_companies['Market Cap (USD) Numerical'])

    # Set the label for the x-axis.
    ax.set_xlabel('Market Cap (USD)')

    # Set the label for the y-axis.
    ax.set_ylabel('Company')

    # Set the title of the bar chart.
    ax.set_title(f'Top {top_n} Companies by Market Cap')

    # Invert the y-axis to have the company with the highest market cap on top.
    ax.invert_yaxis()

    # Format the tick labels on the x-axis to display them in a plain style without scientific notation.
    # ax.ticklabel_format(style='plain', axis='x')

    plt.tight_layout()  # Adjust layout to make room for the longer company names

    # Return the figure object for further manipulation or to display.
    return fig


def plot_market_cap_distribution_wrapped(df, top_n=20):
    """Plot a horizontal bar chart of the top companies by market cap with dynamic height adjustment."""
    df_sorted = df.sort_values(
        by='Market Cap (USD) Numerical', ascending=False)
    top_companies = df_sorted.head(top_n)

    # Wrap company names if they are too long (optional)
    top_companies['Company'] = top_companies['Company'].apply(
        lambda x: '\n'.join(textwrap.wrap(x, 20)))

    # Dynamically adjust figure height to improve label readability
    figure_height = max(6, top_n * 0.3)  # Adjust 0.3 based on your needs

    fig, ax = plt.subplots(figsize=(10, figure_height))
    ax.barh(top_companies['Company'],
            top_companies['Market Cap (USD) Numerical'])
    ax.set_xlabel('Market Cap (USD)')
    ax.set_ylabel('Company')
    ax.set_title(f'Top {top_n} Companies by Market Cap')
    ax.invert_yaxis()
    ax.ticklabel_format(style='plain', axis='x')

    plt.tight_layout()  # Adjust layout to make room for the longer company names
    return fig


def sector_wise_donut_chart(df):
    # Defines a function to create a donut chart visualizing the distribution of companies by sector.
    """Create a donut chart for sector-wise distribution."""
    # The docstring provides a brief description of the function's purpose.

    # Counts the occurrences of each unique value in the 'Sector' column, resets the index to convert
    # the series to a DataFrame, which is required for Plotly Express functions.
    sector_counts = df['Sector'].value_counts().reset_index()

    # Renames the columns of the resulting DataFrame for clarity and to match the expected
    # input format for the plotting function. 'index' column becomes 'Sector' and
    # the counts column becomes 'NumberOfCompanies'.
    sector_counts.columns = ['Sector', 'NumberOfCompanies']

    # Uses Plotly Express to create a pie chart from the sector counts. The 'values' argument
    # specifies which column to use for the pie chart sectors' sizes, 'names' specifies the labels,
    # 'hole=0.3' creates the donut chart appearance by specifying the radius of the hole in the middle,
    # and 'title' sets the chart's title.
    fig = px.pie(sector_counts,
                 values='NumberOfCompanies',
                 names='Sector',
                 hole=0.3,
                 title='Sector-wise Distribution of Companies')

    # Returns the figure object created by Plotly Express. This object can be displayed in a Jupyter
    # Notebook or within a web application using Plotly's display functions.
    return fig


def industry_wise_donut_chart(df):
    """
    Create a donut chart for industry-wise distribution.

    Parameters:
    - df: DataFrame with a column 'Industry' indicating the industry of each company.

    Returns:
    - fig: The Plotly figure object for the donut chart.
    """
    # Calculate the number of companies in each industry
    industry_counts = df['Industry'].value_counts().reset_index()
    industry_counts.columns = ['Industry', 'NumberOfCompanies']

    # Create the donut chart
    fig = px.pie(industry_counts,
                 values='NumberOfCompanies',
                 names='Industry',
                 hole=0.3,  # This creates the donut chart appearance
                 title='Industry-wise Distribution of Companies')

    # Return the Plotly figure object
    return fig


def country_wise_donut_chart(df):
    """
    Create a donut chart for country-wise distribution of companies.

    Parameters:
    - df: DataFrame with a column 'Country' indicating the country of each company.

    Returns:
    - fig: The Plotly figure object for the donut chart.
    """

    # Calculate the number of companies in each country
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'NumberOfCompanies']

    # Create the donut chart
    fig = px.pie(country_counts,
                 values='NumberOfCompanies',
                 names='Country',
                 hole=0.3,  # This creates the donut chart appearance
                 title='Country-wise Distribution of Companies')

    # Return the Plotly figure object
    return fig


def sector_wise_treemap(df):
    """Create a treemap for market cap distribution by sector."""
    sector_market_cap = df.groupby(
        'Sector')['Market Cap (USD) Numerical'].sum().reset_index()
    fig = px.treemap(sector_market_cap,
                     path=['Sector'],
                     values='Market Cap (USD) Numerical',
                     title='Market Cap Distribution by Sector')
    return fig


def plot_sector_market_cap_boxplot(df):
    """
    Plot a box plot of market cap distribution by sector using matplotlib and seaborn.

    This function visualizes the distribution, spread, and outliers of market cap values within each sector,
    providing insights into the financial size and variance of companies across different sectors.

    Parameters:
    - df: DataFrame containing the sectors and their corresponding market cap values.
    """

    # Set the size of the figure to ensure the plot is large enough to be easily readable.
    # This makes the plot wider and taller than the default size.
    plt.figure(figsize=(12, 8))

    # Create a box plot with seaborn. The 'x' parameter specifies the categorical variable (sector),
    # and the 'y' parameter specifies the numerical variable (market cap) to analyze.
    # 'data=df' tells seaborn which DataFrame to use for plotting.
    sns.boxplot(x='Sector', y='Market Cap (USD) Numerical', data=df)

    # Rotate the x-axis labels (sector names) to 45 degrees to prevent overlap and improve readability.
    # 'ha' (horizontal alignment) set to 'right' aligns the end of the label with the tick mark.
    plt.xticks(rotation=45, ha='right')

    # Set the title of the box plot to describe what the plot shows.
    plt.title('Market Cap Distribution by Sector')

    # Label the x-axis as 'Sector' to indicate that each box corresponds to a different sector.
    plt.xlabel('Sector')

    # Label the y-axis as 'Market Cap (USD)' to indicate the variable being analyzed in each box plot.
    plt.ylabel('Market Cap (USD)')

    # Adjust the layout to make sure the plot, labels, and title are not cut off when displayed.
    plt.tight_layout()

    # Return the matplotlib figure object that contains the box plot. This allows for further customization
    # or display outside of this function, if needed.
    return plt.gcf()


def plot_sector_market_cap_boxplot_2(df):
    """
    Enhanced box plot of market cap distribution by sector with statistical values displayed outside the plot.
    """
    plt.figure(figsize=(14, 10))
    ax = sns.boxplot(x='Sector', y='Market Cap (USD) Numerical', data=df)

    plt.xticks(rotation=45, ha='right')
    plt.title('Market Cap Distribution by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Market Cap (USD)')

    # Initialize a list to collect data for each sector
    stats_data = []

    for sector in df['Sector'].unique():
        sector_data = df[df['Sector'] ==
                         sector]['Market Cap (USD) Numerical'].dropna()

        quartiles = np.percentile(sector_data, [25, 50, 75])
        whisker_low = sector_data.min()
        whisker_high = sector_data.max()

        # Collect data for the current sector
        stats_data.append({
            'Sector': sector,
            '25%': f"{quartiles[0]:.2f} B",
            'Median': f"{quartiles[1]:.2f} B",
            '75%': f"{quartiles[2]:.2f} B",
            'Low': f"{whisker_low:.2f} B",
            'High': f"{whisker_high:.2f} B"
        })

    # Convert the list of dictionaries to a DataFrame after collecting all data
    stats_summary = pd.DataFrame(stats_data)

    plt.tight_layout()

    st.write("Market Cap Distribution by Sector (Statistical Summary):")
    st.write(stats_summary)

    return plt.gcf()


def plot_sector_market_cap_boxplot_log_transformed(df):
    """Plot a box plot of market cap distribution by sector with log transformation and improved tick labels."""
    # Ensure market cap is numeric and replace 0s with a small value (to avoid -inf after log transformation)
    df['Market Cap (USD) Numerical'] = pd.to_numeric(
        df['Market Cap (USD) Numerical'], errors='coerce').replace(0, 1)
    df['Log Market Cap (USD) Numerical'] = np.log10(
        df['Market Cap (USD) Numerical'])

    plt.figure(figsize=(14, 10))
    sns.boxplot(x='Sector',
                y='Log Market Cap (USD) Numerical',
                data=df,
                palette='Spectral')
    plt.xticks(rotation=45, ha='right')
    plt.title('Market Cap Distribution by Sector (Log Scale)')
    plt.xlabel('Sector')
    plt.ylabel('Log Market Cap (USD)')

    # Set custom ticks to represent a meaningful range of market caps
    max_log = df['Log Market Cap (USD) Numerical'].max()
    tick_vals = np.arange(0, max_log + 1,
                          1)  # Generate ticks from 0 to max_log with a step of 1
    tick_labels = [
        '${:.0f}B'.format(10**tick_val / 1e9) for tick_val in tick_vals
    ]  # Convert log ticks back to linear scale (in billions)

    plt.yticks(tick_vals, tick_labels)

    plt.tight_layout()
    return plt.gcf()


def plot_sector_market_cap_violin(df):
    """Plot a violin plot of market cap distribution by sector."""
    plt.figure(figsize=(12, 8))
    sns.violinplot(x='Sector', y='Market Cap (USD) Numerical', data=df)
    plt.xticks(rotation=45, ha='right')
    plt.title('Market Cap Distribution by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Market Cap (USD)')
    plt.tight_layout()
    return plt.gcf()


def plot_companies_count_by_sector(df):
    """Plot a count plot of companies by sector."""
    plt.figure(figsize=(12, 8))
    sns.countplot(y='Sector', data=df, order=df['Sector'].value_counts().index)
    plt.title('Number of Companies by Sector')
    plt.xlabel('Count')
    plt.ylabel('Sector')
    plt.tight_layout()
    return plt.gcf()


def plot_companies_count_by_industry(df):
    """
    Plot a count plot of companies by industry using Plotly, with different colors for each industry and a legend.

    Parameters:
    - df: DataFrame with a column 'Industry' indicating the industry of each company.

    Returns:
    - fig: The Plotly Express figure object for the count plot.
    """

    # Ensure the DataFrame is sorted by the 'Industry' counts
    industry_counts = df['Industry'].value_counts().reset_index()
    industry_counts.columns = ['Industry', 'NumberOfCompanies']
    industry_counts = industry_counts.sort_values(
        by='NumberOfCompanies', ascending=True)

    # Create the count plot using Plotly Express, with different colors for each industry
    fig = px.bar(industry_counts, y='Industry', x='NumberOfCompanies', orientation='h',
                 color='Industry',  # Assigns different colors based on 'Industry'
                 title='Number of Companies by Industry')
    # Update layout to include a legend and improve axis titles
    # Sort legend alphabetically
    fig.update_layout(xaxis_title="Count",
                      yaxis_title="Industry",
                      legend_title="Industry",
                      legend=dict(orientation="h",
                                   yanchor="bottom", y=1.02, xanchor="right", x=1))

    # Adjust marker line for clarity
    fig.update_traces(marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)

    return fig


def plot_market_cap_sector_scatter(df):
    """Plot a scatter plot of market cap vs. sectors using the processed market cap values."""
    # Log transform the market cap for better visualization
    df['Log Market Cap (USD) Numerical'] = np.log10(
        df['Market Cap (USD) Numerical'] + 1)  # +1 to avoid log(0)

    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df,
                    x='Sector',
                    y='Log Market Cap (USD) Numerical',
                    palette='tab10',
                    hue='Sector',
                    legend='full')
    plt.xticks(rotation=45, ha='right')
    plt.title('Market Cap (USD) Distribution by Sector (in Billions)')
    plt.xlabel('Sector')
    plt.ylabel('Log Market Cap (USD, in Billions)')
    plt.tight_layout()
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    return plt.gcf()


def plot_market_cap_vs_count_by_sector(df):
    """
    Create a scatter plot using Plotly to show the sum of market cap vs. the count of companies for each sector.

    Parameters:
    - df: DataFrame with columns 'Sector' and 'Market Cap (USD) Numerical'.

    Returns:
    - fig: The Plotly Express figure object for the scatter plot.
    """
    # Aggregate data to get the sum of market cap and count of companies for each sector
    sector_aggregates = df.groupby('Sector').agg(
        SumMarketCap=('Market Cap (USD) Numerical', 'sum'),
        CompanyCount=('Sector', 'count')
    ).reset_index()

    # Create the scatter plot
    fig = px.scatter(sector_aggregates,
                     x='CompanyCount',
                     y='SumMarketCap',
                     size='SumMarketCap',  # Optional: Use market cap as size of the bubble
                     color='Sector',  # Different color for each sector
                     hover_name='Sector',  # Show sector name on hover
                     title='Sum of Market Cap vs. Count of Companies by Sector')

    # Update axes titles
    fig.update_xaxes(title_text='Count of Companies')
    fig.update_yaxes(title_text='Sum of Market Cap (USD)')

    return fig


def create_global_distribution_map(df):
    """
    Create a Choropleth map to show the global distribution of companies.

    Parameters:
    - df: DataFrame containing the company data, including a 'Country' column.

    Returns:
    - Plotly Figure object that can be displayed with .show() method.
    """
    # Aggregate the number of companies per country
    country_counts = df['Country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'NumberOfCompanies']

    # Create the Choropleth map
    fig = px.choropleth(
        country_counts,
        locations="Country",
        locationmode='country names',  # Match countries by their names
        color="NumberOfCompanies",  # Column denoting the number of companies
        hover_name="Country",  # Column to display on hover
        color_continuous_scale=px.colors.sequential.Plasma,  # Color scale
        title="Global Distribution of Top Companies")

    return fig


def plot_stacked_bar_chart_by_country_and_sector(df):
    """
    Plot a stacked bar chart with country names on the x-axis and the number of companies in each sector stacked.

    Parameters:
    - df: DataFrame with columns 'Country', 'Sector'.

    Returns:
    - fig: The Matplotlib figure object.
    """

    # Optionally exclude "United States" from the DataFrame
    # Uncomment the next line to exclude "United States"
    df = df[df['Country'] != 'United States']

    # Aggregate the data: Count of companies by Country and Sector
    sector_counts = df.groupby(['Country',
                                'Sector']).size().unstack(fill_value=0)

    # Create figure and axes for the plot
    fig, ax = plt.subplots(figsize=(20, 12))

    # Plotting the stacked bar chart on the created axes
    sector_counts.plot(kind='bar', stacked=True, ax=ax)

    ax.set_title('Number of Companies by Sector in Each Country')
    ax.set_xlabel('Country')
    ax.set_ylabel('Number of Companies')
    ax.tick_params(axis='x',
                   rotation=90)  # Rotate country names for better readability
    ax.legend(title='Sector', bbox_to_anchor=(1.05, 1),
              loc='upper left')  # Move the legend outside of the plot

    # Return the figure object instead of showing it
    return fig


def plot_stacked_bar_chart_by_country_and_industry(df):
    """
    Plot an interactive stacked bar chart showing the distribution of industries within each country.
    Optionally excludes "United States" from the DataFrame.
    """
    # Optionally exclude "United States" from the analysis. This line can be commented or uncommented
    # to include or exclude the United States in the dataset for the visualization.
    df = df[df['Country'] != 'United States']

    # Group the data by 'Country' and 'Industry', then count the number of occurrences of each combination.
    # 'reset_index' is used to convert the resulting Series to a DataFrame, making it suitable for further processing.
    # The 'name' parameter in 'reset_index' names the column containing the count of companies 'Counts'.
    industry_counts = df.groupby(
        ['Country', 'Industry']).size().reset_index(name='Counts')

    # Pivot the DataFrame to create a wide-format DataFrame where each row represents a country,
    # each column represents an industry, and cell values represent the count of companies in that country-industry combination.
    # 'fillna(0)' replaces NaN values with 0, ensuring that all cells have a numeric value.
    wide_df = industry_counts.pivot(
        index='Country', columns='Industry', values='Counts').fillna(0)

    # Use Plotly Express to create a stacked bar chart. 'wide_df.index' and 'wide_df.columns' specify the x and y axes, respectively.
    # This format matches the wide-format DataFrame created by the pivot operation.
    # The 'barmode'='stack' argument in 'update_layout' ensures that bars are stacked, representing the count of companies in each industry for a country.
    fig = px.bar(wide_df, x=wide_df.index, y=wide_df.columns,
                 title="Number of Companies by Industry in Each Country")

    # Update the layout of the figure to set titles for the x and y axes and to ensure the bar mode is set to 'stack'.
    # This improves the readability and interpretability of the chart.
    fig.update_layout(xaxis_title="Country",
                      yaxis_title="Number of Companies", barmode='stack')

    # Customize the hover information to show the count of companies, the country, and the industry
    # when the user hovers over a part of the stacked bar. This provides additional context and detail.
    fig.update_traces(hovertemplate='%{y} Companies in %{x} - %{label}')

    # Return the figure object, which can be displayed in a Jupyter notebook, a Python script, or a web application.
    return fig


def create_industry_bubble_map(df):
    """
    Create a bubble map showing the distribution of companies by industry within countries, returning the figure object.

    Parameters:
    - df: DataFrame with columns 'Country', 'Industry', and counts of companies.

    Returns:
    - fig: Plotly Figure object.
    """
    # Example pseudo-coordinates mapping
    country_centers = {
        'United States': {
            'lat': 37.0902,
            'lon': -95.7129
        },
        'India': {
            'lat': 20.5937,
            'lon': 78.9629
        },
        # Add more countries here
    }

    # Industry color mapping
    industry_colors = {
        'Consumer Electronics': 'yellow',
        'Software—Infrastructure': 'blue',
        'Oil & Gas Integrated': 'green',
        # Add more industries here
    }

    # Aggregate data: Count companies per industry per country
    industry_counts = df.groupby(['Country',
                                  'Industry']).size().reset_index(name='Counts')

    fig = go.Figure()

    for country, group in industry_counts.groupby('Country'):
        # Skip countries without a predefined center
        if country not in country_centers:
            continue

        base_lat = country_centers[country]['lat']
        base_lon = country_centers[country]['lon']

        for i, (index, row) in enumerate(group.iterrows()):
            # Offset coordinates to avoid overlap
            lat = base_lat + (i * 0.5)  # Adjust the multiplier as needed
            lon = base_lon + (i * 0.5)  # Adjust the multiplier as needed

            industry = row['Industry']
            count = row['Counts']
            color = industry_colors.get(
                industry, 'gray')  # Default to gray if industry not in mapping

            fig.add_trace(
                go.Scattergeo(
                    lon=[lon],
                    lat=[lat],
                    text=f"{industry}: {count}",
                    marker=dict(
                        size=count * 10,  # Adjust size multiplier as needed
                        color=color,
                        line_color='rgb(40,40,40)',
                        line_width=0.5,
                        sizemode='area'),
                    name=f"{country} - {industry}"))

    fig.update_layout(title_text='Global Distribution of Companies by Industry',
                      showlegend=True,
                      geo=dict(
                          scope='world',
                          landcolor='rgb(217, 217, 217)',
                      ))

    # Return the figure object instead of showing it directly
    return fig


def create_sector_bubble_map(df):
    """
    Create a bubble map showing the distribution of companies by sector within countries, returning the figure object.

    Parameters:
    - df: DataFrame with columns 'Country', 'Sector', and counts of companies.

    Returns:
    - fig: Plotly Figure object.
    """
    # Example pseudo-coordinates mapping
    country_centers = {
        'United States': {
            'lat': 37.0902,
            'lon': -95.7129
        },
        'India': {
            'lat': 20.5937,
            'lon': 78.9629
        },
        # Add more countries here
    }

    # Sector color mapping
    sector_colors = {
        'Technology': 'cyan',
        'Energy': 'green',
        'Financials': 'blue',
        'Consumer Discretionary': 'orange',
        'Communication Services': 'red',
        # Add more sectors here
    }

    # Aggregate data: Count companies per sector per country
    sector_counts = df.groupby(['Country',
                                'Sector']).size().reset_index(name='Counts')

    fig = go.Figure()

    for country, group in sector_counts.groupby('Country'):
        # Skip countries without a predefined center
        if country not in country_centers:
            continue

        base_lat = country_centers[country]['lat']
        base_lon = country_centers[country]['lon']

        for i, (index, row) in enumerate(group.iterrows()):
            # Offset coordinates to avoid overlap
            lat = base_lat + (i * 0.2)  # Smaller adjustment for sectors
            lon = base_lon + (i * 0.2)

            sector = row['Sector']
            count = row['Counts']
            color = sector_colors.get(
                sector, 'gray')  # Default to gray if sector not in mapping

            fig.add_trace(
                go.Scattergeo(
                    lon=[lon],
                    lat=[lat],
                    text=f"{sector}: {count}",
                    marker=dict(
                        size=count * 10,  # Adjust size multiplier as needed
                        color=color,
                        line_color='rgb(40,40,40)',
                        line_width=0.5,
                        sizemode='area'),
                    name=f"{country} - {sector}"))

    fig.update_layout(title_text='Global Distribution of Companies by Sector',
                      showlegend=True,
                      geo=dict(
                          scope='world',
                          landcolor='rgb(217, 217, 217)',
                      ))

    return fig
