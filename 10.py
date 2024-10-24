
#  Checker for Even or Odd Numbers
2
def check_even_odd(number):
    if number % 2 == 0:
        return "The number {number} is even."
    else:
        return "The number {number} is odd."

def main():
    user_input = int(input("Please enter a number: "))
    result = check_even_odd(user_input)
    print(result)

if __name__ == "__main__":
    main()

