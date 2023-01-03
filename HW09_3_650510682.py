#!/usr/bin/env python3
# วาเนสซ่า ฟิลลิปส์ ฉี
# 650510682
# HW09_3
# 204111 Sec 003


def main():

 #n = int(input())
 num = int(input())
 #print(three_digits_to_word(n))
 print(num_to_word(num)) 

def three_digits_to_word(n,res= ""):
    # if n < 0 or n > 999: 

    #  res =' ' 

    if n > 0 and n <= 999:
        ch = n //100
        hi = n % 10
        ij = n //10
        jk = ij % 10
        km = n % 100


        low_twenty = ["zero","one", "two", "three", "four", "five",
 "six", "seven", "eight", "nine", "ten",
 "eleven", "twelve", "thirteen", "fourteen", "fifteen",
 "sixteen", "seventeen", "eighteen", "nineteen"]
        low_hundred = ["","ten", "tweenty", "thirty", "fourty", "fifty", "sixty", 'seventy', "eighty", "ninty"]
        hd = "hundred"


        #กรณีที่เลขน้อยกว่า20
        if n < 20:
            res = low_twenty[n]
            return res
        #กรณีที่เป็นเลขหลักสิบที่หาร10ลงตัวเช่น 20 30
        elif n <100 and n % 10 == 0:
            res = low_hundred[ij] 
            return res   
        #กรณีที่เป็นเลขหลักสิบและหาร10ไม่ลงตัว เช่น 21 35
        elif n < 100 and n%10 != 0:
             res = low_hundred[ij] +(str('-'))+low_twenty[hi]
             return res
        #กรณีที่เป็นเลขจำนวนเต็มร้อยเช่น 100 200 300
        elif n >= 100 and n %100 ==0:
            res = low_twenty[ch]+(str(" "))+hd 
            return res 
        #กรณีที่เป็นเลข 111 ถึง 119      
        elif n > 100 and km <= 19:
            res = low_twenty[ch]+(str(" "))+hd+ (str(" "))+low_twenty[km]
            return res  
        #กรณีที่เป็นเลขเช่น 120 130 220 340   
        elif n > 100 and km > 19 and km % 10 == 0:
            res = low_twenty[ch]+(str(" "))+hd+(str(" "))+low_hundred[jk]
            return res 

        #กรณีเลขที่มากกว่า100ทั่วไป เช่น 678 248 156
        else:
            res = low_twenty[ch]+(str(" "))+hd+(str(" "))+low_hundred[jk]+(str("-"))+low_twenty[hi]    
            return res
    else:
        pass        

def num_to_word(num):  
    x = num
    ans = ""
    if num <= 999:
        return three_digits_to_word(num) 
    if x//pow(10,9)>0:
        ans =  three_digits_to_word(x//pow(10,9))+" billion"  ##add billion digit
        x = x%pow(10,9)
    if x//pow(10,6)>0:
        ans = ans+" "+three_digits_to_word(x//pow(10,6))+" million" ##add million digit
        x = x%pow(10,6)
    if x//pow(10,3)>0:
        ans = ans+" "+three_digits_to_word(x//pow(10,3))+" thousand" ##add thousand digit
        x = x%pow(10,3)
    if x<1000:
        ans+= " "+three_digits_to_word(x) ##add hundred digit
        
    if ans[0]==" ":
        ans = ans[1:] ##if ans has white space in fornt 
        
    if ans[-4::] == "zero":
        ans = ans[0:len(ans)-5] ##if ans has "zero" in back    
    return ans
        










if __name__ == '__main__':
    main()