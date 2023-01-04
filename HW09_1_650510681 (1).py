def main():
  n = int(input(""))
  print(life_path(n))


def life_path(n):
  listnum = list(map(int, str(n)))
  sum_num = sum(listnum)
  if sum_num < 9 :
    return sum_num       
  else:
    return life_path(sum_num )

if __name__ == '__main__':
  main()
          
