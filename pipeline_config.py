"""
pipeline_config.py
──────────────────
Centralized configuration file acting as a standardization bridge between two stages:
- Training dataset creation (002_create_custom_dataset.ipynb)
- Post-inference evaluation (004_batch_inference_evaluate.ipynb)

Objective: Ensure absolute consistency in key structures and data processing logic.
"""

# ── FLATTEN SEPARATOR ────────────────────────────────────────────────────────
# The separator used when flattening nested JSON structures into a list of parallel key-value pairs.
# FLATTEN_SEP_TRAIN: "_" → front_holder_first_name (used in 002 for training labels).
# FLATTEN_SEP_EVAL: "_"  → Forces the evaluation phase (004) to use the same underscore separator, eliminating false evaluation errors caused by separator discrepancies (e.g., legacy code using a dot ".").
FLATTEN_SEP_TRAIN: str = "_"
FLATTEN_SEP_EVAL:  str = "_"


# ── CARDHOLDERS FLATTEN CONFIG ────────────────────────────────────────────────
# Defines how the system extracts the dynamic array of Medicare cards into fixed keys for scoring purposes.

# Fixes the maximum number of members on a single card to 5. The system limits scanning to the 5th person.
MAX_CARDHOLDERS: int = 5

# The list of 5 sub-fields to be extracted for each person (creating keys such as cardholders_1_first_name, cardholders_1_middle_initial).
CARDHOLDER_FIELDS: list[str] = [
    "position", "first_name", "middle_initial", "last_name", "full_name"
]


# ── EVALUATION CONFIG ────────────────────────────────────────────────────────
# Defines exception rules to prevent the metric system from inaccurately evaluating the model's performance.

# Excludes noisy fields from the final evaluation report.
# "back_barcode_number": Excluded because it is a synthetic placeholder string in the generated dataset. Using Exact Match evaluation on this string would inaccurately lower the overall score.
EXCLUDED_FIELDS: set[str] = {
    "back_barcode_number",
}

# Blocks the Date Normalization feature from converting special fields to the standard ISO YYYY-MM-DD format.
# Watermark fields require preserving the raw, continuous block format (e.g., 09092004) for exact match comparisons.
DATE_NORMALIZE_EXCLUDE: set[str] = {
    "front_dob_watermark",
    "dob_watermark",
}

# Thresholds for Feature Categorization.
# If a data field contains empty (null) values in more than 70% of the test samples, it is categorized as MISSING_GROUND_TRUTH and may be excluded from the evaluation charts.
NULL_PCT_THRESHOLD: int = 70

# If the average length of data in a field exceeds 50 characters, it is categorized as LONG_TEXT and evaluated using the ROUGE metric.
# If the average length is 50 characters or less, it is categorized as SHORT_TEXT and evaluated using Exact Match/CER metrics.
LENGTH_MEAN_THRESHOLD: int = 50