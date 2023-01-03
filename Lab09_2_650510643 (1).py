def main():
    sep=''
    square_frame(10,sep)

def print_side(x,y):
    if not x:
        return ''
    else:
        print(y.join(x[0]))
        return print_side(x[1:],y)

def square_frame(n, sep=' '):
    list_n=list(range(1,(n*3)+(n-3)))
    pad = len(str(list_n[-1]))
    if pad > 1:
        list_n = list(map(lambda x,y=pad: '0'*(y-len(str(x)))+str(x), list_n))
    else:
        list_n = list(map(str, list_n))
    up = list_n[0:n]
    sidel = list_n[-1-(n-2)+1:]
    sidel.reverse()
    sider = list_n[n:(2*n)-2]
    side = list(zip(sidel,sider))
    down = list_n[n+(n-2):-(n-2)]
    down.reverse() 
    print(sep.join(up))
    print_side(side,sep[0]*(len(sep.join(up))-(len(up[0])*2)))
    print(sep.join(down))


if __name__ == '__main__':
    main()
