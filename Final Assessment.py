def modify(arg_list):
    arg_list = arg_list + [50, 60]
    print("Inside:",arg_list)
i_list = [10,50]
print("Before:",i_list)
modify(i_list)
print("After:",i_list)

samp = {'a':"apple", 'b':"ball"}
samp.update({'b':"boy",'c':"cat"})
print(samp)

t = (10)
print(t)
print(type(t))

set_1 = {1,2,3,1,2,4,5,3,4,8,9,7,10}
for i in range(len(set_1)):
    print(i,end=" ")
print()
def value(num):
    list1 = []
    while num != 0: 
        if num%2 == 0:
            list1.append(num)
        else:
            break
        num -= 2
    print(list1)
value(10)

list3 = [2,4]
list3.insert(7,10)
print(list3)
