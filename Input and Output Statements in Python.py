a = input("Enter Your Name:")
b = int(input("Enter Your Age:"))
c = 20.126
print(a,type(a))
print(b,type(b))
print(c,type(c))
# end is used to specify separator between two print statements  , by default = \n
# sep is used to specify between multipke variables displayed using a single print statement
print(a,b,c)
print(a,b,c,sep=':')
print(a,b,c,end=' ')

print("c=%-8d" %c,end=";")
print("c=%8d" %c,"b=%0.2f" %b,sep=':::')
print(5%6) # = 5

'''
In Python, pass is a null statement which is used to do create empty blocks.
When pass is executed, it results in no-operation and the control will move to the next statement applicable.
Below example shows how pass can be used to create an empty if block.

Example:
'''

num=10
count=0
while(count <= num):
    if(count%2 == 0):
        pass
    else:
        print(count)
    count+=1
