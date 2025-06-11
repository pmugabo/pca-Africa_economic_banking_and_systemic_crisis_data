class MatrixDimensionError(Exception):
    """Custom error for invalid matrix multiplication."""
    pass


def multiply_matrices(A, B):
    # Validate that both inputs are lists of lists
    if not (isinstance(A, list) and isinstance(B, list)):
        raise MatrixDimensionError("Sorry, Group 5 can't allow this: Inputs must be lists.")
    