def printTheArray(arr, n):
    ans =''
    for i in range(0, n):
        ans += str(arr[i])
    return ans

def generateAllBinaryStrings(n, arr, i,count,l_ans):
    if i == n:
        x = printTheArray(arr, n)
        l_ans.append(x)
        return
    arr[i] = 3
    generateAllBinaryStrings(n, arr, i + 1,count,l_ans)
    arr[i] = 4
    generateAllBinaryStrings(n, arr, i + 1,count,l_ans)
    return l_ans

def find_max(n):
    i = 1
    while 2**i <= n:
        i+= 1
    return i

def nth_term(n):
    l_ans = []
    num = find_max(n)
    arr = [None] * num
    for i in range(1,num+1):
        x = (generateAllBinaryStrings(i, arr, 0 , 0 , l_ans))
    return int(x[n-1])

def main():
    print(nth_term(16))

if __name__ == '__main__':
    main()