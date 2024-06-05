import math as mt
import input_service as inps

def f(x):
    """
    Calculates the natural logarithm of 1 - x.

    Args:
        x (float): The value for which the natural logarithm is to be calculated.

    Returns:
        float: The natural logarithm of 1 - x.
    """
    return mt.log(1 - x)


def evaluate(x, eps):
    """
    Prints a table with the values of x, n, F(x), the mathematical function F(x), and the desired accuracy eps.

    Args:
        x (float): Argument of the function.
        eps (float): The desired accuracy.

    Raises:
        ValueError: If the absolute value of x is greater or equal to 1.
        ValueError: If the value of eps is less or equal to 0.
    """
    print("Task 1.")
    print("Evaluate ln(1 - x), |x| < 1")

    if abs(x) >= 1:
        raise ValueError("Absolute value of 'x' must be less than 1")
    if eps <= 0:
        raise ValueError("The value of 'eps' must be greater than 0")

    print(f"x                 n           F(x)               Math F(x)          eps")

    n = 1
    step = -x
    result = -x
    math_result = f(x)

    for n in range(1, 501):
        # Calculates the next value of x using the Newton-Raphson method
        if abs(math_result - result) <= eps:
            return
        
        step *= x * n
        step /= n + 1
        result += step
        # Prints the values of x, n, F(x), Math F(x), and eps
        print(f"{'{:.5f}'.format(x)}           {n}           {'{:.5f}'.format(result)}           {'{:.5f}'.format(math_result)}           {'{:.8f}'.format(eps)}")


def execute():
    """
    Execute the first task. Print results to console.

    """

    print("Task 1.")
    print("Evaluate ln(1 - x).")

    x = inps.input_specified_type(
        float, "Enter value of 'x': ")
    eps = inps.input_specified_type(
        float, "Enter value of 'eps': ")

    try:
        evaluate(x, eps)
    except ValueError as e:
        print(e)