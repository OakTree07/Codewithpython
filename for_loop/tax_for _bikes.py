# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
#Cost price (in Rs)                                       Tax
 #       > 100000                                                  15 %
#      > 50000 and <= 100000                          10%
#        <= 50000                                                  5%
bike_price=int(input("Enter the price of the bike."))
if bike_price>100000:
    tax=bike_price*15/100
    print("The amount is",tax)
elif bike_price>50000 and bike_price<=100000:
    tax=bike_price*10/100
    print("The cost of the bike is ",tax)
elif bike_price<=50000:
    tax=bike_price*5/100
    print("The price of thebike is ",tax)
else:
    print("NO TAX APPLIED.")
