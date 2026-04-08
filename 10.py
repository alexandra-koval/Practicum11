string1  = input()
lst1 = [int(x) for x in string1.split()]
string2 = input()
lst2 = [int(x) for x in string2.split()]
a = int(input())
b = int(input())
for i in range(b-1,a-2,-1):
    lst2.append(lst1[i])
    lst1.pop(i)
print(lst1)
print(lst2)

