# Data layer

`processed/` contains transcribed or derived datasets from the 2016 M.Tech thesis.

## Source mapping

- `dataset_01_material_comparison.csv` → Tables 3.1–3.2
- `dataset_02_temperature_kd.csv` → Tables 3.4–3.5
- `dataset_03_ph_kd.csv` → Tables 3.6–3.7
- `dataset_04_tds_kd.csv` → Table 3.8
- `dataset_05_series_columns.csv` → Table 3.9
- `dataset_06_parallel_columns.csv` → Table 3.10
- `dataset_07_fluidization.csv` → Table 4.1
- `dataset_08_leach_rate.csv` → Table 4.2
- `engineering_summary.csv` → selected engineering observations from Chapters 3–5

## Important note on Dataset 03

The pH tables in the PDF have a complex multi-column layout. The numeric sequence is
preserved as source values rather than being silently reinterpreted. Before using
Dataset 03 for a quantitative model, visually verify the column mapping against the
original thesis page.
