def matrix_mult(m1,m2):
    result = [] 
    for i in range(len(m1)):
        row = [] 
        for j in range(len(m2[0])):
            product = 0 
            for v in range(len(m1[i])):
                 product += m1[i][v] * m2[v][j]
            row.append(product) 

        result.append(row) 
    return result

    
def main():
    print(matrix_mult([[1, 2, 3]], [[7, 8],[9, 10],[11,12]]))

if __name__ =="__main__":
    main()
