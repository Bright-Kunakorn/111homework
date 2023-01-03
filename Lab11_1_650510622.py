#!/usr/bin/env python3
# Nantapa Adirektammakorn jingjing
# 650510622
# Lab011_1
# 204111 Sec 002

def main():
    #month = int(input())
    #year = int(input())
    #for i in range(1,13):
    #    display_calendar(i,2000)
    display_calendar(10,2000)
    

def display_calendar(month, year):
    feb1 =[31, 28, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31]
    feb2 =[31, 29, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31]
    s = 0
    if year % 4 == 0: #เช็คleap year
        for i in range(month-1):
            s+= feb2[i]
    else:
        for i in range(month-1):
            s+= feb1[i]
    day =(year-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7
    day += s % 7
    day = day % 7
    space ='--'
    space = space.rjust(2, ' ')
    print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
  
    if month == 9 or month == 4 or month == 6 or month == 11: 
        for i in range(31 + day):
            if i<= day:
                print(space, end =' ')
            else:
                print('{:2d}'.format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    elif month == 2:
        if year % 4 == 0:
            p = 30
        else:
            p = 29
          
        for i in range(p + day):
            if i<= day:
                print(space, end =' ')
            else:
                print('{:2d}'.format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    else:
        for i in range(32 + day):
            if i<= day:
                print(space, end =' ')
            else:
                print('{:2d}'.format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    print('\n')

if __name__ == '__main__':
    main()