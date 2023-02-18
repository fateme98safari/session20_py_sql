
list=[4,3,5,3,4]
statement=''

k=(len(list)//2)
for i in range(1,k):
        if(list[k-i]==list[k+i]):
            statement=True
        else:
            ststement=False
if statement==True:
        print("symmetrical")
else:
        print("asymmetric")





