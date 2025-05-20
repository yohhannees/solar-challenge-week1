# Solar Challenge – Week 1

Welcome to the first week of the Solar Challenge!  
This repository showcases an analysis of solar energy generation in **Benin**, **Sierra Leone**, and **Togo**, focusing on:

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Dashboard Creation

---

## 📦 Getting Started

### 1. Clone This Repository

```bash
git clone https://github.com/yohhannees/solar-challenge-week1.git
cd solar-challenge-week1
```

### 2. Set Up Your Python Environment

You can use either `venv` or `conda` to manage your environment:

#### 🔹 With `venv` (Python built-in)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 🔹 With conda

```bash
conda create -n solar-challenge python=3.10
conda activate solar-challenge
```

### 3. Install Dependencies

After activating your environment, install the required packages:

```bash
pip install -r requirements.txt
```

This will ensure all necessary libraries are available for running notebooks and scripts.

---

## 🗂️ Project Structure

Here’s a summary of the main folders and files:

```bash
solar-challenge-week1/
├── .github/                # GitHub workflow files
├── data/                   # Raw and processed datasets
│   ├── benin_clean.csv
│   ├── benin-malanville.csv
│   ├── sierra_leone_clean.csv
│   ├── sierra_leone-bumbuna.csv
│   ├── togo_clean.csv
│   └── togo-dapaong_qc.csv
│
├── notebooks/              # Jupyter notebooks for analysis
│   ├── benin_eda.ipynb
│   ├── SierraLeone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── README.md
│
├── scripts/                # Helper scripts (optional)
├── src/                    # Core utility code
├── tests/                  # Test files
├── venv/                   # Virtual environment (not tracked by git)
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Usage Guide

To analyze the solar data for each country, open the relevant Jupyter notebook in the `notebooks/` directory:

- `benin_eda.ipynb`
- `SierraLeone_eda.ipynb`
- `togo_eda.ipynb`

Each notebook covers:

- ✅ Initial data exploration
- 🧹 Missing value treatment
- 📈 Time series plots
- 📊 Statistical analysis
- 📅 Daily and monthly trends

Launch Jupyter and start exploring!

---

## 🛠 Technology Stack

This project leverages:

- **Python 3.10** – Main programming language
- **Jupyter Notebooks** – Interactive analysis
- **Pandas**, **NumPy** – Data processing and computation
- **Matplotlib**, **Seaborn** – Data visualization

These tools enable efficient data analysis and clear visual insights.
