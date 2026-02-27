expense = 0
expense_list = []
print("\t\tExepense-Tracker-V1 \n")
while expense != -999:
    expense = float(input("Enter the expense (-999 to stop adding expenses): "))
    if expense != -999:
        expense_list.append(expense)
expense = 0
for i in expense_list:
    expense = expense + i

print("\n\nTotal expense is:",expense)