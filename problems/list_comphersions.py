num=[1,2,3,4]
# for long running for loop we can use short form of below operations also


# a=[]
# for x in num:
#     print(x*x)
#     a.append(x)
# print(a)    
    
# +++++++ list Comphersion using map++++++++++++++
# a=list(map(lambda n:n*n,num))  #map(lambda variable : operation,exist values from)
# print(a)

#++++++++++ List Comphersion using empty list+++++++++++++++++++
# l=[n*n for n in num]  ##[operation, loop]
# print(l)

#+++++++++++List Comphersion using list++++++++++++++
# l=[n for n in num if n%2==0] ## [result, loop, operation for if]
#print(l)


#+++++++++++++++ convert 2 list to dictonary+++++++++++++++++++++++++++++++++++++
names=['a','b','c','d']
heros=['x','y','z','q']

x={name:hero for name, hero in zip (names,heros)}
# for suppose if you dont want d 
x={name:hero for name, hero in zip (names,heros) if name !='d'}
print (x)
