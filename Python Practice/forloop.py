exp = [100,200,300,400,5500,600]

total = 0

for i in range (len(exp)):
    print(" Month: ",(i+1), "Expense: ", exp[i])
    total = total + exp[i]

print("Total : ", total)