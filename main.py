import csv

def check_loan_eligibility():
    print("---- Loan Eligibility Checker ----")

name=input("Enter your name: ")
age=int(input("Enter your age: ")) 
income=float(input("Enter your monthly income (in INR): "))
credit_score=int(input("Enter your credit score (300-850): "))
loan_amount=float(input("Enter the desired loan amount (INR): "))
existing_EMI=float(input("Enter your existing debts (in INR): "))
employment_status=input("Enter your employment status (employed/self-employed/unemployed): ").lower()

eligible = True
reason = ""

#eligibility conditions
if age < 21 or age > 60:
    eligible = False
    reason += "Age must be between 21 and 60. "
elif income < 25000:
    eligible = False
    reason += " income should be at least INR 20,000. "
elif credit_score < 650:
    eligible = False
    reason += "Credit score must be at least 650. "
elif loan_amount > income * 20:
    eligible = False
    reason += "Loan amount exceeds 20 times your monthly income. "
elif existing_EMI > income * 0.4:
    eligible = False
    reason += "Existing debts exceed 40% of your monthly income. "
elif employment_status not in ['employed', 'self-employed']:
    eligible = False
    reason += "Employment status must be 'employed' or 'self-employed'. "

print("\n---- Eligibility Result ----")
if eligible:
    print(f"Congratulations {name}, you are eligible for the loan!")
else:
    print(f"Sorry {name}, you are not eligible for the loan.")
    print("Reason(s):", reason)

# Save to CSV
with open('loan_eligibility.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, age, income, credit_score, loan_amount, existing_EMI, employment_status, "Eligible" if eligible else "Not Eligible", reason])

