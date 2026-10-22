def energy_kwh(power_watts, hours):
    """Energy used by a device of `power_watts` running for `hours`, in kWh."""
    return power_watts * hours / 1000


if __name__ == "__main__":
    print("A 2000 W kettle running for 0.1 hours uses", energy_kwh(2000, 0.1), "kWh")
