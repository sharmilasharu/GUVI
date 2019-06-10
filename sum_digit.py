number=int(input())
temp=number
sum_of_dig=0
while(number!=0):
  remainder=number%10
  sum_of_dig=sum_of_dig+remainder
  number=number//10

print(sum_of_dig) 
  
