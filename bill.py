# =========================================
# BILL DISPLAY
# =========================================


def display_bill(
    name,
    previous_reading,
    current_reading,
    units,
    energy_charge,
    fixed_charge,
    tax,
    total_bill
):

    print()
    print("=" * 45)
    print("           ELECTRICITY BILL")
    print("=" * 45)

    print("Customer Name    :", name)
    print("Previous Reading :", previous_reading)
    print("Current Reading  :", current_reading)
    print("Units Consumed   :", units)

    print("-" * 45)

    print(f"Energy Charge    : ₹{energy_charge:.2f}")
    print(f"Fixed Charge     : ₹{fixed_charge:.2f}")
    print(f"Tax              : ₹{tax:.2f}")

    print("-" * 45)

    print(f"TOTAL BILL       : ₹{total_bill:.2f}")

    print("=" * 45)


# =========================================
# SAMPLE DATA
# =========================================

name = "Rahul Sharma"

previous_reading = 1250
current_reading = 1495

units = current_reading - previous_reading

energy_charge = 1115

fixed_charge = 100

subtotal = energy_charge + fixed_charge

tax = subtotal * 0.05

total_bill = subtotal + tax


# =========================================
# DISPLAY BILL
# =========================================

display_bill(
    name,
    previous_reading,
    current_reading,
    units,
    energy_charge,
    fixed_charge,
    tax,
    total_bill
)