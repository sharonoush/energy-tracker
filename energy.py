def energy_kwh(power_watts, hours):
    """Energy used by a device of `power_watts` running for `hours`, in kWh."""
    return power_watts * hours / 1000


def cost_eur(kwh, price_per_kwh=0.35):
    """Cost of `kwh` of electricity, in euros."""
    return kwh * price_per_kwh


# name: (average power in watts, hours used per day)
APPLIANCES = {
    "fridge": (40, 24),
    "laptop": (60, 6),
    "kettle": (2000, 0.2),
    "washing machine": (500, 1),
}


def daily_report(price_per_kwh=0.35):
    """Print the daily energy use and cost of every appliance."""
    total_kwh = 0
    for name, (watts, hours) in APPLIANCES.items():
        kwh = energy_kwh(watts, hours)
        total_kwh += kwh
        print(f"{name:16} {kwh:5.2f} kWh/day   {cost_eur(kwh, price_per_kwh):5.2f} EUR/day")
    print(f"{'TOTAL':16} {total_kwh:5.2f} kWh/day   {cost_eur(total_kwh, price_per_kwh):5.2f} EUR/day")


if __name__ == "__main__":
    daily_report()
