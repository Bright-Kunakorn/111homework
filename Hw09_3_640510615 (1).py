#!/usr/bin/env python3
# Tassin Ongsakul(dossdy)
# 640510615
# Hw09_3
# 204111 Sec 001
def main():
    for i in range(100000):
        print(num_to_word(i))

def three_digits_to_word(n):
    a = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen',   
        20 : 'twenty', 21 : 'twenty-one', 22 : 'twenty-two', 23 : 'twenty-three', 24 : 'twenty-four', 25 : 'twenty-five', 26 : 'twenty-six', 27 : 'twenty-seven', 28 : 'twenty-eight', 29 : 'twenty-nine',
        30 : 'thirty', 31 : 'thirty-one', 32 : 'thirty-two', 33 : 'thirty-three', 34 : 'thirty-four', 35 : 'thirty-five', 36 : 'thirty-six', 37 : 'thirty-seven', 38 : 'thirty-eight', 39 : 'thirty-nine',
        40 : 'forty', 41 : 'forty-one', 42 : 'forty-two', 43 : 'forty-three', 44 : 'forty-four', 45 : 'forty-five', 46 : 'forty-six', 47 : 'forty-seven', 48 : 'forty-eight', 49 : 'forty-nine',
        50 : 'fifty', 51 : 'fifty-one',	52 : 'fifty-two', 53 : 'fifty-three', 54 : 'fifty-four', 55 : 'fifty-five',	56 : 'fifty-six', 57 : 'fifty-seven', 58 : 'fifty-eight', 59 : 'fifty-nine',
        60 : 'sixty', 61 : 'sixty-one',	62 : 'sixty-two', 63 : 'sixty-three', 64 : 'sixty-four', 65 : 'sixty-five',	66 : 'sixty-six', 67 : 'sixty-seven', 68 : 'sixty-eight', 69 : 'sixty-nine',
        70 : 'seventy', 71 : 'seventy-one',	72 : 'seventy-two', 73 : 'seventy-three', 74 : 'seventy-four', 75 : 'seventy-five',	76 : 'seventy-six', 77 : 'seventy-seven', 78 : 'seventy-eight', 79 : 'seventy-nine',
        80 : 'eighty', 81 : 'eighty-one', 82 : 'eighty-two', 83 : 'eighty-three', 84 : 'eighty-four', 85 : 'eighty-five', 86 : 'eighty-six', 87 : 'eighty-seven', 88 : 'eighty-eight', 89 : 'eighty-nine',
        90 : 'ninety',  91 : 'ninety-one', 92 : 'ninety-two', 93 : 'ninety-three', 94 : 'ninety-four', 95 : 'ninety-five', 96 : 'ninety-six', 97 : 'ninety-seven', 98 : 'ninety-eight', 99 : 'ninety-nine',
        100 : 'one hundred'}
    k=1000
    if (n < 20):
        return a[n]

    elif (n < 100):
        if n % 10 == 0: 
            return a[n]
        else: 
            return a[n]

    elif (n < k):
        if n % 100 == 0: 
            return a[n // 100] + ' hundred'
        else: 
            return a[n // 100] + ' hundred ' + three_digits_to_word(n % 100)    

    

def num_to_word(num):
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if (num < 20):
        return three_digits_to_word(num)

    elif (num < 100):
        return three_digits_to_word(num)

    elif (num < k):
        return three_digits_to_word(num) 

    elif (num < m):
        if num % k == 0: 
            return num_to_word(num // k) + ' thousand'
        else: 
            return num_to_word(num // k) + ' thousand ' + num_to_word(num % k)

    elif (num < b):
        if (num % m) == 0: 
            return num_to_word(num // m) + ' million'
        else: 
            return num_to_word(num // m) + ' million ' + num_to_word(num % m)

    elif (num < t):
        if (num % b) == 0: 
            return num_to_word(num // b) + ' billion'
        else: 
            return num_to_word(num // b) + ' billion ' + num_to_word(num % b)


if __name__ == '__main__':
    main() 






