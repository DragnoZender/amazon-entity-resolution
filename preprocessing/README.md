# Amazon Business Entity Resolution — Preprocessing

This module implements the **data preprocessing and normalization pipeline** for the Amazon Business Entity Resolution Challenge.

The goal of preprocessing is to reduce superficial differences between business records while preserving the original information required by downstream **blocking, feature engineering, and matching** stages.

---

## Overview

The challenge contains three independent business data sources:

- **Source 1** — deduplicated reference entities
- **Source 2** — noisy business records
- **Source 3** — noisy business records

Each source contains:

- `entity_id`
- `business_name`
- `business_address`
- `country`

The preprocessing pipeline creates normalized versions of the business name and address while preserving the original columns.

### Pipeline

```text
Raw Data
   │
   ▼
Unicode Normalization
   │
   ▼
Case Normalization
   │
   ▼
Whitespace Normalization
   │
   ▼
Punctuation Normalization
   │
   ├──────────────────────┐
   ▼                      ▼
Business Name         Business Address
Normalization         Normalization
   │                      │
   ├── Legal suffixes     └── Address abbreviations
   │
   ▼
Normalized Dataset


# Preprocessing Module

This module contains the preprocessing and normalization functions for the
Amazon Business Entity Resolution project.

The purpose of this module is to normalize business names and addresses before
they are used by the blocking and feature-engineering stages.

---

## 1. What this module provides

The module provides four functions:

```python
normalize_text()
normalize_business_name()
normalize_business_address()
preprocess_dataframe()



## 2. How to import

```
from preprocessing import (
    normalize_text,
    normalize_business_name,
    normalize_business_address,
    preprocess_dataframe
)
```