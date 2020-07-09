#Fibonacci Generator

def get_nth_term():
    while True:    
        try:
            nth_term = int(input("Enter the nth term: "))
            if(nth_term < 0):
                negativeNumberError = ValueError("nth term should be positive: " + str(nth_term))
                raise negativeNumberError
            break
        except ValueError as ve:
            print(ve)
    return nth_term

#Recursive Fibonnaci:
def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return get_fibonacci(n-1) + get_fibonacci(n-2)

print("Result: " + str(get_fibonacci(get_nth_term())) )



# print(my_nth_term)