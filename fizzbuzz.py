def fizzbuzz():
    icount = 1
    while icount <= 100:
        if icount % 3 == 0 and icount % 5 == 0:
            print("Fizzbuzz")
        elif icount % 3 == 0:
            print("Fizz")
        elif icount % 5 == 0:
            print("Buzz")
        else:
            print(icount) 
        icount = icount + 1

fizzbuzz()