# This is the example of how to use the analyzer to analyze the code and get the result.
# You can run this code by using the command: python example_analyzer.py

# Dataset URL -> https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

import ironbars.core.analyzer as analyzer
import pandas as pd
import csv
from pathlib import Path

orig_path = Path(__file__).parent

# loading the dataset
df = pd.read_csv(orig_path / "datasets" / "diabetes.csv")
print("Dataset loaded successfully. Here are the first few rows:")
print(df.head())

# analyzing the dataset
Analyzer = analyzer.Analyzer()
metadata_df = Analyzer.analyze(df) # metadata is stored in the result variable, which is a Metadata object

# saving the result to csv and json files
metadata_df = pd.DataFrame.from_dict(metadata_df.columns, orient="index")
metadata_df.index.name = "column"
metadata_df.to_csv(orig_path / "results" / f"diabetes_metadata.csv")
metadata_df.to_json(orig_path / "results" / f"diabetes_metadata.json", orient="index", indent=4)
metadata_df.to_markdown(orig_path / "generated" / f"diabetes_metadata.md", index=True)

print("Metadata analysis completed. The results are saved in the results folder.")
print(metadata_df.head())
