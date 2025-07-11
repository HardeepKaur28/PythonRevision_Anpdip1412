print("------------------------------------------------------------")
print("                               PAYSLIP                       ")
print("-------------------------------------------------------------")
input("Enter Name : ")
basic = float(input("Enter Basic Salary : "))
print("-------------------------------------------------------------")

da = basic * 0.05
ta = basic * 0.06
hra = basic * 0.12
pf = basic * 0.15

total_sal = basic+da+ta+hra+pf
net_sal = total_sal-pf

print(f"DA : {da}")
print(f"TA : {ta}")
print(f"HRA : {hra}")
print(f"PF : {pf}")
print(f"TOTAL SALARY : {total_sal}")

print("---------------------------------------------------------------")
print(f"NET SALARY : {net_sal}")
print("---------------------------------------------------------------")