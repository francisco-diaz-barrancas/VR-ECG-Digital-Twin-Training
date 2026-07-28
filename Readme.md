# 🫀 VR ECG Digital Twin Training

<p align="center">
  <strong>Research materials for the study:</strong><br>
  <em>Enhancing Medical Education with Virtual Reality: A Digital Twin for ECG Training</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Virtual%20Reality-Meta%20Quest%203-blue" alt="Virtual Reality">
  <img src="https://img.shields.io/badge/Development-Unity-black" alt="Unity">
  <img src="https://img.shields.io/badge/AI-ONNX-orange" alt="ONNX">
  <img src="https://img.shields.io/badge/Application-ECG%20Training-red" alt="ECG Training">
  <img src="https://img.shields.io/badge/Study-Pilot%20Evaluation-green" alt="Pilot Study">
</p>

---

## 📖 Overview

This repository contains the questionnaires, anonymised participant-level data, analysis materials, and methodological documentation associated with the manuscript:

> **Enhancing Medical Education with Virtual Reality: A Digital Twin for ECG Training**

The project presents a virtual reality training environment that combines:

- 12-lead ECG electrode-placement practice;
- an interactive virtual patient;
- parameter-driven ECG visualisation;
- a cardiac digital twin;
- ECG-profile classification;
- on-device artificial intelligence;
- immediate educational feedback.

The application was developed in **Unity** and designed for deployment on the **Meta Quest 3**.

---

## 🎯 Study purpose

The study evaluates the application as a pilot and exploratory educational tool.

The main objectives are to assess:

- usability and ease of interaction;
- perceived realism of the virtual environment;
- clarity of the ECG representations;
- perceived educational usefulness;
- motivation and engagement;
- acceptance among medical students and healthcare professionals;
- potential improvements to the application.

The study does not evaluate the application as a certified medical device and does not establish clinical diagnostic validity.

---

## 🗂️ Repository structure

VR-ECG-Digital-Twin-Training/
│
├── README.md
├── LICENSE.md
├── CITATION.cff
│
├── questionnaires/
│   ├── student_questionnaire.pdf
│   └── healthcare_professional_questionnaire.pdf
│
├── data/
│   ├── students_anonymized.csv
│   ├── healthcare_professionals_anonymized.csv
│   ├── data_dictionary.md
│   └── README.md
│
├── datasets/
│   ├── ecg_dataset.csv
│   └── README.md
│
└── analysis/
    ├── descriptive_analysis.py
    ├── requirements.txt
    └── README.md


---

## 🥽 VR training workflow

During the virtual reality session, participants interact with a simulated clinical environment and complete the following sequence:

1. Place the required limb electrodes on the virtual patient.
2. Activate and observe the D2 waveform.
3. Place the six precordial electrodes from V1 to V6.
4. Visualise the complete 12-lead ECG.
5. Modify ECG-related parameters through the cardiac digital twin.
6. Observe the resulting changes in ECG morphology.
7. Classify the displayed ECG profile.
8. Compare the learner's selection with the AI-generated category.
9. Receive immediate educational feedback.

The learner performs a closed ECG-profile classification task using predefined rhythm or pathology categories. This activity is intended for educational purposes and does not constitute an unrestricted clinical diagnosis.

---

## 📋 Questionnaires

The `questionnaires/` directory contains the complete questionnaires administered during the study.

### Medical students

📄 `questionnaires/student_questionnaire.pdf`

The student questionnaire evaluates:

- ease of use;
- interface clarity;
- understanding of ECG concepts;
- confidence in ECG interpretation;
- motivation;
- active learning;
- perceived usefulness;
- satisfaction;
- willingness to recommend the application.

### Healthcare professionals

📄 `questionnaires/healthcare_professional_questionnaire.pdf`

The healthcare-professional questionnaire evaluates:

- clinical plausibility of the ECG profiles;
- quality of the visual representation;
- consistency with the ECG acquisition workflow;
- usefulness for formative assessment;
- parameter configuration;
- usability;
- potential application in healthcare education;
- suggestions for improvement.

> **Important:** These questionnaires were developed by the authors for this exploratory study. They should not be interpreted as psychometrically validated or standardised scales.

---

## 📊 Data

The `data/` directory contains anonymised participant-level responses.

### Student data

📁 `data/students_anonymized.csv`

Contains the anonymised questionnaire responses provided by medical students.

### Healthcare-professional data

📁 `data/healthcare_professionals_anonymized.csv`

Contains the anonymised questionnaire responses provided by healthcare professionals.

### Data dictionary

📘 `data/data_dictionary.md`

The data dictionary describes:

- variable names;
- variable definitions;
- data types;
- questionnaire items;
- response scales;
- permitted values;
- missing-value conventions.

The raw Google Forms exports and original research records are not included in this public repository.

---

## 🔐 Data protection and anonymisation

The public datasets contain no direct personal identifiers.

Before publication, the following information was removed or generalised where applicable:

- names and surnames;
- email addresses;
- exact response timestamps;
- IP addresses;
- internal participant identifiers;
- institutional identifiers;
- potentially identifying free-text responses;
- combinations of variables presenting a reasonable re-identification risk.

Public participant codes such as `STU001` and `HCP001` were created exclusively for this repository. They are not linked to the internal codes used during data collection.

The original data and informed-consent documentation are stored separately under restricted institutional access.

No patient records, clinical histories, biological samples, medical images, or identifiable patient information are included in this repository.

---

## 📈 Analysis

The `analysis/` directory contains the scripts and instructions required to reproduce the descriptive analyses reported in the manuscript.

The analyses may include:

- frequencies and percentages;
- means and standard deviations;
- medians and interquartile ranges;
- minimum and maximum values;
- item-level response distributions;
- graphical summaries;
- summaries of open-ended responses.

The results should be interpreted as exploratory and descriptive. They are not intended to demonstrate clinical validity or confirm educational effectiveness.

### Installation

Create a Python environment and install the required packages:

```bash
pip install -r analysis/requirements.txt
```

### Run the analysis

From the repository root:

```bash
python analysis/descriptive_analysis.py
```


---

## 📝 Citation

Please cite the associated manuscript:

```text
Díaz-Barrancas, F., Flores-Martin, D., Berrocal, J.,
Murillo, J. M., and Pardo, P. J.

Enhancing Medical Education with Virtual Reality:
A Digital Twin for ECG Training.
```

Citation metadata for this repository are available in:

```text
CITATION.cff
```

A permanent DOI will be added after the first archived release:

```text
DOI: [PENDING]
```

---

## 📄 Licence


| Resource | Recommended licence |
|---|---|
| Questionnaires | CC BY 4.0 |
| Anonymised datasets | CC BY 4.0 |

The definitive licence terms are provided in the `LICENSE` file.

---

## 👥 Authors

- **Francisco Díaz-Barrancas** — University of Extremadura
- **Daniel Flores-Martin** — COMPUTAEX Foundation
- **Javier Berrocal** — University of Extremadura
- **Juan M. Murillo** — University of Extremadura
- **Pedro J. Pardo** — University of Extremadura

---

## ✉️ Contact

**Francisco Díaz-Barrancas**  
University of Extremadura  
Email: `frdiaz@unex.es`

---

<p align="center">
  <strong>Virtual reality, digital twins, and artificial intelligence for ECG education.</strong>
</p>
