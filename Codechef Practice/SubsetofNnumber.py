# a=[]
# def subset(n,i,output):
#     # if i==0:
#     #     a=[]

#     if i==n:
#         print(output)
#         a.append(output)
#         return 
    
#     subset(n, i+1, output)
#     output.append(i+1)
#     subset(n, i+1, output)
#     output.pop()

#     if i==0:
#         return a
#     else:
#         return
        
# b=[]
# b=subset(3,0,[])    
# print(b)
# # for i in range(len(a)):
# #     a[i].sort()

# # a.sort()

# # for i in range(len(a)):
# #     for j in range(len(a[i])):
# #         print(a[i][j],end=" ")
# #     print("")

   
def fun(li,i,res): #fun([1,2,3],2,"")
    if i == -1:
        print(res)
        return
    fun(li,i-1,res)
    fun(li,i-1,str(li[i]) + ' '+res)
    return

t=int(input())
for x in range(t):
    n=int(input())
    l=list(range(1,n+1))
    fun(l,len(l)-1,"")  


