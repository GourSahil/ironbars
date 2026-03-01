# Changelog

All notable changes to IronBars will be documented in this file.

The format is based on semantic versioning (PEP 440 compliant).

---

## [0.1.0a1] - 2026-03-01

### Added
- Initial `Analyzer` implementation
- Column-level metadata generation
- Unique ratio (`unique_score`) calculation
- Missing ratio (`missing_score`) calculation
- Normalized volatility metric (`diff_score`)
- Semantic classification system:
  - `continuous`
  - `categorical`
  - `categorical_numeric`
  - `identifier`
  - `constant`
  - `empty`
  - `datetime`
- Edge case handling for:
  - Empty columns
  - Constant columns
  - Sequential identifiers
  - Mixed-type inputs
- Pytest-based test suite
- MkDocs documentation with API auto-generation
- GitHub Pages deployment

---

## Version Chart

IronBars  
└── 0.1.0a1 (Alpha Release) – March 1, 2026