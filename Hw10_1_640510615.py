#!/usr/bin/env python3
# Tassin Ongsakul(dossdy)
# 640510615
# Hw10_1
# 204111 Sec 001

def main():
    x = common_prime_factor(180,48 ,True)
    print('- - - - - - - -')
    print(x)

def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(factors)
 
def common_prime_factor(a,b,show_list=False):
    r = a%b
    count = 0
    while r !=0:
        a=b 
        b=r
        r=a%b
        if show_list == True:#โชว์วิธีืทำ
            if count == 0:
                print ('a:',prime_factor(a))
                count+=1
            else:
                print ('b:',prime_factor(a))
        elif show_list == False:
            pass
    return prime_factor(b)

if __name__ == '__main__':
    main()






