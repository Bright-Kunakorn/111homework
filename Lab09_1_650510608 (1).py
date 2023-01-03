

def main():
    x = int(input(""))
    y = int(input(""))
    print(sum_prime_in_range(x,y))
    

def sum_prime_in_range(x,y):
    if not new_funtion:
        return 0
    else:
        return new_funtion[0] + sum_prime_in_range(new_funtion[1:])
    
def new_funtion(x,y):
    num = range(x, y+1, 1)
    list_prime = filter(primenum,num)
    return list_prime
  
def primenum(x, i=2):
    if x == i:
        return True
    elif x % i == 0:
        return False
    else:
        return primenum(x, i + 1)
    
    
if __name__ == '__main__':
    main()