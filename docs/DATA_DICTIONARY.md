# Data dictionary

## Dataset 01 — material comparison

| Field | Meaning | Unit |
|---|---|---|
| material | ion-exchange material | — |
| analyte | activity category / radionuclide | — |
| initial_activity_bq_ml | activity before treatment | Bq/mL |
| final_activity_bq_ml | activity after treatment | Bq/mL |
| remaining_activity_pct | final / initial × 100 | % |
| kd_ml_g | distribution coefficient | mL/g |
| equilibration_time_h | batch contact time | h |
| sample_volume_ml | LLW volume | mL |
| material_mass_g | media mass | g |

## Dataset 05 / 06 — column studies

`bed_volumes` is cumulative bed volumes processed. DF fields are decontamination
factors reported in the thesis. Activity fields are outlet activity values.

## Dataset 07 — fluidisation

Velocities are superficial velocities. Bed-volume rates are the corresponding
normalized rates reported in Table 4.1.

## Dataset 08 — cement waste product

`leach_rate_g_cm2_day` and `cumulative_fraction_leached` reproduce Table 4.2.
