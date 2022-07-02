t = int(input())
final_answers=[]
for i in range(t):
    k = 0
    count = 1
    n = int(input())
    m = int(input())
    a = []
    c=[]
    for j in range(n):
        l, r = map(int, input().split())
        a.append([l, r])
    a.sort()
    for q in range(n-1):
        if max(a[q][0], a[q+1][0]) <= min(a[q][1], a[q+1][1]):
            a[q+1][1] = min(a[q][1], a[q+1][1])
            a[q+1][0] = max(a[q][0], a[q+1][0])
            count += 1
        else:
            c.append(count)
            count = 1
        

    c.append(count)

    if n==0:
        final_answers.append(0)
    else:
        final_answers.append(max(c))
for e in range(len(final_answers)):
    print(final_answers[e],end=" ")
    
