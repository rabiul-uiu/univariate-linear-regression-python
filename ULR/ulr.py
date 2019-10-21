import csv
import math



file1 = open("train.csv", "r")
file2= open("test.csv", "r")
csv1 = csv.reader(file1)
csv2=csv.reader(file2)
list1=list(csv1)
list2=list(csv2)
train=[]
test=[]

for i in range(1,len(list1)):
    train.append(list1[i])


for i in range(1,len(list2)):
    test.append(list2[i])

sumx=0
sumy=0


for i in range(0,len(train)):
    sumx=sumx+ float(train[i][0])
xavg=sumx/len(train)


for i in range(0,len(train)):
    sumy=sumy+ float(train[i][1])
yavg=sumy/len(train)

SSxy=0

for i in range(0, len(train)):
    sub1 = float(train[i][0]) - xavg
    sub2 = float(train[i][1]) - yavg
    multi = sub1 * sub2
    SSxy=SSxy+multi

SSxx=0
for i in range(0, len(train)):
    power = pow((float(train[i][0]) - xavg),2)

    SSxx=SSxx+power

B1=SSxy/SSxx

B0=yavg-(B1*xavg)




esum=0
for i in range(0, len(test)):
    y=B0+B1*float(test[i][0])
    # print(y)
    e=float(test[i][1])-y
    esum=esum+pow(e,2)



    print("E",i+1," :",e)
print("===")
meanerror=esum/(2*len(test))
print("Mean Error")
print(meanerror)