from math import log2


def profit(n, country):
    Total_rounds = int(log2(n))
    temp = Total_rounds-2
    teams = list(range(1, n+1))
    #match_no = n-(2**(int(log2(n))-1))
    profitable_matches = 0
    winner = []
    # n = n//2
    for i in range(1, Total_rounds+1):

        k = 0

        for j in range(1, (((n//(2**i))+1))):
            
            if country[teams[k]] != country[teams[k+1]]:
                profitable_matches+=1

            winner.append(teams[k])
            k += 2
            #match_no += 1
        

        teams = winner
        print(teams)
        winner.clear()
        #match_no = 2**(temp)
        #temp -= 1
        # n = n//2


    print(profitable_matches)


n = int(input())
country = [0]
country.extend((map(int, input().split())))
profit(n, country)
