def is_perfect_number(num):
    sum = 1
    if(num <= 0):
        return False
    else:
        for divisor in range(2,num):
            if num % divisor == 0:
                sum = sum + divisor
        if sum == num:
            return True
        else:
            return False

input_data = int(input("Please enter a number to check for Perfect number! \n"))
print("Is number a perfect number :- " + str(is_perfect_number(input_data)))