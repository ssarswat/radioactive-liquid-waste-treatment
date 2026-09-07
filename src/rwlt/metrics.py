"""Core calculations used in the LLW analysis repository."""

import pandas as pd


def distribution_coefficient(initial_activity: float, final_activity: float,
                             volume_ml: float, mass_g: float) -> float:
    """Calculate Kd using the equation defined in the thesis."""
    if final_activity <= 0 or volume_ml <= 0 or mass_g <= 0:
        raise ValueError("final_activity, volume_ml and mass_g must be > 0")
    return ((initial_activity - final_activity) / final_activity) * (volume_ml / mass_g)


def remaining_activity_pct(initial_activity: float, final_activity: float) -> float:
    if initial_activity <= 0:
        raise ValueError("initial_activity must be > 0")
    return final_activity / initial_activity * 100.0


def removal_efficiency_pct(initial_activity: float, final_activity: float) -> float:
    return 100.0 - remaining_activity_pct(initial_activity, final_activity)


def decontamination_factor(feed_activity: float, effluent_activity: float) -> float:
    if feed_activity <= 0 or effluent_activity <= 0:
        raise ValueError("activities must be > 0")
    return feed_activity / effluent_activity


def pressure_drop_kozeny_carman(mu_pa_s: float, length_m: float,
                                sphericity: float, particle_diameter_m: float,
                                porosity: float, superficial_velocity_m_s: float) -> float:
    """Kozeny–Carman pressure drop per packed-bed length, Pa."""
    if not (0 < porosity < 1):
        raise ValueError("porosity must lie between 0 and 1")
    return (
        180 * mu_pa_s * length_m
        / (sphericity ** 2 * particle_diameter_m ** 2)
        * ((1 - porosity) ** 2 / porosity ** 3)
        * superficial_velocity_m_s
    )
