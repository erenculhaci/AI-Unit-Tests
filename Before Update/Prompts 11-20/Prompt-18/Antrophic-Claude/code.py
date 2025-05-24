# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # Validate input
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list must be one element shorter than operand list")
    
    if len(operator) < 1 or len(operand) < 2:
        raise ValueError("Must have at least one operator and two operands")
    
    # Start with the first operand
    result = operand[0]
    
    # Apply each operation in sequence
    for i in range(len(operator)):
        op = operator[i]
        if op == '+':
            result += operand[i+1]
        elif op == '-':
            result -= operand[i+1]
        elif op == '*':
            result *= operand[i+1]
        elif op == '//':
            result //= operand[i+1]
        elif op == '**':
            result **= operand[i+1]
        else:
            raise ValueError(f"Unsupported operator: {op}")
    
    return result