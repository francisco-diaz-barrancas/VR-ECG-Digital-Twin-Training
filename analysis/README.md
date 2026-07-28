# 📈 Analysis

This directory contains the reproducible descriptive analysis for the study:

> **Enhancing Medical Education with Virtual Reality: A Digital Twin for ECG Training**

## Files

```text
analysis/
├── README.md
├── descriptive_analysis.py
└── requirements.txt
```

The generated outputs are stored automatically in:

```text
analysis/results/
```

## What the script calculates

For every Likert-scale item and participant group, the script calculates:

- number of valid responses;
- number of missing responses;
- mean;
- sample standard deviation;
- median;
- first and third quartiles;
- interquartile range;
- minimum and maximum;
- frequency and percentage for responses 1–5;
- number and percentage of favourable responses rated 4 or 5.

It also exports the non-empty open-ended comments and generates graphical summaries.

## Expected repository structure

```text
VR-ECG-Digital-Twin-Training/
├── analysis/
│   ├── README.md
│   ├── descriptive_analysis.py
│   └── requirements.txt
└── data/
    ├── students_anonymized.csv
    └── healthcare_professionals_anonymized.csv
```

## Installation

From the repository root, install the dependencies:

```bash
pip install -r analysis/requirements.txt
```

## Run the analysis

```bash
python analysis/descriptive_analysis.py
```

## Generated outputs

```text
analysis/results/
├── combined_descriptive_statistics.csv
├── descriptive_analysis_report.md
├── students_descriptive_statistics.csv
├── students_response_frequencies.csv
├── students_feedback.csv
├── students_mean_scores.png
├── students_favourable_responses.png
├── students_likert_distribution.png
├── healthcare_professionals_descriptive_statistics.csv
├── healthcare_professionals_response_frequencies.csv
├── healthcare_professionals_feedback.csv
├── healthcare_professionals_mean_scores.png
├── healthcare_professionals_favourable_responses.png
└── healthcare_professionals_likert_distribution.png
```

## Optional custom paths

```bash
python analysis/descriptive_analysis.py   --data-dir path/to/data   --output-dir path/to/results
```

The two participant groups are analysed separately because they completed different questionnaires.
