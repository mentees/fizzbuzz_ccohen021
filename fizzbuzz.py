def fizzbuzz(user_input):
    for i in range(1, user_input + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)        

def main(): 
    # input (and validate)
    while True:
        # validate: only number
        while True:
            try:
                limit = int(input("Enter a number to which you wish to count: "))
                break
            except ValueError:
                print("Value must be a number. Please try again.")

        # validate: value
        if limit < 0 or limit > 1000:
            print("Value out of range. (0 < Number < 1000)")
        else:
            break  

    # process and output      
    fizzbuzz(limit)

main()