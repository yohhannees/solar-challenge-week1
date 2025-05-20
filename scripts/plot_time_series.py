import matplotlib.pyplot as plt

def plot_time_series(df, date_col, value_col, title="Time Series Plot"):
    """
    Plot a time series from a DataFrame.

    Args:
        df (pd.DataFrame): Data to plot.
        date_col (str): Name of the date column.
        value_col (str): Name of the value column.
        title (str): Plot title.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(df[date_col], df[value_col])
    plt.title(title)
    plt.xlabel(date_col)
    plt.ylabel(value_col)
    plt.tight_layout()
    plt.show()