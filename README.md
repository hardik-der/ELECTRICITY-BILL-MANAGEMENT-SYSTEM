The Smart Electricity Billing System is a modular software application engineered in Python to automate energy
consumption calculations, dynamic progressive tariff evaluation, surcharge accounting, and structured bill
generation. Designed for multi-use environments including residential households, student dormitories, and
commercial units, the system enforces meter validation rules to eliminate negative consumption errors and outdated
manual ledger entries. It is used to calculate the bill for the household , school ,etc..    

The following are the step to create an Smart Electricity Billing System :-
# STEP 1 - BASIC_INPUT.PY : Takes the customer name , previous reading , and current reading as input.
# STEP 2 - METER_READING.PY : Calculate the electricity units consumed ( UNITS  = CURRENT READING - PREVIOUS READING ).
# STEP 3 - VALIDATION.PY : Checks whether the meter readings are valid and prevents incorrect input.
# STEP 4 - TARRIF.PY : Applies different electricity rates according to the number of units consumed.
# STEP 5 - CALCULATOR.PY : Calculates the energy charge , fixed charge , and tax to find the total bill.
# STEP 6 - BILL.PY : Displays the customer's electricity bill in a clean and readable format .
# STEP 7 - FINAL.PY : Combines all previous step or module into one complete smart electricity bill calculator.
