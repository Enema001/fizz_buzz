

for Num in range(1,101):                        # For loop used to define the range 1-100
    print(Num)                                  # Prints the number in the range


    if Num % 3 == 0 and Num % 5 == 0:           # if statement used to check the conditions for multiples of 3 and 5 (%15)
        print('FizzBuzz')
        continue

    elif Num % 3 == 0:                          # Checking for multiples of 3
        print('Fizz')
        continue

    elif Num % 5 == 0:                          # Check for Multiples of 5
        print('Buzz')
        continue

    elif all(Num%i!=0 for i in range(2,Num)):   # Checking for prime numbers
               print(Num, 'is a prime number')

    else:
        print(Num)                              # 

