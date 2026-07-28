# 📘 Data Dictionary

<p align="center">
  <strong>Variable definitions for the VR ECG Digital Twin Training Study</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Students-53-blue" alt="53 students">
  <img src="https://img.shields.io/badge/Healthcare%20Professionals-6-green" alt="6 healthcare professionals">
  <img src="https://img.shields.io/badge/Scale-Likert%201--5-orange" alt="Likert scale">
</p>

---

## 📖 Overview

This file describes the variables included in:

```text
students_anonymized.csv
healthcare_professionals_anonymized.csv
```

Each row represents one participant.

All closed-ended questions use a five-point Likert scale:

| Value | Meaning |
|---:|---|
| 1 | Strongly disagree |
| 2 | Disagree |
| 3 | Neutral |
| 4 | Agree |
| 5 | Strongly agree |

Empty fields indicate that no response was provided.

---

# 🎓 Student dataset

## File

```text
students_anonymized.csv
```

## Variables

| Variable | Type | Values | Description |
|---|---|---|---|
| `participant_id` | Text | `STU001`, `STU002`, ... | Public anonymous participant code. |
| `ease_of_use` | Integer | 1–5 | The VR application was easy to use and understand. |
| `interface_intuitive` | Integer | 1–5 | The interface was intuitive. |
| `improved_ecg_understanding` | Integer | 1–5 | The VR experience improved my understanding of ECG concepts. |
| `increased_interpretation_confidence` | Integer | 1–5 | I feel more confident interpreting ECGs after using the application. |
| `simulation_motivating` | Integer | 1–5 | The simulation experience was engaging and motivating. |
| `realistic_learning_situations` | Integer | 1–5 | The virtual environment reflects realistic learning situations. |
| `active_learning` | Integer | 1–5 | The application facilitated active learning. |
| `useful_for_peers` | Integer | 1–5 | The application would be useful for other students at my academic level. |
| `overall_satisfaction` | Integer | 1–5 | Overall, I am satisfied with the experience. |
| `recommend_academic_training` | Integer | 1–5 | I would recommend this VR application for medical education. |
| `improvement_feedback` | Text | Free text or empty | Suggestions for improving or changing the application. |

## Column order

```csv
participant_id,ease_of_use,interface_intuitive,improved_ecg_understanding,increased_interpretation_confidence,simulation_motivating,realistic_learning_situations,active_learning,useful_for_peers,overall_satisfaction,recommend_academic_training,improvement_feedback
```

---

# 🩺 Healthcare-professional dataset

## File

```text
healthcare_professionals_anonymized.csv
```

## Variables

| Variable | Type | Values | Description |
|---|---|---|---|
| `participant_id` | Text | `HCP001`, `HCP002`, ... | Public anonymous participant code. |
| `clinical_pattern_accuracy` | Integer | 1–5 | The ECG simulation model accurately reflects real clinical patterns. |
| `formative_evaluation` | Integer | 1–5 | The application supports effective formative assessment for cardiology learning. |
| `visual_dynamic_representation` | Integer | 1–5 | The visual and dynamic ECG representation is suitable for educational purposes. |
| `clinical_workflow_alignment` | Integer | 1–5 | The design supports a workflow consistent with clinical practice. |
| `integration_medical_training` | Integer | 1–5 | The application could be integrated into medical training programmes. |
| `physiological_parameter_customization` | Integer | 1–5 | The physiological parameters provide sufficient customisation for different scenarios. |
| `consistency_real_cases` | Integer | 1–5 | The application results are consistent with those expected in real cases. |
| `research_specialized_training` | Integer | 1–5 | The application could be useful for research or specialised training. |
| `overall_usability` | Integer | 1–5 | The overall usability of the system is satisfactory. |
| `recommend_professional_advanced_teaching` | Integer | 1–5 | I would recommend its use in professional or advanced teaching contexts. |
| `improvement_feedback` | Text | Free text or empty | Suggestions for improving or changing the application. |

## Column order

```csv
participant_id,clinical_pattern_accuracy,formative_evaluation,visual_dynamic_representation,clinical_workflow_alignment,integration_medical_training,physiological_parameter_customization,consistency_real_cases,research_specialized_training,overall_usability,recommend_professional_advanced_teaching,improvement_feedback
```

---

## 🔐 Notes

- Participant identifiers are anonymous public codes.
- Exact response timestamps are not included.
- Open-ended student comments were translated into English.
- The questionnaires are exploratory and are not validated psychometric instruments.
- Student and healthcare-professional responses should be analysed separately.

---

## 📄 Version

```text
Version: 1.0
Language: English
Response scale: Likert 1–5
Study status: Manuscript under review in Virtual Reality
```
