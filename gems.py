#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    while(reqd_quantity!=0):
        
        if(reqd_gems[0]==gems_list[0]):
            bill_amount=price_list[0]*reqd_quantity[0]
            return bill_amount
        elif(reqd_gems[0]==gems_list[1]):
            bill_amount=price_list[0]*reqd_quantity[0]
            return bill_amount
        elif(reqd_gems[0]==gems_list[2]):
            bill_amount=price_list[0]*reqd_quantity[0]
            return bill_amount
        elif(reqd_gems[0]==gems_list[3]):
            bill_amount=price_list[0]*reqd_quantity[1]
            return bill_amount
        elif(reqd_gems[1]==gems_list[0]):
            bill_amount=price_list[1]*reqd_quantity[1]
            return bill_amount
        elif(reqd_gems[1]==gems_list[1]):
            bill_amount=price_list[1]*reqd_quantity[1]
            return bill_amount
        elif(reqd_gems[1]==gems_list[2]):
            bill_amount=price_list*reqd_quantity[1]
            return bill_amount 
        elif(reqd_gems[1]==gems_list[3]):
            bill_amount=price_list[1]*reqd_quantity[1]
            return bill_amount
        elif(reqd_gems[2]==gems_list[0]):
            bill_amount=price_list*reqd_quantity[2]
            return bill_amount    
        elif(reqd_gems[2]==gems_list[1]):
            bill_amount=price_list*reqd_quantity[2]
            return bill_amount    
        elif(reqd_gems[2]==gems_list[2]):
            bill_amount=price_list*reqd_quantity[2]
            return bill_amount    
        elif(reqd_gems[2]==gems_list[3]):
            bill_amount=price_list*reqd_quantity[2]
            return bill_amount    
        
            
    
   

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
