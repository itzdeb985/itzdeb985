#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Creating a restaurant tip program

# If the bill is $150, then split between x number of people, add tip as per choice, and then pay the bill

print("Welcome to Tip calculator : ")
bill = float(input("What is the amount of the bill: ? $"))
#bill_dtype = type(bill)
#print(bill_dtype)
bill_tip=int(input("How much tip you want to give ? 10 , 12 , 15 , 20: %"))
group_num=int(input("How many people are their in your group ?"))
tip_amount=(bill_tip/100)*bill
Total_bill= tip_amount+bill
print(f"Total bill including tip is {Total_bill}")
Per_person_cost=Total_bill/group_num
print (f"Per_person_cost will be $ {Per_person_cost}")
#print(tip_amount)




# In[ ]:




