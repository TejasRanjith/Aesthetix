li = [1,2,1,2,1,2,3,1,2,2,3,3,3,3]
result = {}
# identify the number which is occuring for odd number of times
for elem in li:
    result[elem] = li.count(elem)
for key in result:
    if result[key] % 2 != 0:
        print(key)
print(result)