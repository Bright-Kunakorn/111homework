#!/usr/bin/env python3
# Tassin Ongsakul(dossdy)
# 64051065
# Hw09_3
# 204111 Sec 001
def main():
    num = int(input())
    print (num_to_word(num))

def three_digits_to_word(n):
    return { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', 
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'ninteen',   
          20 : 'twenty', 30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
  
def num_to_word(num):
    n = str(num)
    d = three_digits_to_word(n)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0:
            return d[num]
        else:
            return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < 1000):
        if num % 100 == 0:
            return d[num // 100] + ' hundred'
        else:
            return d[num // 100] + ' hundred ' + num_to_word(num % 100)

if __name__ == '__main__':
    main()





