"""
pipeline_config.py
──────────────────
Shared configuration for 002_create_custom_dataset and 004_batch_inference_evaluate.
Import this file in both notebooks:

    import sys; sys.path.insert(0, str(BASE_DIR))
    from pipeline_config import *
"""


# ── FLATTEN SEPARATOR ────────────────────────────────────────────────────────
# Separator used when flattening nested dicts.
# "_" → front_holder_first_name  (used in 002 for training labels)
# "." → front.holder.first_name  (used in 004 for evaluation display)
FLATTEN_SEP_TRAIN: str = "_"
FLATTEN_SEP_EVAL:  str = "_"   # match training — no dot notation in eval


# ── CARDHOLDERS FLATTEN CONFIG ────────────────────────────────────────────────
# Max number of cardholders to expand into individual flat fields.
MAX_CARDHOLDERS: int = 5

# Fields to extract per cardholder
CARDHOLDER_FIELDS: list[str] = [
    "position", "first_name", "middle_initial", "last_name", "full_name"
]


# ── EVALUATION CONFIG ────────────────────────────────────────────────────────
# Fields excluded from evaluation (too noisy or irrelevant)
EXCLUDED_FIELDS: set[str] = {
    "back_barcode_number",   # synthetic placeholder — not a real barcode
}

# Fields that look like dates but must NOT be normalised (raw format preserved)
DATE_NORMALIZE_EXCLUDE: set[str] = {
    "front_dob_watermark",
    "dob_watermark",
}

# Null percentage threshold: fields where GT is empty > this % → MISSING_GROUND_TRUTH
NULL_PCT_THRESHOLD: int = 70

# String length threshold: mean length > this → LONG_TEXT, else SHORT_TEXT
LENGTH_MEAN_THRESHOLD: int = 50

