# 1(a) Program to calculate EB Bill
prev = int(input("Enter previous month reading : "))
curr = int(input("Enter present month reading : "))
units = curr - prev
if units <= 100:
    amttopay = 0
    print("You have consumed less electricity. No amount to pay for this month")
elif units > 100 and units <= 200:
    amttopay = (units - 100) * 0.8
elif units > 200 and units <= 300:
    amttopay = (units - 200) * 1 + 80
elif units > 300 and units <= 400:
    amttopay = (units - 300) * 1.5 + 100 + 80
else:
    amttopay = (units - 400) * 2 + 150 + 100 + 80
print("You have consumed ", units, " units")
print("Your Electricity Bill for this month : ", amttopay)
