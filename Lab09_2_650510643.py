#!/usr/bin/env python3
# ศศิวัสส์ แสงแก้ว พงษ์
# 650510643
# Lab09_1
# 204111 Sec 002

def main():
    n=int(input())
    s=input()
    if s=='':
        s=' '
    square_frame(n,s)

def square_frame(n, s):
    list_n=list(range(1,(n*3)+(n-3)))
    pad=len(str(list_n[-1]))
    if pad>1:
        list_n=list(map(lambda x,y=pad: '0'*(y-len(str(x)))+str(x), list_n))
    else:list_n=list(map(str, list_n))
    up=list_n[0:n]
    sidel=list_n[-1-(n-2)+1:]
    sidel.reverse()
    sider=list_n[n:(2*n)-2]
    side=list(zip(sidel,sider))
    down=list_n[n+(n-2):-(n-2)]
    down.reverse() 
    print(s.join(up))
    print_side(side,s[0]*(len(s.join(up))-(len(up[0])*2)))
    print(s.join(down))
    
def print_side(x,y):
    if not x:
        return ''
    else:
        print(y.join(x[0]))
        return print_side(x[1:],y)

if __name__ == '__main__':
    main()
