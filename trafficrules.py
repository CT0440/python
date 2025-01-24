# 1. A traffic police officer calculates fines based on the violation:
# • Crossing red light: ₹500.
# • Speeding: ₹1000.
# • No helmet: ₹300.
# Write a program to calculate the total fine based on user input

print("Select the violations committed:")
print("1. Crossing red light: ₹500")
print("2. Speeding: ₹1000")
print("3. No helmet: ₹300")
print("Enter the numbers corresponding to violations separated by commas (e.g., 1,2):")

violations = input("Enter your choice(s): ").split(',')

fine_1 = 500
fine_2 = 1000
fine_3 = 300

total_fine = 0

for violation in violations:
    violation = violation.strip()
    if violation == '1':
        total_fine += fine_1
    elif violation == '2':
        total_fine += fine_2
    elif violation == '3':
        total_fine += fine_3

print(f"Total fine: ₹{total_fine}")
