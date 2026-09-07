from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

parallel = pd.read_csv(ROOT / "data/processed/dataset_06_parallel_columns.csv")

ax = parallel.plot(
    x="bed_volumes",
    y=["gross_beta_4a_bq_ml", "gross_beta_13x_bq_ml"],
    marker="o",
    figsize=(8, 5),
)
ax.axhline(3.7, linestyle="--", linewidth=1)
ax.set_xlabel("Cumulative bed volumes")
ax.set_ylabel("Gross beta activity (Bq/mL)")
ax.set_title("Parallel column performance")
plt.tight_layout()
plt.savefig(FIG / "parallel_gross_beta_breakthrough.png", dpi=180)
plt.close()

ax = parallel.plot(
    x="bed_volumes",
    y=["df_gross_4a", "df_gross_13x"],
    figsize=(8, 5),
)
ax.set_xlabel("Cumulative bed volumes")
ax.set_ylabel("Decontamination factor")
ax.set_title("Parallel column decontamination factor")
plt.tight_layout()
plt.savefig(FIG / "parallel_df.png", dpi=180)
plt.close()
