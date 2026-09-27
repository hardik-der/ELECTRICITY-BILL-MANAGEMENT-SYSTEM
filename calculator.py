# =========================================
# CALCULATOR MODULE
# =========================================


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


# =========================================
# SAMPLE DATA
# =========================================

name = "Rahul Sharma"

previous_reading = 1250
current_reading = 1495

units = current_reading - previous_reading

energy_charge = calculate_energy_charge(units)


# =========================================
# OUTPUT
# =========================================

print("=" * 45)
print("       ELECTRICITY CALCULATOR")
print("=" * 45)

print()
print("Customer Name :", name)
print("Previous Reading:", previous_reading)
print("Current Reading :", current_reading)
print("Units Consumed  :", units)

print()
print("Energy Charge   : ₹", energy_charge)