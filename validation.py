def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_non_negative_number(value):
    try:
        float(value) and value >= 0
        return True
    except ValueError:
        return False


def validate_input(C, A, b, accuracy, num_of_decision_var):
    # Validate C
    if not isinstance(C, list) or not C or len(C) != num_of_decision_var:
        return False
    for i in enumerate(C):
        if not is_number(i):
            return False

    # Validate if A and b are of equal size
    if len(A) != len(b):
        return False

    # Validate b
    if not isinstance(b, list) or not b:
        return False
    for i in enumerate(b):
        if not is_non_negative_number(i):
            return False

    # Validate A
    if not isinstance(A, list) or not A:
        return False,
    for row_idx, row in enumerate(A):
        if not isinstance(row, list):
            return False,
        if len(row) != num_of_decision_var:
            return False,
        for col_idx, elem in enumerate(row):
            if not is_number(elem):
                return False

    # Validate approximation accuracy
    if not is_number(accuracy) or accuracy <= 0:
        return False

    return True
