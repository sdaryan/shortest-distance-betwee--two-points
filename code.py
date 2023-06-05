list1 = input().split()

list2 = [int(item) for item in list1]

list3 = sorted(list2)

results=list3[-1]-list3[0]

print(results)
