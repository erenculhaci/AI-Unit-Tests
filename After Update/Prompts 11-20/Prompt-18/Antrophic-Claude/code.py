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
    
    # Validate operators
    valid_operators = {'+', '-', '*', '//', '**'}
    for op in operator:
        if op not in valid_operators:
            raise ValueError(f"Unsupported operator: {op}")
    
    # Apply the first operation to the first two operands
    result = operand[0]
    
    # Apply each subsequent operation using the result of previous operations
    # This creates a nested evaluation, like ((((a op1 b) op2 c) op3 d)...)
    for i in range(len(operator)):
        op = operator[i]
        if op == '+':
            result += operand[i+1]
        elif op == '-':
            result -= operand[i+1]
        elif op == '*':
            result *= operand[i+1]
        elif op == '//':
            if operand[i+1] == 0:
                raise ZeroDivisionError("Division by zero")
            result //= operand[i+1]
        elif op == '**':
            result **= operand[i+1]
    
    return result