for _ in range(int(input())):
    n = int(input())
    cnt = 0
    if n == 1:
        print('Bob')
    else:
        while n != 1:
            flag = False
            i = 1
            while 2**i <= n:
                if 2**i == n:
                    flag = True
                    break
                
                maxi = 2**i
                flag=False
                i += 1

            if flag == True:
                n = n//2
                cnt += 1
            else:
                n -= maxi
                cnt += 1
        if cnt % 2 == 0:
            print('Bob')
        else:
            print('Alice')
