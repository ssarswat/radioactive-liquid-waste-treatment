# Dataset 01 — Material Comparison

## Purpose

This dataset captures the comparative batch-experiment results for four ion-exchange materials evaluated for treatment of low-level radioactive liquid waste (LLW):

- Zeolite 4A
- 13X-CFC
- HMO-PU
- CFC-PU

The dataset contains initial and final activity measurements and distribution coefficients (Kd) for gross beta-gamma activity, ⁹⁰Sr, ¹³⁷Cs and ⁹⁹Tc.

## Experimental Basis

The source experiment used:

- **Material mass:** 1 g
- **LLW volume:** 20 mL
- **Equilibration time:** 6 h
- **Feed pH:** 8.20
- **Feed TDS:** 452 ppm

The experiment compared the ability of the four ion-exchange materials to remove radionuclides from the LLW under identical batch-contact conditions.

## Dataset Contents

The dataset contains the following variables:

| Variable | Description | Unit | Provenance |
|---|---|---|---|
| `material` | Ion-exchange material used | — | Source |
| `analyte` | Activity category or radionuclide | — | Source |
| `initial_activity_bq_ml` | Initial activity before treatment | Bq/mL | Source |
| `final_activity_bq_ml` | Activity after equilibration | Bq/mL | Source |
| `remaining_activity_pct` | Activity remaining after treatment | % | Derived |
| `kd_ml_g` | Distribution coefficient | mL/g | Source |
| `equilibration_time_h` | Batch contact time | h | Source |
| `sample_volume_ml` | LLW volume used | mL | Source |
| `material_mass_g` | Ion-exchange material mass | g | Source |
| `source_table` | Source-table reference | — | Metadata |

## Materials Evaluated

### Zeolite 4A

A synthetic zeolite evaluated as an ion-exchange medium for radionuclide removal.

### 13X-CFC

A modified zeolite evaluated for radionuclide uptake and subsequent column studies.

### HMO-PU

A hybrid inorganic-organic ion-exchange material evaluated in the batch experiments.

### CFC-PU

A hybrid ion-exchange material that demonstrated strong radionuclide uptake in the batch experiments.

## Radionuclides and Activity Measurements

The dataset includes measurements for:

- Gross beta-gamma activity
- ⁹⁰Sr
- ¹³⁷Cs
- ⁹⁹Tc

The initial and final activities are reproduced from the source experimental tables.

## Distribution Coefficient

The dissertation defines the distribution coefficient as:

\[
K_d = \frac{I-F}{F}\times\frac{V}{m}
\]

where:

- `I` = initial activity
- `F` = final activity
- `V` = volume of LLW
- `m` = mass of ion-exchange material

The resulting unit is **mL/g**.

The `kd_ml_g` values in this dataset are retained as reported in the source table.

## Derived Variable

The field `remaining_activity_pct` is calculated as:

```text
remaining_activity_pct =
    final_activity_bq_ml / initial_activity_bq_ml × 100
