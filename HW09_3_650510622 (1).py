#!/usr/bin/env python3
# นันทพา อดิเรกธรรมากร 
# 650510622
# HW09_3
# 204111 Sec 002

def main():
    n = int(input())
    print(num_to_word(n))

def three_digits_to_word(n):
    units = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if 0 <= n <= 19:
        return (units[n])
    elif n<100:
        return  tens[n// 10]+'-'+units[int(n% 10)] 
    elif n<1000:
        return units[n// 100]  +"hundred " + three_digits_to_word(int(n % 100))

def num_to_word(num):
    first = three_digits_to_word(num)
    if num < 1000:
        return first
    else:
        if num<1000000: 
           return  num_to_word(num // 1000) + "thousand " + num_to_word(int(num % 1000))
        elif num < 1000000000:    
           return num_to_word(num // 1000000) + "million " + num_to_word(int(num % 1000000))
        elif num < 100000000000:
            return num_to_word(num//1000000000) + "billion " + num_to_word(int(num %1000000000))
       
        


if __name__ == '__main__':
    main()