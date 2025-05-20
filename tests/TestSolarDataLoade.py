import unittest
import pandas as pd
from src.data_loader import SolarDataLoader

class TestSolarDataLoader(unittest.TestCase):
    def setUp(self):
        # Create a small sample DataFrame and save as CSV for testing
        self.test_csv = "tests/test_sample.csv"
        df = pd.DataFrame({
            "date": ["2024-01-01", "2024-01-02"],
            "solar_output": [100, 150]
        })
        df.to_csv(self.test_csv, index=False)
        self.loader = SolarDataLoader(self.test_csv)

    def tearDown(self):
        import os
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_load(self):
        df = self.loader.load()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 2)
        self.assertIn("solar_output", df.columns)

    def test_head(self):
        self.loader.load()
        head = self.loader.head()
        self.assertEqual(len(head), 2)
        self.assertEqual(head.iloc[0]["solar_output"], 100)

if __name__ == "__main__":
    unittest.main()