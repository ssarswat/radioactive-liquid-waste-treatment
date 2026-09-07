"""Reusable analysis helpers."""

import pandas as pd


def rank_materials_by_kd(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.sort_values(["analyte", "kd_ml_g"], ascending=[True, False])
          [["analyte", "material", "kd_ml_g", "remaining_activity_pct"]]
          .reset_index(drop=True)
    )


def best_material_by_analyte(df: pd.DataFrame) -> pd.DataFrame:
    idx = df.groupby("analyte")["kd_ml_g"].idxmax()
    out = df.loc[idx, ["analyte", "material", "kd_ml_g", "remaining_activity_pct"]].copy()
    out["removal_efficiency_pct"] = 100 - out["remaining_activity_pct"]
    return out.sort_values("analyte").reset_index(drop=True)
