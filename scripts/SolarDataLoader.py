import pandas as pd

class SolarDataLoader:
    """
    Loads and inspects solar energy datasets.

    Attributes:
        filepath (str): Path to the CSV data file.
        data (pd.DataFrame): Loaded data.
    """

    def __init__(self, filepath):
        """
        Initialize the loader with a file path.
        """
        self.filepath = filepath
        self.data = None

    def load(self):
        """
        Load CSV data into a pandas DataFrame.

        Returns:
            pd.DataFrame: Loaded data.
        """
        self.data = pd.read_csv(self.filepath)
        return self.data

    def info(self):
        """
        Print DataFrame info.
        """
        if self.data is not None:
            print(self.data.info())
        else:
            print("Data not loaded yet.")

    def head(self, n=5):
        """
        Return the first n rows.

        Args:
            n (int): Number of rows to return.

        Returns:
            pd.DataFrame: First n rows.
        """
        if self.data is not None:
            return self.data.head(n)
        else:
            print("Data not loaded yet.")