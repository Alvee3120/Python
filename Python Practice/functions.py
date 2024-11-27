def cal_total (arr):
    total = 0
    for i in arr:
        total+=i
    return total


a = [12,34,354,56,45,334]
b= [12,34,56,34,65,34,654]

a_total = cal_total(a)
b_total = cal_total(b)

print(" a total = ", a_total)
print("b total = ", b_total)


def sum (p,q):
    total = p+q
    return total

x= 5
y= 3

total_of_X_Y = sum(x,y)

print(total_of_X_Y)