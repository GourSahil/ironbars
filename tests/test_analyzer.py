import pandas as pd
import numpy as np
from pathlib import Path
import random
import ironbars.core.analyzer as analyzer

PATH = Path(__file__).parent
special_dump = False

def run_analyzer(dataframe: pd.DataFrame, export_prefix: str, dump=False):
    """
    Helper function to analyze dataframe and export both
    dataset + metadata for manual inspection.
    """
    a = analyzer.Analyzer()
    metadata = a.analyze(dataframe)

    # Assertions (structure validation)
    assert isinstance(metadata, analyzer.Metadata)
    assert isinstance(metadata.columns, dict)

    for column, meta in metadata.columns.items():
        assert "dtype" in meta
        assert "length" in meta
        assert "unique_score" in meta
        assert "missing_score" in meta
        assert "diff_score" in meta
        assert "semantic_type" in meta

    # Save dataset
    if dump:
        dataframe.to_csv(PATH / f"{export_prefix}_dataset.csv", index=False)

    # Convert metadata dict to DataFrame
    metadata_df = pd.DataFrame.from_dict(metadata.columns, orient="index")
    metadata_df.index.name = "column"

    # Save metadata
    if dump:
        metadata_df.to_csv(PATH / f"{export_prefix}_metadata.csv")

    return metadata


def test_analyzer_with_random_data():
    df = pd.DataFrame({
        "numeric_col": np.random.rand(100),
        "categorical_col": [random.choice(["A", "B", "C"]) for _ in range(100)],
        "datetime_col": pd.date_range(start="2020-01-01", periods=100, freq="D"),
        "identifier_col": [f"id_{i}" for i in range(100)],
        "categorical_numeric_col": [random.choice([1, 2, 3]) for _ in range(100)],
    })

    run_analyzer(df, export_prefix="random_data")

def test_edge_all_missing():
    df = pd.DataFrame({
        "all_missing": [np.nan] * 100
    })

    metadata = run_analyzer(df, export_prefix="edge_all_missing")

    assert metadata.columns["all_missing"]["semantic_type"] == "empty"

def test_edge_constant_column():
    df = pd.DataFrame({
         "constant_col": [42] * 100
     })

    metadata = run_analyzer(df, export_prefix="edge_constant")

    assert metadata.columns["constant_col"]["semantic_type"] == "constant"

def test_edge_sequential_float():
    df = pd.DataFrame({
        "float_seq": np.arange(0.0, 100.0)
    })

    metadata = run_analyzer(df, export_prefix="edge_float_seq")

    assert metadata.columns["float_seq"]["semantic_type"] == "identifier"

def test_edge_binary_numeric():
    df = pd.DataFrame({
        "binary_col": [random.choice([0, 1]) for _ in range(200)]
    })

    metadata = run_analyzer(df, export_prefix="edge_binary")

    assert metadata.columns["binary_col"]["semantic_type"] == "categorical_numeric"

def test_edge_high_cardinality_string():
    df = pd.DataFrame({
        "user_id": [f"user_{i}" for i in range(200)]
    })

    metadata = run_analyzer(df, export_prefix="edge_string_identifier")

    assert metadata.columns["user_id"]["semantic_type"] == "identifier"

def test_edge_high_cardinality_string():
    df = pd.DataFrame({
        "user_id": [f"user_{i}" for i in range(200)]
    })

    metadata = run_analyzer(df, export_prefix="edge_string_identifier")

    assert metadata.columns["user_id"]["semantic_type"] == "identifier"

def test_edge_mixed_types():
    df = pd.DataFrame({
        "mixed_col": [1, "A", 3, None, "B"] * 20
    })

    metadata = run_analyzer(df, export_prefix="edge_mixed")

    # Mixed should not crash and should default safely
    assert metadata.columns["mixed_col"]["semantic_type"] in ["categorical", "unknown"]

def test_edge_mostly_missing():
    df = pd.DataFrame({
        "mostly_missing": [np.nan] * 90 + list(range(10))
    })

    metadata = run_analyzer(df, export_prefix="edge_mostly_missing")

    assert metadata.columns["mostly_missing"]["missing_score"] > 0.8