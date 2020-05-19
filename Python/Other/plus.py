f = open("p.txt", "r");
arr = []
if f.mode == 'r':
    x = f.readlines()
    x = [i.strip('\n') for i in x]
    for i in range(200):
        arr.append(int(x[i]))

c = []
for i in range(len(arr)-1):
    if i != len(arr) - 2:
        z = arr[i+1] - arr[i]
        c.append(z)
print(c)
