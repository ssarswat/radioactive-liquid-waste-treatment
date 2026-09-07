import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rwlt.metrics import (
    distribution_coefficient,
    remaining_activity_pct,
    decontamination_factor,
    pressure_drop_kozeny_carman,
)


def test_kd_matches_thesis_material_example():
    assert math.isclose(distribution_coefficient(146, 26.10, 20, 1), 91.88, rel_tol=1e-3)


def test_remaining_activity():
    assert math.isclose(remaining_activity_pct(68, 0.4), 0.588235, rel_tol=1e-5)


def test_df():
    assert math.isclose(decontamination_factor(20.7, 0.69), 30.0, rel_tol=1e-3)


def test_pressure_drop_example():
    dp = pressure_drop_kozeny_carman(
        mu_pa_s=1.002e-3,
        length_m=1.0,
        sphericity=1.0,
        particle_diameter_m=0.0005,
        porosity=0.3,
        superficial_velocity_m_s=0.0006,
    )
    assert dp > 0
