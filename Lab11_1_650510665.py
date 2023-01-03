#!/usr/bin/env python3
# Thidathip  Inphithak Lucky
# 650510665
# Lab11_1
# 204111 Sec 03

import math
def leap_year(y):
    if (y % 4 == 0):
        if (y % 400 == 0):
            return ("YES")
        elif (y % 100 == 0): return ("NO")
        else: return("YES")
    else: return("NO")
def display_calendar(month, year):
    k=year%100
    j=math.floor(year/100)
    if month==1: 
        m=13
    elif month==2: 
        m=14
    else: m=month
    # print(k, j)
    h=int((1+(math.floor(13*(m+1))/5)+k+(math.floor(k/4))+(math.floor(j/4))-(2*j))%7)
    if m==13 or m==14:
        h=h-1
    else: h=h
    # print("h", h)
    d=((h+5)%7)+1
    # print("d", d)
    if month==2: #เดือน2
        # print(leap_year(year), d)
        if leap_year(year)=="YES":
            d=d-1
            day=29
        elif leap_year(year)=="NO": 
            day=28
    elif month in [1,3,5,7,8,10,12]: #เดือนลงด้วยคม มี31วัน
        day=31
    else: 
        day=30
    # print(day)
    print("Su Mo Tu We Th Fr Sa")
    list_d=[]
    if d!=7:
        list_d=['--']*d
    list_d.extend(list(range(1,day+1)))
    # print(list_d)
    list_w=[]
    for index in range(len(list_d)):
        if index%7==0:
            list_w.append(list_d[index:index+7])
            index+=1
    # print(list_w)
    for item in list_w:
        for n in item:
            if type(n)==int:
                print("%2d" % (n), end=" ")
            else: print(n, end=" ")
        print("")
def main():
    display_calendar(2, 2023)

if __name__ == '__main__':
    main()
