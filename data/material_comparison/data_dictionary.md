# Dataset 01 — Data Dictionary

## Overview

This document defines the variables, units, provenance and interpretation rules for Dataset 01 — Material Comparison.

The dataset contains comparative batch-experiment results for four ion-exchange materials evaluated for treatment of low-level radioactive liquid waste.

## Variables

| Field | Type | Unit | Description | Provenance |
|---|---|---|---|---|
| `material` | string | — | Ion-exchange material used in the batch experiment | Source |
| `analyte` | string | — | Activity category or radionuclide measured | Source |
| `initial_activity_bq_ml` | float | Bq/mL | Initial activity of the LLW before treatment | Source |
| `final_activity_bq_ml` | float | Bq/mL | Activity measured after equilibration with the material | Source |
| `remaining_activity_pct` | float | % | Fraction of initial activity remaining after treatment | Derived |
| `kd_ml_g` | float | mL/g | Distribution coefficient reported by the source | Source |
| `equilibration_time_h` | integer | h | Batch contact/equilibration time | Source |
| `sample_volume_ml` | integer | mL | LLW volume used in the batch experiment | Source |
| `material_mass_g` | integer | g | Mass of ion-exchange material used | Source |
| `source_table` | string | — | Source-table reference for traceability | Metadata |

## Material Values

The `material` field contains:

- `4A`
- `13X-CFC`
- `HMO-PU`
- `CFC-PU`

## Analyte Values

The `analyte` field contains:

- `Gross beta-gamma`
- `90Sr`
- `137Cs`
- `99Tc`

## Experimental Conditions

The batch experiments used:

| Parameter | Value | Unit |
|---|---:|---|
| Material mass | 1 | g |
| LLW volume | 20 | mL |
| Equilibration time | 6 | h |
| Feed pH | 8.20 | — |
| Feed TDS | 452 | ppm |

## Distribution Coefficient

The source defines the distribution coefficient as:

\[
K_d = \frac{I-F}{F}\times\frac{V}{m}
\]

where:

- `I` = initial activity
- `F` = final activity
- `V` = LLW volume
- `m` = ion-exchange material mass

The resulting unit is **mL/g**.

The `kd_ml_g` field contains the value reported in the source table.

## Derived Variables

### `remaining_activity_pct`

Calculated as:

```text
remaining_activity_pct =
    final_activity_bq_ml / initial_activity_bq_ml × 100
