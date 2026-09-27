# =========================================
# METER READING
# =========================================

name = "Rahul Sharma"

previous_reading = 1250
current_reading = 1495

units = current_reading - previous_reading

print("=" * 45)
print("       SMART ELECTRICITY BILL")
print("=" * 45)

print()
print("Customer Name    :", name)
print("Previous Reading :", previous_reading)
print("Current Reading  :", current_reading)
print("Units Consumed   :", units)