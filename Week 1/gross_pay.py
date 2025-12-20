hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly pay rate: "))

gross_pay = hours_worked * hourly_rate
print(f"\nGross pay: ${gross_pay:.2f}")

def calculate_tax(income):
    tax = 0.0

    if income <= 15600:
        tax += 0.105 * income
        return tax
    else:
        tax += 0.105 * 15600

    if income <= 53500:
        tax += 0.175 * (income - 15600)
        return tax
    else:
        tax += 0.175 * (53500 - 15600)

    if income <= 78100:
        tax += 0.30 * (income - 53500)
        return tax
    else:
        tax += 0.30 * (78100 - 53500)

    if income <= 180000:
        tax += 0.33 * (income - 78100)
        return tax
    else:
        tax += 0.33 * (180000 - 78100)

    tax += 0.39 * (income - 180000)
    return tax

tax_amount = calculate_tax(gross_pay)
net_pay = gross_pay - tax_amount

print(f"Tax deducted: ${tax_amount:.2f}")
print(f"Final income (net pay): ${net_pay:.2f}")
