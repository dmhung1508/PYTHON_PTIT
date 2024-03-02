t = int(input())
list1 = []
for i in range(t):
    s= input()
    list1.append(s)

unique_elements = set(list1)
print(len(unique_elements))