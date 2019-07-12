Number=int(input())
sec_num=list(map(int,input().split()))
sin_list=sorted(sec_num)
sin_list.reverse()
if(sin_list[0]==0):
   print("0")  
else:
  print(*sin_list)  
     
    
  
