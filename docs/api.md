# Api Reference

## Semantic Classification

IronBars classifies columns into the following semantic types:

- `continuous`
- `categorical`
- `categorical_numeric`
- `identifier`
- `constant`
- `empty`
- `datetime`

Classification is based on structural signals such as:

- Unique ratio
- Missing ratio
- Difference score (volatility)
- Datatype inspection

::: ironbars.core.analyzer.Analyzer

### Example Usage
```python
import pandas as pd
from ironbars import Analyzer

df = pd.DataFrame({
    "id": [1, 2, 3],
    "value": [10.5, 11.2, 13.4]
})

a = Analyzer()
metadata = a.analyze(df)

print(metadata.columns)
```