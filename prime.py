Number=int(input())
num=0
for i in range(2,Number):
  if(Number%i==0):
    num=1
    break
if(num==1):
  print("no")
else:
  print("yes")
