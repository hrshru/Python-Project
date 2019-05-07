''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


a=int(input())
b=int(input())
c=(input())
d=(input())
count=0
count1=0
for z in range(b):
    list1=c.split()
    list2=d.split()
    for j in list1:
        for k in list2:
            if j[0]>k[0]:
                count+=1
                break
                
            else:
                count1+=1
if(count<count1):
    print("WIN")
else:
    print("LOSE")
                
    
    




