#Fibonacci Sequence

#taking input
nterms = int(input("Please Enter Positive Integer : "))

n1,n2 = 0,1
count = 0

if nterms <=0:
    print("Please Enter Positive Integer")
elif nterms == 1:
    print("Fibonacci sequence for "+str(nterms)+ " is "+ str(n1))
else:
    print("Fibonacci sequence for ",str(nterms))
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count +=1

