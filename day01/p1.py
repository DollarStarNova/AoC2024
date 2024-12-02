list_a = []
list_b = []
diffsum = 0

with open("day01/input.txt", "r") as data:
    for line in data:
        a, b = line.split()
        list_a.append(int(a))
        list_b.append(int(b))
list_a.sort()
list_b.sort()

i=0
while i < len(list_a):
    diffsum += abs(list_a[i] - list_b[i])
    i+=1

print(diffsum)