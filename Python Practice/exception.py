a = input("Enter a number : ")3
b = input("Enter another number : ")

try :
    z = int(a)/ int(b)

except Exception as e :
    print ("Exception Occured : ", e)
    z= None

print("Divition is : ", z)