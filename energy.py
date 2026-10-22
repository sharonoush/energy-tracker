def energy_kwh(power_watts, hours):
    """Energy used by a device of `power_watts` running for `hours`, in kWh."""
    return power_watts * hours / 1000


def cost_eur(kwh, price_per_kwh=0.35):
    """Cost of `kwh` of electricity, in euros."""
    return kwh * price_per_kwh


if __name__ == "__main__":
    kwh = energy_kwh(2000, 0.1)
    print("A 2000 W kettle running for 0.1 hours uses", kwh, "kWh")
    print("That costs about", round(cost_eur(kwh), 3), "euros")
