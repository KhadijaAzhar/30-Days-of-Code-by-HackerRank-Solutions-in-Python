n=int(input())
d={}
#d=[map(str, input.split()) for x in range(n)]
for i in range(n):
    name,num=input().split()
    d[name]=num
    
    


for i in range(n):
    try:
        name = input()
       
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
   
    except:
        break


