Data

This directory contains the anonymised questionnaire data associated with the study:

Enhancing Medical Education with Virtual Reality: A Digital Twin for ECG Training

The datasets include responses from medical students and healthcare professionals who evaluated the VR-based ECG training environment.

Files

File

Participants

Description

students_anonymized.csv

53

Anonymised responses from medical students.

healthcare_professionals_anonymized.csv

6

Anonymised responses from healthcare professionals.

data_dictionary.md

—

Definitions, formats, and permitted values for all variables.

Data structure

Each row represents one participant.

The datasets contain:

one public pseudonymous participant identifier;

ten closed-ended questionnaire responses;

one optional open-ended feedback field.

The public participant identifiers follow these formats:

students: STU001, STU002, ...

healthcare professionals: HCP001, HCP002, ...

These identifiers were created specifically for the public repository and are not linked to names, email addresses, consent forms, or internal research identifiers.

Response scale

All closed-ended items use a five-point Likert scale:

Value

Meaning

1

Strongly disagree

2

Disagree

3

Neutral

4

Agree

5

Strongly agree

Missing responses, where applicable, are represented by an empty field.

Student dataset

The student dataset contains the following columns:

participant_id, ease_of_use, interface_intuitive, improved_ecg_understanding, increased_interpretation_confidence, simulation_motivating, realistic_learning_situations, active_learning, useful_for_peers, overall_satisfaction, recommend_academic_training, improvement_feedback

The questionnaire evaluates:

ease of use;

interface intuitiveness;

perceived improvement in ECG understanding;

confidence in ECG interpretation;

motivation and engagement;

realism of the learning environment;

active learning;

usefulness for students at a similar academic level;

overall satisfaction;

recommendation for medical education;

suggestions for improvement.

Healthcare-professional dataset

The healthcare-professional dataset contains the following columns:

participant_id, clinical_pattern_accuracy, formative_evaluation, visual_dynamic_representation, clinical_workflow_alignment, integration_medical_training, physiological_parameter_customization, consistency_real_cases, research_specialized_training, overall_usability, recommend_professional_advanced_teaching, improvement_feedback

The questionnaire evaluates:

clinical plausibility of the ECG patterns;

usefulness for formative assessment;

quality of the visual and dynamic representation;

alignment with clinical workflow;

potential integration into medical training;

customisation of physiological parameters;

consistency with expected real cases;

usefulness for research or specialised training;

overall usability;

recommendation for professional or advanced teaching;

suggestions for improvement.

Data preparation

Before publication, the datasets were prepared as follows:

exact response timestamps were removed;

direct personal identifiers were excluded;

public participant codes were generated;

column names were standardised in English;

references to the previous tool name were removed;

open-ended student comments were translated into English;

the final student response was excluded during data cleaning;

the open-ended feedback column was retained.

Anonymisation

The public files do not contain:

names or surnames;

email addresses;

IP addresses;

exact timestamps;

institutional identifiers;

internal participant codes;

consent documentation.

Open-ended responses were reviewed and translated to reduce the risk of disclosing identifying information.

Users must not attempt to re-identify participants or combine these data with external information for that purpose.

Recommended use

These datasets may be used for:

reproducing the descriptive analyses reported in the manuscript;

secondary research;

educational-methodology studies;

usability and acceptance analyses;

comparison with future versions of the VR training environment.

The questionnaires were developed for an exploratory evaluation and should not be presented as validated psychometric instruments.

The data do not independently demonstrate:

objective learning gains;

clinical competence;

diagnostic accuracy;

medical-device performance;

clinical validity.
