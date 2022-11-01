#!/usr/bin/python3
import itertools

list=[]

support=float(input("Enter the minimum support: "))

items=['i1','i2','i3','i4','i5']
num=int(input("Enter number of transactions: "))

for i in range(num):
    print("Enter the items bought in transaction ",i+1," separated by a comma: ")
    val=input()
    list.append(val)
print("Tranactions are as follows: ")

for i in list:
    print(i)

print("The candidate set C1 is : ",items)

#calculate support for all items in candidate set C1
supportc1=[]
for item in items:
    val=0
    for i in range(len(list)):
        if item in list[i]:
            val+=1
    supportc1.append(float(val/5))
    

for i in range(5):
    print("Support for ",items[i]," is : ",supportc1[i])

print("Genrating L1 which is frequent 1-item set from C1")
l1=[]
for i in range(len(items)):
    if supportc1[i]>=support:
        l1.append(items[i])
print("L1 is : ",l1)
#---------------------------------------------------------------------------------------------------------
#Generating Candidate set C2
c2=[]
for val in itertools.combinations(items,2):
    c2.append(val)

#calculating support for all items in c2
print("Candidate set c2 is : ",c2)
supportc2=[]

for i in range(len(c2)):
    val=0 
    for item in list:
        if c2[i][0] in item and c2[i][1] in item: 
            val+=1
    supportc2.append(float(val/5))


for i in range(len(c2)):
    print("Support for ",c2[i]," is : ",supportc2[i])

#generating L2 from C2
l2=[]
for i in range(len(c2)):
    if supportc2[i] >=support:
        l2.append(c2[i])
print(l2)
#--------------------------------------------------------------------------------------------------------------

c3=[]
for val in itertools.combinations(items,3):
    c3.append(val)

supportc3=[]

for i in range(len(c3)):
    val=0
    for item in list:
        if c3[i][0] in item and c3[i][1] in item and c3[i][2] in item:
            val+=1
    supportc3.append(float(val/5))

for i in range(len(c3)):
    print("Support for : ",c3[i]," is: ",supportc3[i])

#generating L3 from C3

l3=[]

for i in range(len(c3)):
    if supportc3[i] >=support:
        l3.append(c3[i])
print("L3 is : ",l3)

#---------------------------------------------------------------------------------
confidence=[]

for i in range(len(l3)):
    val=0
    div=0
    for item in list:
        if l3[i][0] in item:
            if l3[i][0] in item and l3[i][1] in item and l3[i][2] in item:
                val+=1
                div+=1
    confidence.append(float(val/div))

for i in range(len(l3)):
    print("Confidence for ",l3[i]," is: ",confidence[i])
