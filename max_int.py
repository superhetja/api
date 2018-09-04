# User inputs numbers repeatedly until a negative value is entered.


num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
while num_int > 0 :
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))  
# gerist eitthvað?


print("The maximum is", max_int)    # Do not change this line

#breytingar