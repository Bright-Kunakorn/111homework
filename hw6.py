def matrix_mult(m1, m2):
    result = [[sum(a * b for a, b in zip(A_row, B_col))
                        for B_col in zip(*m2)]
                                for A_row in m1]
    return result
