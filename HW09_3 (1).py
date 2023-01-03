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
    x = n
    units = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n==0:
        return "zero"
    if n>99:
        ans = ans+units[x//100]+" hundred" 
        if x%100 > 19:
            ans = ans+" "+tens[(x%100)//10] 
            
            if x%10!=0:
                ans =ans+"-"+units[(x%100)%10]  
        else:
            ans = ans+" "+units[x%100] 
            
    else:
        if x > 19:
            ans = ans+tens[x//10]
            
            if x%10!=0:
                ans =ans+"-"+units[x%10]  
        else:
            ans = ans+units[x] 
    return ans

def num_to_word(num):
    x = num
    ans = ""
    if num <= 999:
        return three_digits_to_word(num) 
    if x//pow(10,9)>0:
        ans =  three_digits_to_word(x//pow(10,9))+" billion" 
        x = x%pow(10,9)
    if x//pow(10,6)>0:
        ans = ans+" "+three_digits_to_word(x//pow(10,6))+" million" 
        x = x%pow(10,6)
    if x//pow(10,3)>0:
        ans = ans+" "+three_digits_to_word(x//pow(10,3))+" thousand" 
        x = x%pow(10,3)
    if x<1000:
        ans+= " "+three_digits_to_word(x)  
    if ans[0]==" ":
        ans = ans[1:]   
    if ans[-4::] == "zero":
        ans = ans[0:len(ans)-5] 
    return ans

if __name__ == '__main__':
    main()