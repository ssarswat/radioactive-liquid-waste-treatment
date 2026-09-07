import sys
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

st.set_page_config(page_title="Radioactive Liquid Waste Treatment Analytics", layout="wide")
st.title("Low-Level Radioactive Liquid Waste Treatment Analytics")
st.caption("Reproducible analysis of the 2016 M.Tech experimental dataset.")

data_path = ROOT / "data/processed/dataset_01_material_comparison.csv"
df = pd.read_csv(data_path)

st.subheader("Material comparison")
analyte = st.selectbox("Analyte", sorted(df["analyte"].unique()))
view = df[df["analyte"] == analyte].sort_values("kd_ml_g", ascending=False)

c1, c2, c3 = st.columns(3)
best = view.iloc[0]
c1.metric("Highest Kd", f"{best.kd_ml_g:,.2f} mL/g")
c2.metric("Best material", best.material)
c3.metric("Removal efficiency", f"{100-best.remaining_activity_pct:.2f}%")

st.dataframe(
    view[["material", "initial_activity_bq_ml", "final_activity_bq_ml",
          "remaining_activity_pct", "kd_ml_g"]].reset_index(drop=True),
    use_container_width=True,
)

st.bar_chart(view.set_index("material")["kd_ml_g"])

st.info(
    "The dashboard is an analytical representation of the thesis data. "
    "It is not intended for operational radioactive-waste treatment decisions."
)
