# =========================================
# METER READING VALIDATION
# =========================================

name = "Rahul Sharma"

previous_reading = 1250
current_reading = 1495

print("=" * 45)
print("       SMART ELECTRICITY BILL")
print("=" * 45)

print()
print("Customer Name    :", name)
print("Previous Reading :", previous_reading)
print("Current Reading  :", current_reading)

# Check whether the reading is valid

if current_reading < previous_reading:

    print()
    print("ERROR!")
    print("Current reading cannot be less")
    print("than previous reading.")

else:

    units = current_reading - previous_reading

    print()
    print("Reading is VALID")
    print("Units Consumed:", units)