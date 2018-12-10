# FizzBuzz! | By Tredon Austin
# Implementation of FizzBuzz by me. Seemed like a fun side project to do
# really quickly (especially with my Mathematics background).

index = 1
while index != 101:
    if index % 15 == 0:
        print("FizzBuzz")
    elif index % 5 == 0:
        print("Buzz")
    elif index % 3 == 0:
        print("Fizz")
    else:
        print(str(index))
    index += 1