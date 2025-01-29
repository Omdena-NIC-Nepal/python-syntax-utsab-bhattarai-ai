def format_string(name, age):
    return(f"My name is {name} and I am {age} years old")
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    pass

def conditional_check(number):
    if number > 10:
        return("Greater")
    elif number < 10:
        return("Lesser")
    else:
        return("Equal")
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    pass

def loop_sum(n):
    for i in range(1,n+1):
        sum=i+sum
        return(sum)
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    pass

def list_operations(numbers):
    for i in numbers:
        sum = sum + i

    return(tuple(sum, max(numbers), min(numbers)))
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    pass

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    pass

def set_operations(list1, list2):
    return intersection(list1, list2)
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    pass

def arithmetic_ops(a, b):
    print("Sum:", a+b)
    print("difference:", a-b)
    print("product:", a*b)
    print("quotient:", a/b)
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    pass

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    pass

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    pass