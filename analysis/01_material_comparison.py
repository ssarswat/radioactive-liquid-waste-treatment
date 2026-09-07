from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed" / "dataset_01_material_comparison.csv"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

df = pd.read_csv(DATA)

ranking = (
    df.sort_values(["analyte", "kd_ml_g"], ascending=[True, False])
      [["analyte", "material", "kd_ml_g", "remaining_activity_pct"]]
)
print(ranking.to_string(index=False))

ax = df.pivot(index="material", columns="analyte", values="kd_ml_g").plot(kind="bar")
ax.set_ylabel("Kd (mL/g)")
ax.set_title("Distribution coefficient by material and analyte")
plt.tight_layout()
plt.savefig(FIG / "material_kd_comparison.png", dpi=180)
plt.close()
