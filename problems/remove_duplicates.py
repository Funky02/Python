# string = 'rohith'
# e = ''
# x=''
# for char in string:
#     if char not in e:
#         e+= char
#     else:
#         x+=char
# print("String with duplicates removed:",e)
# print(x)

#-----------------------------------------------------

# string = 'rohith'
# x=''
# y=''
# for char in string:
#     if char in x:
#         y+= char 
#     else:
#         x+=char
# print("String with duplicates removed:", y)
# print("String with original:", x)

#--------------------------------------------------------

x=['r','o','h','i','t','h']
a=''
b=''

for p in x:
    if p in a:
        b+= p
    else:
        a+=p
print("duplicates",b)
print("original",a)