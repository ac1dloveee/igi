from functools import reduce
import input_sequence as inpseq

def find_index_of_maximum(nums: list[float]) -> int:
    """
    Finds the index of the maximum value in a list of numbers.

    Args:
        nums (list[float]): The list of numbers.

    Returns:
        int: The index of the maximum value in the list.
    """
    
    return 1 + nums.index(max(nums))

def multiplication_of_elements_between_zeroes(nums: list[float]) -> float:
    """
    Finds the multiplication of elements between zeroes in a list of numbers.

    Args:
        nums (list[float]): The list of numbers.

    Raises:
        ValueError: If the list does not contain any zeroes.
        ValueError: If the list contains only one zero.

    Returns:
        float: The multiplication of elements between zeroes in the list.
    """

    if not 0.0 in nums:
        raise ValueError("List does not contain any zeroes.")
    
    if nums.index(0.0) == len(nums) - 1 - nums[::-1].index(0.0):
        raise ValueError("List contains only one zero.")

    # Reduce the list of numbers between first and last
    # zero in input list to their multiplication.
    return reduce(lambda x, y: x * y, 
                  [num for num in nums
                   [nums.index(0.0) + 1 : len(nums) - 1 - nums[::-1].index(0.0)]],
                   1.0)

def execute():
    """
    Execute the fifth task. Prints results to console.
    """
    print("Task 5.")
    print("Finds index of maximum number.")
    print("Finds multiplication of numbers between zeroes.")

    numbers = inpseq.default_input(float)

    print(f"Your numbers: { numbers }")
    print()
    
    print(f"Index of maximum is { find_index_of_maximum(numbers) }")
    try:
        print(f"Multiplication of elements between zeroes is { multiplication_of_elements_between_zeroes(numbers) }.")
    except ValueError as e:
        print(e)
    print()