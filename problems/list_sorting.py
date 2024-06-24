# def num(lis):
#     for i in range(len(lis)):
#         for j in range(len(lis)-1):
#             if lis[j]>lis[j+1]:
#                 lis[j],lis[j+1]=lis[j+1],lis[j]
# def main():
#     x=[1,66,33,1,77,22,55]
    
#     print('before sorting',x)
#     num(x)
#     print('after sorting',x)
    
# main()

#++++++++++++++++ sort using sort methods & reverse it+++++++++++++++++++++++++++++++++++++++++++++++++

# x=[1,3,4,3,2,4,64,3]
# x.sort()
# #x.sort(reverse=True) # to reverse the list
# print(x)

#++++++++++++++++++++++++ list , set , dic sort by using sorted method & reverse it +++++++++++++++++++++++++++++++++++++++++++++

# x=[1,3,2,7,54,3,4]
# x={1,3,2,7,54,3,4}
# x=(1,3,2,7)
# #a=sorted(x)
# a=sorted(x, reverse=True) # to reverse the list
# print(a)

#++++++++++++++++++++

# x=[-4,-6,0,1,2]
# a=sorted(x,key=abs)
# print(a)

#+===============================================

class employee:
    def __init__(self,name,age,salary) -> None:
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return f"{self.name}, age={self.age}, salary={self.salary}\n"
        
e1=employee('rohith',23,23000)
e2=employee('veeru',24,50000)
e3=employee('vamshi',23,23000)

employees=[e1,e2,e3]

def e_sort(emp):
    return emp.name
ss=sorted(employees, key=e_sort)
print(ss)

