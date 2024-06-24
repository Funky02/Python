#++++++++++++++++++++Reverse the number+++++++++++++
# x = 1234
# b = 0
# while x > 0:
#      a=x % 10
#      b=(b * 10)+a
#      x=x//10
# print(b)

#+++++++++++++++++REverse the string++++++++++++++++++++++++

# s = "hello"
# re = ""
# for char in s:
#     re = char + re
# print(re)  # Output: "olleh"

#++++++++++++++++++REverse the string+++++++++++++++++++++++++

# s="hello"

# for x in range(len(s)-1,-1,-1):
#     print(s[x])


#++++++++++++ REVERSE the string ++++++++++++++++++++++++++

# # x="rohith"
# x=["r","o","h","i","t","h"]
# print(x[-1::-1])
#   #----or------
# print(x[::-1])

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

x="rohith"
a=list(x)
print(a[-1::-1])