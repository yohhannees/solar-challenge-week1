import pandas as pd

class SolarDataLoader:
    """Loads and inspects solar energy datasets."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load(self):
        """Load CSV data into a pandas DataFrame."""
        self.data = pd.read_csv(self.filepath)
        return self.data

    def info(self):
        """Print DataFrame info."""
        if self.data is not None:
            print(self.data.info())
        else:
            print("Data not loaded yet.")

    def head(self, n=5):
        """Return the first n rows."""
        if self.data is not None:
            return self.data.head(n)
        else:
            print("Data not loaded yet.")