#!/usr/bin/env python3
# ศศิวัสส์ แสงแก้ว พงษ์
# 650510643
# HW09_2
# 204111 Sec 002


def main():
    pc_list=[(1,0)]
    v='z'
    print(print_polynomial(pc_list, v))

def print_polynomial(pc_list, v):
    a=sorted(pc_list, key=lambda power: power[0], reverse=True)
    ans=list(map(polynomial, a))
    result=sumstr(ans)
    result=str(result).strip()
    result=str(result).replace('x',v)
    if result[0]=='-':
        result=result.lstrip(' -')
        return '-'+result
    else:
        result=result.lstrip(' +')
        return result

def samesam(n):
    print(n)

def sumstr(n):
    if not n:
        return ''
    else: return n[0]+sumstr(n[1:])

def polynomial(n):
    n=list(n)
    p=n[0]
    s=n[1]
    if p==0:
        if s==0:
            return ''
        elif s>0:
            return ' + '+str(abs(s))
        else: return ' - '+str(abs(s))
    elif p==1:
        if s==0:
            return ''
        elif s>0:
            return ' + '+str(abs(s))+'x'
        else: return ' - '+str(abs(s))+'x'
    else: 
        if s==0:
            return ''
        elif s>0:
            return ' + '+str(abs(s))+'x^'+str(p)
        else: return ' - '+str(abs(s))+'x^'+str(p)

    
if __name__ == '__main__':
    main()