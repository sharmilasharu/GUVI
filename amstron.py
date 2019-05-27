    
N=int(input(""))
s=0
num=N
while(N>0):
  r=N%10
  s=s+(r**3)
  N=N//10
if(s==num):
  print("yes")
else:
  print("no")
