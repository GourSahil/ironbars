import pandas as pd

class Metadata:
    columns: dict[str, dict[str, str]]

class Analyzer:
    """
    The `Analyzer` class is responsible for analyzing the source code of a project to identify potential issues, code smells, and areas for improvement. It uses various techniques such as static code analysis, pattern recognition, and heuristics to evaluate the codebase.
    """
    def __init__(self):
        self.name = __name__

    def __get_semantic_type(self, meta: dict) -> str:
        """ Determine the semantic type of a column based on its metadata.

        Args:
            meta (dict): Metadata dictionary for a column containing dtype, unique_score, diff_score, missing_score, and unique_count.

        Returns:
            str: Semantic type of the column (e.g., "identifier", "categorical", "continuous", "datetime", "empty", "constant", "categorical_numeric", or "unknown").
        """
        dtype = meta["dtype"]
        unique_score = meta["unique_score"]
        diff_score = meta["diff_score"]
        missing_score = meta["missing_score"]
        unique_count = meta["unique_count"]

        # Empty column
        if missing_score == 1.0:
            return "empty"

        # Datetime
        if pd.api.types.is_datetime64_any_dtype(dtype):
            return "datetime"

        # Numeric types
        if pd.api.types.is_numeric_dtype(dtype):

            if unique_count == 1:
                return "constant"

            if unique_score > 0.95 and diff_score < 0.1:
                return "identifier"

            if unique_score < 0.1:
                return "categorical_numeric"

            return "continuous"

        # Text / object
        if pd.api.types.is_object_dtype(dtype) or pd.api.types.is_string_dtype(dtype):

            if unique_score > 0.95:
                return "identifier"

            return "categorical"

        return "unknown"

    def __generate_meadata(self, df:pd.DataFrame) -> Metadata:
        """ Generate metadata for a given DataFrame by analyzing each column's properties.

        Args:
            df (pd.DataFrame): The input DataFrame for which metadata needs to be generated.

        Returns:
            Metadata: An object containing metadata information for each column in the DataFrame, including dtype, length, unique_score, missing_score, diff_score, and semantic_type.
        """
        metadata = Metadata()
        metadata.columns = {}
        for column in df.columns:
            metadata.columns[column] = {
                "dtype": str(df[column].dtype),
                "length": len(df[column]),
                "unique_count": df[column].dropna().nunique(),
                "unique_score": round(df[column].nunique()/len(df), 3),
                "missing_score": round(df[column].isnull().sum()/len(df), 3),
                "diff_score": -1,
            }

            if pd.api.types.is_numeric_dtype(df[column]):
                diffs = df[column].diff().dropna()
                # normalize the diff score to be between 0 and 1, where 0 means no variation and 1 means high variation
                if len(diffs) == 0:
                    metadata.columns[column]["diff_score"] = 0
                else:
                    std_diff = diffs.std()
                    mean_abs_diff = abs(diffs.mean())
                    raw_score = std_diff / (mean_abs_diff + 1e-9)
                    diff_score = raw_score / (1 + raw_score)
                    metadata.columns[column]["diff_score"] = round(diff_score, 3)
            
            # setting the metadata semantic type
            metadata.columns[column]["semantic_type"] = self.__get_semantic_type(metadata.columns[column])

        return metadata

    def analyze(self, df: pd.DataFrame) -> Metadata:
        """Analyze a DataFrame and return metadata.

        Args:
            df (pd.DataFrame): The DataFrame to analyze.

        Returns:
            Metadata: Metadata object containing the analysis results for each column in the DataFrame.
        """
        return self.__generate_meadata(df)