# Let's run the code with the provided file to visualize the line plot, bar chart, and box plots.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean the data
df = pd.read_csv("C:/Users/edj36/OneDrive/Documents/time_series_visualizer.csv", index_col='date', parse_dates=True)
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


# Function to draw a line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], color='tab:red')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.show()
    return fig


def draw_bar_plot():
    # Make sure the index is in datetime format
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index, errors='coerce')  # Convert to datetime if necessary

    # Extract 'year' and 'month' from the datetime index
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group data by year and month and calculate the mean for each group
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Plotting
    fig = df_bar.plot(kind="bar", figsize=(10, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()
    return fig
def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)  # Converts the index to a regular column named 'date'
    df_box['date'] = pd.to_datetime(df_box['date'])  # Explicitly convert 'date' to datetime

    # Extract year and month information
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month

    # Sort by month number to ensure correct order in the box plot
    df_box = df_box.sort_values('month_num')

    # Draw the box plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])

    # Customize plot titles and labels
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.show()
    return fig
# Calling the functions to generate and display plots
draw_line_plot()
draw_bar_plot()
draw_box_plot()
