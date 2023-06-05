/*
Exercise 150, file pp_150.py (on the basis of exercise 100)
Write a program that computes the value of n factorial - n!
Use iterative implementation
Expected results
0! = 1
1! = 1
2! = 1 * 2 = 2
3! = 1 * 2 * 3 = 6
4! = 1 * 2 * 3 * 4
10! = 3628800
32! = 263130836933693530167218012160000000
n! = 1 * 2 * 3 * .... * n

In order to do it implement the function
def factorial(n: int) -> int:

Improve error handling using exceptions
*/

#include <iostream>
#include <stdexcept>

template <typename T>
T factorial(const T &n);

int main()
{
    long long result;
    for (long long i = -2; i < 15; ++i) {
        try {
            result = factorial(i);  // if put directly in cout, then numeric limits of int (?) are reached
            std::cout << "Factorial of '" << i << "' is '" << result << "'.\n";
        }
        catch (const std::invalid_argument &e) {
            std::cerr << "Skipping '" << i << "', due to error: " << e.what() << '\n';
        }
    }
    return 0;
}

template <typename T>
T factorial(const T &n)
{
    /*
     * Functions calculates the factorial of n
     *
     * Parameters:
     * n: number, positive int
     * Returns:
     * The factorial
     *
     */
    if (n < 0) {
        throw std::invalid_argument("Non-positive numbers are not supported.");
    }
    if (n <= 1) {
        return 1;
    }
    else {
        T f = 1;
        for (T i = 1; i < n + 1; ++i) {
            f *= i;
        }
        return f;
    }
}
