para=input()
d=0
for i in range(len(para)):
  if(para[i].isdigit() or para[i].isalpha()):
    pass
  else:
    d=d+1
   
print(d)
