
def main():
    #pc_list = [(2, -6), (0, -8), (1, 34)]
    #pc_list = [(0,2),(1,1)]
    #pc_list = [(0,0),(0,0)]
    pc_list = [(2,0),(0,1)]
    #pc_list = [(2,0),(0,1),(0,2),(7,8)]
    #pc_list = [(100, 1), (4, 2), (1, 34),(12,3)]
    v = ("s")
    
    print(print_polynomial(pc_list,v))
    #print(check_pd(pc_list,i=0))
    # print(help_me(pc_list,v))


def help_me(final,v):
    #a =list(map(str,pc_list))
    #str_1 =' '.join(map(str,a))
    str_2 = final

    #print(final)
    #a = sorted(pc_list[i])
    #print(final)
    
    poly = []
    power, coefficient, sym = str_2
    #print(str_2)
    
    if coefficient == 0:
        poly.append(" ")
        # poly.append("{} ".format(power))
    elif power == 0:
        poly.append(" {} {}".format(sym,abs(coefficient)))
            
    elif power == 1:
        if coefficient == 1:
            poly.append(" {} {}".format(sym,v))
        else:
            poly.append(" {} {}{}".format(sym,abs(coefficient),v))      
    else:
        string = " {} {}{}".format(sym,coefficient,v) + "^{}".format(power)
        poly.append(string)
        

    return ' '.join(map(str,poly))


#สร้างฟังก์ชันเพื่อเช็คเครื่องหมายสัมประสิทธิ์
def check_pd(pc_list):
    if pc_list[1] >= 0:
        return "+"
    else:
        return "-" 



def print_polynomial(pc_list,v):
    a = sorted(pc_list,reverse=True)
    sym = list(map(check_pd,a))
    pow, coe = zip(*a)
    first = list(list(zip(pow,coe,sym))[0])
    #print(first)
    if first[1] == 1 and first[0] != 1:
        first[1] = ""
        res = str(first[1])+(str(v))+(str('^'))+(str(first[0]))

    elif first[1] == 0:
        first[1] = "" 
        res = " "

    elif first[0] == 1:
        first[0] = ""
        res = str(v)        
    else:
        res = str(first[1])+(str(v))+(str("^"))+(str(first[0]))


    
    #print((res))
    final = list(zip(pow,coe,sym))[1:]

    if len(final)==1 and res == " ":
        
        final = list(zip(pow,coe,sym))[1:]
        
    else:
        final = list(zip(pow,coe,sym))[1:]
        

    # print(final)
    #print(len(final))
  

    res_1 = list(map(lambda x:help_me(x, v), final))

    res_2 = ''.join(map(str,res_1))
    

    return   res+res_2







if __name__ == '__main__':
    main() 