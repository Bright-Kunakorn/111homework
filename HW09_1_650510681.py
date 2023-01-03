#!/usr/bin/env python3
# waraporn sonwai bour
# 650510681
# HW09_1
# 204111 Sec 003

def main():
  n = 120210201000000000000000000
  print(life_path(n))


def life_path(n):
  listnum = list(map(int, str(n)))
  sum_num = sum(listnum)
  if sum_num <= 9:
    return sum_num       
  else:
    return life_path(sum_num)

if __name__ == '__main__':
  main()
          