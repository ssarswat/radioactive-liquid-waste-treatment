from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

ph = pd.read_csv(ROOT / "data/processed/dataset_03_ph_kd.csv")
tds = pd.read_csv(ROOT / "data/processed/dataset_04_tds_kd.csv")

# The thesis PDF contains a visually complex pH table. The repository preserves
# its numeric fields and flags them for manual verification rather than silently
# imposing a new interpretation.
print("pH dataset columns:", list(ph.columns))
print("\nTDS dataset:")
print(tds.to_string(index=False))

ax = tds.plot(x="tds_ppm", y=["kd_4a_ml_g", "kd_13x_cfc_ml_g"], marker="o")
ax.set_ylabel("Kd (mL/g)")
ax.set_title("TDS versus Kd")
plt.tight_layout()
plt.savefig(FIG / "tds_vs_kd.png", dpi=180)
plt.close()
