# Ironbars
![Python](https://img.shields.io/badge/Python-3.10%2B-blue) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

**IronBars** is a Python library that automatically analyzes tabular datasets and
suggests the most suitable visualizations and preprocessing ideas. Instead
of manually guessing which plots to use, IronBars guides you with clean,
interpretive visual suggestions tailored to your data types and relationships.

```bash
 Transform raw datasets into meaningful visual insights through automated,
 Intelligent plot selection.
```
---
## Scope
**IronBars** focuses on :-
1. Focused on **Auto EDA (Exploratory Data Analysis)**
2. Suggests and generates suitable plots
3. Designed for structured tabular datasets (CSV / pandas DataFrame)
4. Intended for students, analysts, and ML beginners

## Out of Scope
IronBars does not aim to:
1. Replace full business intelligence platforms
2. Perform automated machine learning
3. Provide deep statistical infer
4. Act as a dashboard framework

---

## Installation Instructions
> Currently library is under development, I will publish it soon over pypi. If you really wanna use the code, just simply clone the repository and import the ironbars in your code.

## Usage
> Currently first version isn't made yet, This part will be updated as I publish the first version.

## How IronBars Thinks

IronBars analyzes each column using structural signals:

1. Uniqueness ratio
2. Missing ratio
3. Volatility score (normalized difference)
4. Datatype detection

These signals are combined into deterministic rules to assign a semantic type to each column.