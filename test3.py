def main():
    list_x = [[2, 3, 4],
[1, 2]]
    square_matrix(list_x)

    for i in list_x:
        print(str(i))
    print(list_x)
   
def square_matrix(list_x):
    each_row = []
    for i in list_x: # หาความยาว row ที่มากที่สุด
        each_row += [len(i)]

    len_row = max(each_row)  # หาความยาว row ที่มากที่สุด
    len_column = len(list_x)
    z = [0]
   
    for j in range(len_column): # เติม 0 ให้แต่ละ row เท่ากัน
        if len_row >= len_column: # เติม 0 ตาม max row
            if len(list_x[0])<len_row: 
                count_z = len_row - len(list_x[0])
                a = list_x.pop(0)
                list_x.append(a + z*(count_z))
                continue
            if len(list_x[0]) >= len_row:
                a = list_x.pop(0)
                list_x.append(a)
                continue
        else: #เติม 0 ตาม ความยาวของ column
            count_z = len_column - len(list_x[0])
            a = list_x.pop(0)
            list_x.append(a + z*(count_z))

    count_c = len_row - len_column
    for k in range(count_c): # เติม [0] ให้ column = ความยาวมากสุดของrow
        if len_row > len_column:
            list_x.append(z*(len_row))


if __name__=='__main__':
    main()