from src.data_loader import SolarDataLoader
from src.eda_utils import plot_time_series

def main():
    """
    Example script to load data and display basic info.
    """
    # Load Benin cleaned data
    loader = SolarDataLoader("data/benin_clean.csv")
    df = loader.load()
    loader.info()
    print(loader.head())

    # Example plot (uncomment and update column names as needed)
    # plot_time_series(df, date_col="date", value_col="solar_output")

if __name__ == "__main__":
    main()