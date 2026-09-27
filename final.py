# =========================================
# FINAL ELECTRICITY BILL SYSTEM
# =========================================

from calculator import calculate_energy_charge
from bill import display_bill


# =========================================
# CUSTOMER DATA
# =========================================

name = "Rahul Sharma"

previous_reading = 1250

current_reading = 1495


# =========================================
# VALIDATION
# =========================================

if current_reading < previous_reading:

    print("ERROR!")
    print("Current reading cannot be less")
    print("than previous reading.")

else:

    # Calculate units

    units = current_reading - previous_reading


    # Calculate energy charge

    energy_charge = calculate_energy_charge(units)


    # Fixed charge

    fixed_charge = 100


    # Subtotal

    subtotal = energy_charge + fixed_charge


    # Tax

    tax = subtotal * 0.05


    # Final bill

    total_bill = subtotal + tax


    # Display final bill

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