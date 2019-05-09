#Card Validation Program 
def input1():
    print("Enter the card number: ")
    firsthalf=list()
    sechalf=list()
    for i in range(1,17):
        x=int(input())
        if i<9:
            firsthalf.append(x)
        else:
            sechalf.append(x)
    return(firsthalf,sechalf)

def process(a,b):
    sum1=int(0)
    sum2=int(0)
    for i in a:
        sum1=sum1+i
    for i in b:
        sum2=sum2+i
    print(sum1,sum2)

    if sum1>sum2:
        diff=sum1-sum2
    else:
        diff=sum2-sum1
    print(diff)
    
    if (diff%2) != 0:
        print("CARD IS VALID ")
    else:
        print("CARD is INVALID ")
    
if __name__ == "__main__":
   a=list()
   b=list()
   choice=str(input("Do you want to quit - Press q: "))
   while choice != 'q' :
     a,b=input1()
     process(a,b)
     choice=str(input("Do you want to quit - press q: "))