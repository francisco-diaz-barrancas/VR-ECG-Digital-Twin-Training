# 📊 Study Data

<p align="center">
  <strong>Anonymised questionnaire responses from the VR ECG Digital Twin Training Study</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Students-53-blue" alt="53 students">
  <img src="https://img.shields.io/badge/Healthcare%20Professionals-6-green" alt="6 healthcare professionals">
  <img src="https://img.shields.io/badge/Scale-Likert%201--5-orange" alt="Likert scale">
  <img src="https://img.shields.io/badge/Data-Anonymised-lightgrey" alt="Anonymised data">
</p>

---

## 📖 Overview

This directory contains the anonymised questionnaire responses associated with the study:

> **Enhancing Medical Education with Virtual Reality: A Digital Twin for ECG Training**

The study evaluates a virtual reality environment designed to support ECG education through:

- electrode-placement practice;
- interactive ECG visualisation;
- physiological-parameter manipulation;
- ECG-profile classification;
- immediate educational feedback.

The data were collected from two participant groups:

| Participant group | Number of participants |
|---|---:|
| Medical students | 53 |
| Healthcare professionals | 6 |
| **Total** | **59** |

The two groups are stored and analysed separately because they completed different questionnaires and evaluated the system from different perspectives.

---

## 🗂️ Files

```text
data/
│
├── README.md
├── data_dictionary.md
├── students_anonymized.csv
└── healthcare_professionals_anonymized.csv
```

| File | Description |
|---|---|
| `students_anonymized.csv` | Responses from 53 medical students |
| `healthcare_professionals_anonymized.csv` | Responses from 6 healthcare professionals |
| `data_dictionary.md` | Definition, format and permitted values of each variable |
| `README.md` | General description of the public datasets |

---

## 🎓 Student dataset

### File

```text
students_anonymized.csv
```

Each row represents one medical student.

The dataset contains:

- one anonymised participant identifier;
- ten Likert-scale responses;
- one optional open-ended feedback field.

### Variables

```text
participant_id
ease_of_use
interface_intuitive
improved_ecg_understanding
increased_interpretation_confidence
simulation_motivating
realistic_learning_situations
active_learning
useful_for_peers
overall_satisfaction
recommend_academic_training
improvement_feedback
```

### Evaluation dimensions

The student questionnaire assesses:

- ease of use and understanding;
- interface intuitiveness;
- perceived improvement in ECG understanding;
- confidence in ECG interpretation;
- motivation and engagement;
- realism of the learning environment;
- active learning;
- usefulness for other students;
- overall satisfaction;
- recommendation for medical education.

---

## 🩺 Healthcare-professional dataset

### File

```text
healthcare_professionals_anonymized.csv
```

Each row represents one healthcare professional.

The dataset contains:

- one anonymised participant identifier;
- ten Likert-scale responses;
- one optional open-ended feedback field.

### Variables

```text
participant_id
clinical_pattern_accuracy
formative_evaluation
visual_dynamic_representation
clinical_workflow_alignment
integration_medical_training
physiological_parameter_customization
consistency_real_cases
research_specialized_training
overall_usability
recommend_professional_advanced_teaching
improvement_feedback
```

### Evaluation dimensions

The healthcare-professional questionnaire assesses:

- clinical plausibility of the simulated ECG patterns;
- usefulness for formative assessment;
- visual and dynamic ECG representation;
- alignment with clinical workflow;
- potential integration into medical training;
- physiological-parameter customisation;
- consistency with expected real cases;
- usefulness for research or specialised training;
- overall usability;
- recommendation for professional or advanced teaching.

---

## ⭐ Response scale

All closed-ended items use a five-point Likert scale:

| Value | Meaning |
|---:|---|
| 1 | Strongly disagree |
| 2 | Disagree |
| 3 | Neutral |
| 4 | Agree |
| 5 | Strongly agree |

Empty fields represent unanswered or non-applicable responses where applicable.

The value `0` is not used as a valid response or as a missing-value code.

---

## 🔐 Data preparation and anonymisation

Before publication, the datasets were prepared as follows:

- exact response timestamps were removed;
- names and email addresses were excluded;
- public participant identifiers were generated;
- column names were standardised in English;
- references to previous tool names were removed;
- open-ended student responses were translated into English;
- potentially identifying information was reviewed;
- the final student record was excluded during data cleaning;
- open-ended feedback was retained when suitable for public release.

Public participant identifiers follow these formats:

```text
STU001, STU002, STU003, ...
HCP001, HCP002, HCP003, ...
```

These identifiers were created specifically for the public repository.

The datasets do not contain:

- names or surnames;
- email addresses;
- IP addresses;
- exact timestamps;
- institutional identifiers;
- internal participant codes;
- identifiable medical records;
- patient information.

Users must not attempt to re-identify participants or combine these datasets with external information for that purpose.

---

## 📝 Open-ended feedback

The variable:

```text
improvement_feedback
```

contains optional suggestions and comments provided by participants.

Student comments were translated from Spanish into English while preserving their original meaning.

Empty cells indicate that the participant did not provide an open-ended response.

Open-ended responses should be interpreted qualitatively and should not be treated as Likert-scale data.

---

## 📈 Recommended analyses

For each Likert-scale item, the following descriptive statistics may be calculated:

- number of valid responses;
- mean;
- standard deviation;
- median;
- interquartile range;
- minimum and maximum;
- frequency of each response option;
- percentage of responses equal to or greater than 4.

The percentage of favourable responses can be calculated as:

```text
Number of responses rated 4 or 5
──────────────────────────────── × 100
Number of valid responses
```

The student and healthcare-professional datasets should be analysed separately.

---

## ⚠️ Interpretation

The questionnaire responses represent participant perceptions of:

- usability;
- realism;
- motivation;
- satisfaction;
- educational usefulness;
- potential applicability.

The data do not independently demonstrate:

- objective learning gains;
- clinical competence;
- diagnostic accuracy;
- clinical validity;
- medical-device performance.

The questionnaires were developed for this exploratory evaluation and should not be presented as validated psychometric instruments.

---

## ♻️ Reuse

These datasets may be used for:

- reproducing the descriptive analyses reported in the manuscript;
- secondary research;
- usability studies;
- educational-technology research;
- comparison with future versions of the VR environment.

Users of the data should:

- cite the associated manuscript and repository;
- preserve the meaning of the original variables;
- clearly report any data transformations;
- avoid attempting to identify participants;
- state that the questionnaires are exploratory instruments;
- analyse both participant groups separately unless a combined analysis is justified.

---

## 📘 Data dictionary

Detailed information about every variable is available in:

```text
data_dictionary.md
```

The data dictionary includes:

- variable names;
- variable descriptions;
- data types;
- permitted values;
- questionnaire wording;
- missing-value conventions;
- recommended column order.

---


<p align="center">
  <strong>Virtual reality and digital twins for ECG education.</strong>
</p>
