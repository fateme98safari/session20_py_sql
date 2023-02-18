import random

list_marry=[]

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']
# for i in range(len(boys)):
while len(boys)>0:    
    b=random.randint(0,len(boys)-1)
    g=random.randint(0,len(girls)-1)
    list_marry.append([boys[b],girls[g]])
    del boys[b]
    del girls[g]
print(list_marry)    


