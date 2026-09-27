# =========================================
# ELECTRICITY TARIFF
# =========================================

name = "Rahul Sharma"

previous_reading = 1250
current_reading = 1495

units = current_reading - previous_reading


def calculate_energy_charge(units):

    if units <= 100:

        charge = units * 3

    elif units <= 200:

        charge = (
            (100 * 3)
            + ((units - 100) * 5)
        )

    elif units <= 300:

        charge = (
            (100 * 3)
            + (100 * 5)
            + ((units - 200) * 7)
        )

    else:

        charge = (
            (100 * 3)
            + (100 * 5)
            + (100 * 7)
            + ((units - 300) * 9)
        )

    return charge


energy_charge = calculate_energy_charge(units)


print("=" * 45)
print("       ELECTRICITY TARIFF")
print("=" * 45)

print()
print("Customer Name :", name)
print("Units Used    :", units)

print()
print("Tariff:")
print("0 - 100 units   : ₹3/unit")
print("101 - 200 units : ₹5/unit")
print("201 - 300 units : ₹7/unit")
print("Above 300       : ₹9/unit")

print()
print("Energy Charge   : ₹", energy_charge)