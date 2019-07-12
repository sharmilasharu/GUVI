Number=int(input())
sec_num=list(map(int,input().split()))
new_lis=[]
count=0
for i in range(0,Number+1):
  if(sec_num.count(i)>1):
    new_lis.append(i)
if(len(new_lis)==0):
  print("unique")
  
fin_list=sorted(new_lis)
print(*fin_list)    
    
  
