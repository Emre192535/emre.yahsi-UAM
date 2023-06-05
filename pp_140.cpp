/*
Exercise 140, file pp_140.py

Variables are defined below:

sum = 3000
counter = 0

We want to divide sum by counter.

Use the try... except... clause to handle a division by zero exception.
If the division is done correctly, print the result to the console. At the time of error, let the following text be printed to the console: "You can't  divide by 0!"
*/

#include <iostream>
#include <stdexcept>

template <typename T>
float divide_to_float(const T &num, const T &denominator);

int main()
{
    const int sum = 3000;
    const int counter = 0;

    try {
        std::cout << divide_to_float(sum, counter) << '\n';
    }
    catch (std::overflow_error &e) {
        std::cout << e.what() << '\n';
    }
    return 0;
}

template <typename T>
float divide_to_float(const T &num, const T &denominator)
{
    // You need to check it yourself and throw an exception.
    // Integer divide by zero is not an exception in standard C++.
    if (denominator == 0) {
        throw std::overflow_error("You can't divide by 0!");
    }
    return static_cast<float>(num) / denominator;
}
