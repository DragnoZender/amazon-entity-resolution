
import re
import unicodedata
import pandas as pd


# ============================================================
# Basic text normalization
# ============================================================

def normalize_text(text):
    """
    Basic normalization for business names and addresses.
    Does not translate, correct spelling, or add information.
    """

    if pd.isna(text):
        return ""

    text = str(text)

    # Unicode normalization
    text = unicodedata.normalize("NFKC", text)

    # Lowercase
    text = text.lower()

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Normalize punctuation
    text = re.sub(r"[.,;:!?()\[\]{}]", " ", text)

    # Normalize hyphens and slashes
    text = re.sub(r"[-/]", " ", text)

    # Normalize whitespace again
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# Business name normalization
# ============================================================

LEGAL_SUFFIX_PATTERNS = {
    r"\bprivate limited\b": "pvt ltd",
    r"\bprivate ltd\b": "pvt ltd",
    r"\bpvt limited\b": "pvt ltd",
    r"\bpvt ltd\b": "pvt ltd",
    r"\bpvt\b": "pvt",
    r"\bincorporated\b": "inc",
    r"\bcorporation\b": "corp",
    r"\blimited liability company\b": "llc",
}


def normalize_business_name(text):
    """
    Normalize a business name using basic text normalization
    plus canonicalization of common legal suffix forms.
    """

    text = normalize_text(text)

    if not text:
        return ""

    for pattern, replacement in LEGAL_SUFFIX_PATTERNS.items():
        text = re.sub(pattern, replacement, text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# Address normalization
# ============================================================

ADDRESS_ABBREVIATIONS = {
    r"\broad\b": "rd",
    r"\bstreet\b": "st",
    r"\bavenue\b": "ave",
    r"\bboulevard\b": "blvd",
    r"\bdrive\b": "dr",
    r"\blane\b": "ln",
    r"\bcircle\b": "cir",
    r"\bhighway\b": "hwy",
    r"\bparkway\b": "pkwy",
    r"\bcourt\b": "ct",
    r"\bplace\b": "pl",
    r"\bterrace\b": "ter",
    r"\bbroadway\b": "bway",
}


def normalize_business_address(text):
    """
    Normalize a business address.

    Preserves numbers and multilingual text.
    Does not geocode, translate, or add missing information.
    """

    text = normalize_text(text)

    if not text:
        return ""

    for pattern, replacement in ADDRESS_ABBREVIATIONS.items():
        text = re.sub(pattern, replacement, text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


# ============================================================
# DataFrame preprocessing
# ============================================================

def preprocess_dataframe(df):
    """
    Add normalized business name and address columns
    while preserving the original columns.
    """

    df = df.copy()

    df["business_name_normalized"] = (
        df["business_name"].map(normalize_business_name)
    )

    df["business_address_normalized"] = (
        df["business_address"].map(normalize_business_address)
    )

    return df