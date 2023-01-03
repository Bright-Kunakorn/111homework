#!/usr/bin/env python3
# นันทพา อดิเรกธรรมากร 
# 650510622
# HW09_3
# 204111 Sec 002

def main():
    n = int(input())
    print(num_to_word(n))

def three_digits_to_word(n):
    ans = ""
    units = ["","one","two","three","four","five","sinum","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sinumteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sinumty","seventy","eighty","ninety"]
    if n==0:
        return "zero"
    if n>99:
        ans = ans+units[n//100]+" hundred" 
        if n%100 > 19:
            ans = ans+" "+tens[(n%100)//10] 
            if n%10!=0:
                ans =ans+"-"+units[(n%100)%10]  
        else:
            ans = ans+" "+units[n%100] 
    else:
        if n > 19:
            ans = ans+tens[n//10]
            
            if n%10!=0:
                ans =ans+"-"+units[n%10]  
        else:
            ans = ans+units[n] 
    return ans

def num_to_word(n):
    ans = ""
    if n <= 999:
        return three_digits_to_word(n) 
    if n//pow(10,9)>0:
        ans =  three_digits_to_word(n//pow(10,9))+" billion" 
        n = n%pow(10,9)
    if n//pow(10,6)>0:
        ans = ans+" "+three_digits_to_word(n//pow(10,6))+" million" 
        n = n%pow(10,6)
    if n//pow(10,3)>0:
        ans = ans+" "+three_digits_to_word(n//pow(10,3))+" thousand" 
        n = n%pow(10,3)
    if n<1000:
        ans+= " "+three_digits_to_word(n)  
    if ans[0]==" ":
        ans = ans[1:]   
    if ans[-4::] == "zero":
        ans = ans[0:len(ans)-5] 
    return ans

if __name__ == '__main__':
    main()