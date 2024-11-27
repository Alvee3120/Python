bd = ["singara", "somusa", "puri", "ruti"]
italian = ["pizza", "burger"]
chinese = ["egg role", "fried rice", "chicker curry"]

dish = input("enter a dish name : ")

if dish in bd :
    print("this is bd dish")

elif dish in italian :
    print(" this is italian dish")

elif dish in chinese :
    print ("this is chinese dish")

else:
    print("I dont know : hehe<(")