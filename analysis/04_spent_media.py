from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

fluid = pd.read_csv(ROOT / "data/processed/dataset_07_fluidization.csv")
leach = pd.read_csv(ROOT / "data/processed/dataset_08_leach_rate.csv")

print(fluid.to_string(index=False))

ax = leach.plot(x="days", y="leach_rate_g_cm2_day", marker="o", figsize=(8, 5))
ax.set_ylabel("Leach rate (g/cm² day)")
ax.set_title("Cement waste product leach-rate history")
plt.tight_layout()
plt.savefig(FIG / "leach_rate.png", dpi=180)
plt.close()
