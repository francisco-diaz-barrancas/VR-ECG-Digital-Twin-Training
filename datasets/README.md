# 🫀 ECG Dataset

<p align="center">
  <strong>Parameter-based ECG profiles for classification and educational simulation</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Samples-3%2C000-blue" alt="3,000 samples">
  <img src="https://img.shields.io/badge/Features-8-green" alt="8 input features">
  <img src="https://img.shields.io/badge/Classes-6-orange" alt="6 diagnosis classes">
  <img src="https://img.shields.io/badge/Data-Synthetic-lightgrey" alt="Synthetic data">
</p>

---

## 📖 Overview

This directory contains the synthetic dataset used in the study:

> **Enhancing Medical Education with Virtual Reality: A Digital Twin for ECG Training**

The dataset represents parameter-based ECG profiles designed for machine-learning classification and educational simulation.

It contains **3,000 synthetic samples** generated from clinically meaningful ECG parameters. Each sample includes eight input features and one diagnosis label.

> **Important:** This dataset does not contain real patient records or identifiable clinical information. It is intended for research, software testing, reproducibility, and educational use.

---

## 🗂️ File

```text
ecg_dataset.csv
```

### Dataset summary

| Property | Value |
|---|---:|
| Samples | 3,000 |
| Input features | 8 |
| Target variable | 1 |
| Diagnosis classes | 6 |
| Missing values | 0 |
| Duplicate rows | 0 |
| File format | CSV |
| Encoding | UTF-8 |

---

## 🧩 Variables

| Variable | Type | Unit / values | Description |
|---|---|---|---|
| `Heart_Rate` | Numeric | beats per minute | Estimated number of cardiac cycles per minute. |
| `PR_Interval` | Numeric | milliseconds | Time from the onset of atrial depolarisation to the onset of ventricular depolarisation. |
| `QRS_Duration` | Numeric | milliseconds | Duration of ventricular depolarisation. |
| `ST_Segment` | Numeric | relative deviation | Simulated ST-segment displacement from the baseline. Negative values represent depression and positive values represent elevation. |
| `QTc_Interval` | Numeric | milliseconds | Heart-rate-corrected QT interval. |
| `Electrical_Axis` | Numeric | degrees | Simulated mean electrical axis of ventricular depolarisation. |
| `Rhythm` | Categorical | See below | Cardiac rhythm associated with the ECG profile. |
| `T_Wave` | Categorical | See below | Simulated T-wave morphology. |
| `Diagnosis` | Categorical | 6 classes | Target category assigned to the ECG profile. |

---

## 📏 Observed numerical ranges

These ranges describe the values present in the published CSV file.

| Variable | Minimum | Maximum | Mean |
|---|---:|---:|---:|
| `Heart_Rate` | 30.83 | 122.71 | 77.05 |
| `PR_Interval` | 70.43 | 251.58 | 164.68 |
| `QRS_Duration` | 66.25 | 141.34 | 104.72 |
| `ST_Segment` | -2.03 | 2.94 | 0.35 |
| `QTc_Interval` | 331.48 | 523.70 | 420.09 |
| `Electrical_Axis` | -112.72 | 101.30 | -0.50 |

Values are stored as floating-point numbers.

---

## 🔤 Categorical values

### Rhythm

| Category | Samples |
|---|---:|
| `Sinus` | 1,500 |
| `Bradycardia` | 500 |
| `Tachycardia` | 500 |
| `Atrial Fibrillation` | 500 |

### T-wave morphology

| Category | Samples |
|---|---:|
| `Normal` | 746 |
| `Inverted` | 772 |
| `Flattened` | 749 |
| `Peaked` | 733 |

---

## 🎯 Diagnosis classes

The target column is:

```text
Diagnosis
```

The dataset contains six balanced diagnosis categories:

| Diagnosis | Samples | Percentage |
|---|---:|---:|
| `Normal` | 500 | 16.67% |
| `Bradycardia` | 500 | 16.67% |
| `Tachycardia` | 500 | 16.67% |
| `Atrial Fibrillation` | 500 | 16.67% |
| `Myocardial Infarction` | 500 | 16.67% |
| `Heart Block` | 500 | 16.67% |

The balanced class distribution supports reproducible comparison between classification approaches.

---

## 🔎 Example

```csv
Heart_Rate,PR_Interval,QRS_Duration,ST_Segment,QTc_Interval,Electrical_Axis,Rhythm,T_Wave,Diagnosis
51.5591,161.7455,129.1363,0.0556,451.0593,-15.4455,Bradycardia,Normal,Bradycardia
```

---

## 🧠 Intended use

The dataset may be used for:

- training and evaluating ECG-profile classifiers;
- reproducing the machine-learning experiments described in the study;
- testing preprocessing and normalisation pipelines;
- validating ONNX model conversion and deployment;
- developing educational ECG applications;
- generating configurable scenarios in virtual reality;
- demonstrating digital-twin workflows.

The input parameters are intended to be interpreted jointly. A single value should not be used in isolation to infer a diagnosis.

---

## 🐍 Loading the dataset with Python

```python
import pandas as pd

data = pd.read_csv("ecg_dataset.csv")

print(data.head())
print(data.shape)
print(data["Diagnosis"].value_counts())
```

### Separating features and target

```python
X = data.drop(columns=["Diagnosis"])
y = data["Diagnosis"]
```

Categorical variables such as `Rhythm` and `T_Wave` must be encoded before training most machine-learning models.

---

<p align="center">
  <strong>Synthetic ECG data for reproducible research and immersive medical education.</strong>
</p>
