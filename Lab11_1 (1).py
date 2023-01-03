def main():

    display_calendar(2, 2023)



def display_calendar(month, year) :
    mm = month
    yy = year
   
    day =(yy-1)% 400
    day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
    day = day % 7
  
    nly =[31, 28, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31]
    ly =[31, 29, 31, 30, 31, 30, 
        31, 31, 30, 31, 30, 31]
    s = 0
  
    if yy % 4 == 0:
        for i in range(mm-1):
            s+= ly[i]
    else:
        for i in range(mm-1):
            s+= nly[i]
  
    day += s % 7
    day = day % 7
   
  
    print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
  
    if mm == 9 or mm == 4 or mm == 6 or mm == 11: 
        for i in range(31 + day):
            if i<= day:
                print("--", end =' ')
            else:
                print("{:2d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    elif mm == 2:
        if yy % 4 == 0:
            p = 30
        else:
            p = 29
          
        for i in range(p + day):
            if i<= day:
                print('--', end =' ')
            else:
                print("{:2d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print() 
    else:
        for i in range(32 + day):
          
            if i<= day:
                print('--', end =' ')
            else:
                print("{:2d}".format(i-day), end =' ')
                if (i + 1)% 7 == 0:
                    print()
    print()

if __name__ == '__main__':
    main()