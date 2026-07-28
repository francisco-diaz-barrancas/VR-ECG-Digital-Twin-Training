#!/usr/bin/env python3
"""
Descriptive analysis for the VR ECG Digital Twin Training Study.

The script reads the anonymised student and healthcare-professional CSV files,
validates their Likert responses, calculates descriptive statistics, exports
response frequencies and open-ended feedback, and creates publication-ready
figures.

Run from the repository root:

    python analysis/descriptive_analysis.py

Expected input files:

    data/students_anonymized.csv
    data/healthcare_professionals_anonymized.csv

Outputs are written to:

    analysis/results/
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LIKERT_VALUES = [1, 2, 3, 4, 5]
ID_COLUMN = "participant_id"
FEEDBACK_COLUMN = "improvement_feedback"


STUDENT_LABELS = {
    "ease_of_use": "Ease of use and understanding",
    "interface_intuitive": "Interface design is intuitive",
    "improved_ecg_understanding": "Improved understanding of ECGs",
    "increased_interpretation_confidence": "Increased confidence interpreting ECGs",
    "simulation_motivating": "Simulation experience was motivating",
    "realistic_learning_situations": "Simulation reflects real learning situations",
    "active_learning": "Facilitated active learning",
    "useful_for_peers": "Useful for peers at the same academic level",
    "overall_satisfaction": "Overall satisfaction with the experience",
    "recommend_academic_training": "Recommendation for academic training",
}


PROFESSIONAL_LABELS = {
    "clinical_pattern_accuracy": "ECG simulation reflects real clinical patterns",
    "formative_evaluation": "Supports effective formative evaluation",
    "visual_dynamic_representation": "Visual and dynamic representation is adequate",
    "clinical_workflow_alignment": "Design aligns with clinical workflow",
    "integration_medical_training": "Potential integration into medical programmes",
    "physiological_parameter_customization": "Parameter customisation for different scenarios",
    "consistency_real_cases": "Results are consistent with expected real cases",
    "research_specialized_training": "Useful for research or specialised training",
    "overall_usability": "Overall system usability is satisfactory",
    "recommend_professional_advanced_teaching": (
        "Recommendation for professional or advanced teaching"
    ),
}


@dataclass(frozen=True)
class DatasetConfig:
    key: str
    display_name: str
    filename: str
    labels: dict[str, str]


DATASETS = (
    DatasetConfig(
        key="students",
        display_name="Medical students",
        filename="students_anonymized.csv",
        labels=STUDENT_LABELS,
    ),
    DatasetConfig(
        key="healthcare_professionals",
        display_name="Healthcare professionals",
        filename="healthcare_professionals_anonymized.csv",
        labels=PROFESSIONAL_LABELS,
    ),
)


def parse_args() -> argparse.Namespace:
    repository_root = Path(__file__).resolve().parents[1]

    parser = argparse.ArgumentParser(
        description="Generate descriptive statistics and figures from the study datasets."
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=repository_root / "data",
        help="Directory containing the two anonymised CSV files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repository_root / "analysis" / "results",
        help="Directory in which the analysis outputs will be created.",
    )
    return parser.parse_args()


def load_and_validate_dataset(
    csv_path: Path,
    config: DatasetConfig,
) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {csv_path}\n"
            "Confirm that the CSV files are stored in the repository's data/ directory."
        )

    dataframe = pd.read_csv(csv_path, encoding="utf-8-sig")

    required_columns = [ID_COLUMN, *config.labels.keys(), FEEDBACK_COLUMN]
    missing_columns = [column for column in required_columns if column not in dataframe.columns]

    if missing_columns:
        raise ValueError(
            f"{csv_path.name} is missing required columns: "
            + ", ".join(missing_columns)
        )

    if dataframe[ID_COLUMN].isna().any():
        raise ValueError(f"{csv_path.name} contains missing participant identifiers.")

    if dataframe[ID_COLUMN].duplicated().any():
        duplicated = dataframe.loc[
            dataframe[ID_COLUMN].duplicated(), ID_COLUMN
        ].astype(str).tolist()
        raise ValueError(
            f"{csv_path.name} contains duplicated participant identifiers: {duplicated}"
        )

    for column in config.labels:
        original = dataframe[column]
        numeric = pd.to_numeric(original, errors="coerce")

        invalid_mask = original.notna() & numeric.isna()
        if invalid_mask.any():
            bad_values = sorted(original.loc[invalid_mask].astype(str).unique())
            raise ValueError(
                f"Column '{column}' in {csv_path.name} contains non-numeric values: "
                f"{bad_values}"
            )

        out_of_range = numeric.notna() & ~numeric.isin(LIKERT_VALUES)
        if out_of_range.any():
            bad_values = sorted(numeric.loc[out_of_range].unique().tolist())
            raise ValueError(
                f"Column '{column}' in {csv_path.name} contains values outside 1–5: "
                f"{bad_values}"
            )

        dataframe[column] = numeric.astype("Int64")

    dataframe[FEEDBACK_COLUMN] = dataframe[FEEDBACK_COLUMN].fillna("").astype(str).str.strip()
    return dataframe[required_columns].copy()


def calculate_descriptive_statistics(
    dataframe: pd.DataFrame,
    config: DatasetConfig,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    for variable, label in config.labels.items():
        values = dataframe[variable].dropna().astype(float)
        valid_n = int(values.count())
        missing_n = int(dataframe[variable].isna().sum())

        if valid_n == 0:
            mean = sd = median = q1 = q3 = iqr = minimum = maximum = np.nan
            favourable_n = 0
            favourable_percent = np.nan
        else:
            mean = float(values.mean())
            sd = float(values.std(ddof=1)) if valid_n > 1 else np.nan
            median = float(values.median())
            q1 = float(values.quantile(0.25))
            q3 = float(values.quantile(0.75))
            iqr = q3 - q1
            minimum = float(values.min())
            maximum = float(values.max())
            favourable_n = int((values >= 4).sum())
            favourable_percent = float(favourable_n / valid_n * 100)

        rows.append(
            {
                "variable": variable,
                "criterion": label,
                "valid_n": valid_n,
                "missing_n": missing_n,
                "mean": mean,
                "sd": sd,
                "median": median,
                "q1": q1,
                "q3": q3,
                "iqr": iqr,
                "minimum": minimum,
                "maximum": maximum,
                "favourable_n": favourable_n,
                "favourable_percent": favourable_percent,
            }
        )

    return pd.DataFrame(rows)


def calculate_response_frequencies(
    dataframe: pd.DataFrame,
    config: DatasetConfig,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []

    for variable, label in config.labels.items():
        values = dataframe[variable].dropna().astype(int)
        valid_n = int(values.count())

        for response in LIKERT_VALUES:
            count = int((values == response).sum())
            percentage = float(count / valid_n * 100) if valid_n else np.nan

            rows.append(
                {
                    "variable": variable,
                    "criterion": label,
                    "response": response,
                    "count": count,
                    "percentage": percentage,
                }
            )

    return pd.DataFrame(rows)


def export_feedback(
    dataframe: pd.DataFrame,
    output_path: Path,
) -> int:
    feedback = dataframe.loc[
        dataframe[FEEDBACK_COLUMN].ne(""),
        [ID_COLUMN, FEEDBACK_COLUMN],
    ].copy()
    feedback.to_csv(output_path, index=False, encoding="utf-8")
    return len(feedback)


def save_horizontal_chart(
    statistics: pd.DataFrame,
    value_column: str,
    x_label: str,
    title: str,
    output_path: Path,
    x_min: float,
    x_max: float,
    error_column: str | None = None,
) -> None:
    plot_data = statistics.iloc[::-1].copy()
    values = plot_data[value_column].to_numpy(dtype=float)
    labels = plot_data["criterion"].tolist()

    figure_height = max(5.5, len(labels) * 0.58)
    fig, ax = plt.subplots(figsize=(11, figure_height))

    if error_column is None:
        ax.barh(labels, values)
    else:
        errors = plot_data[error_column].fillna(0).to_numpy(dtype=float)
        ax.barh(labels, values, xerr=errors, capsize=3)

    ax.set_xlim(x_min, x_max)
    ax.set_xlabel(x_label)
    ax.set_title(title)
    ax.grid(axis="x", alpha=0.25)

    offset = (x_max - x_min) * 0.01
    for index, value in enumerate(values):
        if np.isnan(value):
            continue
        suffix = "%" if value_column == "favourable_percent" else ""
        label = f"{value:.1f}{suffix}"
        ax.text(min(value + offset, x_max), index, label, va="center", fontsize=9)

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def save_likert_distribution_chart(
    frequencies: pd.DataFrame,
    config: DatasetConfig,
    output_path: Path,
) -> None:
    pivot = frequencies.pivot(
        index="criterion",
        columns="response",
        values="percentage",
    ).fillna(0)

    ordered_labels = list(config.labels.values())
    pivot = pivot.reindex(ordered_labels).iloc[::-1]

    figure_height = max(5.5, len(pivot.index) * 0.6)
    fig, ax = plt.subplots(figsize=(12, figure_height))

    left = np.zeros(len(pivot))
    for response in LIKERT_VALUES:
        values = pivot[response].to_numpy(dtype=float)
        ax.barh(pivot.index, values, left=left, label=str(response))
        left += values

    ax.set_xlim(0, 100)
    ax.set_xlabel("Percentage of valid responses")
    ax.set_title(f"{config.display_name}: Likert response distribution")
    ax.legend(
        title="Likert response",
        ncols=5,
        loc="lower center",
        bbox_to_anchor=(0.5, -0.18),
    )

    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def format_number(value: object, digits: int = 2) -> str:
    if pd.isna(value):
        return "NA"
    return f"{float(value):.{digits}f}"


def build_markdown_report(
    analyses: list[dict[str, object]],
    output_path: Path,
) -> None:
    lines = [
        "# Descriptive Analysis Report",
        "",
        "This report was generated automatically from the anonymised questionnaire data.",
        "",
        "## Methods",
        "",
        "For every Likert item, the analysis reports the number of valid and missing "
        "responses, mean, sample standard deviation, median, first and third quartiles, "
        "interquartile range, minimum, maximum, and the frequency and percentage of "
        "responses rated 4 or 5. Response frequencies for all five scale points are "
        "available in the accompanying CSV files.",
        "",
    ]

    for item in analyses:
        config: DatasetConfig = item["config"]  # type: ignore[assignment]
        statistics: pd.DataFrame = item["statistics"]  # type: ignore[assignment]
        participant_n: int = item["participant_n"]  # type: ignore[assignment]
        feedback_n: int = item["feedback_n"]  # type: ignore[assignment]

        lines.extend(
            [
                f"## {config.display_name}",
                "",
                f"- Participants: **{participant_n}**",
                f"- Non-empty open-ended responses: **{feedback_n}**",
                "",
                "| Criterion | Valid n | Mean | SD | Median | IQR | Min–max | % ≥ 4 |",
                "|---|---:|---:|---:|---:|---:|---:|---:|",
            ]
        )

        for _, row in statistics.iterrows():
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(row["criterion"]),
                        str(int(row["valid_n"])),
                        format_number(row["mean"]),
                        format_number(row["sd"]),
                        format_number(row["median"]),
                        format_number(row["iqr"]),
                        f"{format_number(row['minimum'], 0)}–{format_number(row['maximum'], 0)}",
                        format_number(row["favourable_percent"], 1),
                    ]
                )
                + " |"
            )

        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()
    data_dir = args.data_dir.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    completed_analyses: list[dict[str, object]] = []
    combined_statistics: list[pd.DataFrame] = []

    for config in DATASETS:
        csv_path = data_dir / config.filename
        dataframe = load_and_validate_dataset(csv_path, config)

        statistics = calculate_descriptive_statistics(dataframe, config)
        frequencies = calculate_response_frequencies(dataframe, config)

        statistics_output = output_dir / f"{config.key}_descriptive_statistics.csv"
        frequencies_output = output_dir / f"{config.key}_response_frequencies.csv"
        feedback_output = output_dir / f"{config.key}_feedback.csv"

        statistics.to_csv(
            statistics_output,
            index=False,
            encoding="utf-8",
            float_format="%.3f",
        )
        frequencies.to_csv(
            frequencies_output,
            index=False,
            encoding="utf-8",
            float_format="%.3f",
        )
        feedback_n = export_feedback(dataframe, feedback_output)

        save_horizontal_chart(
            statistics=statistics,
            value_column="mean",
            error_column="sd",
            x_label="Mean Likert score (error bars: SD)",
            title=f"{config.display_name}: mean questionnaire scores",
            output_path=output_dir / f"{config.key}_mean_scores.png",
            x_min=1,
            x_max=5,
        )
        save_horizontal_chart(
            statistics=statistics,
            value_column="favourable_percent",
            error_column=None,
            x_label="Responses rated 4 or 5 (%)",
            title=f"{config.display_name}: favourable responses",
            output_path=output_dir / f"{config.key}_favourable_responses.png",
            x_min=0,
            x_max=100,
        )
        save_likert_distribution_chart(
            frequencies=frequencies,
            config=config,
            output_path=output_dir / f"{config.key}_likert_distribution.png",
        )

        statistics_with_group = statistics.copy()
        statistics_with_group.insert(0, "group", config.display_name)
        combined_statistics.append(statistics_with_group)

        completed_analyses.append(
            {
                "config": config,
                "statistics": statistics,
                "participant_n": len(dataframe),
                "feedback_n": feedback_n,
            }
        )

        print(
            f"Processed {config.display_name}: "
            f"{len(dataframe)} participants, {feedback_n} open-ended responses."
        )

    pd.concat(combined_statistics, ignore_index=True).to_csv(
        output_dir / "combined_descriptive_statistics.csv",
        index=False,
        encoding="utf-8",
        float_format="%.3f",
    )

    build_markdown_report(
        completed_analyses,
        output_dir / "descriptive_analysis_report.md",
    )

    print(f"Analysis completed. Results saved to: {output_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
