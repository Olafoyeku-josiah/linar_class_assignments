print("hello.")
monthly_salary=int(input(" Enter your monthly salary: "))
childs_fees=int(input(" Enter your child's fees: "))
if monthly_salary> 20000 and childs_fees<=20000:
    print("dear user, you can settle your child's fee.")
elif monthly_salary==20000 and childs_fees>20000:
    print("Dear user, you can pay an installment fee.")
elif monthly_salary==20000 and childs_fees==20000:
    print("you can still settle the fee but other expenses are left out.")
else:
    print("you can loan the remaining amount and settle the fees.")
print("thank you.")