def fizz_buzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num

while True:
    num_input = input("Enter a number (or 'q' to quit): ")
    if num_input.lower() == 'q':
        break
    try:
        num = int(num_input)
        print(fizz_buzz(num))
    except ValueError:
        print("Please enter a valid integer or 'q' to quit.")

fizz_buzz()