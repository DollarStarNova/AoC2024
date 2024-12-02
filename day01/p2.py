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

entry_counter = {}
for a in list_a:
    if not str(a) in entry_counter.keys():
        entry_counter[str(a)] = {'leftcount':1, 'rightcount':0}
    else:
        entry_counter[str(a)] = {
            'leftcount': entry_counter[str(a)]['leftcount'] + 1,
            'rightcount': entry_counter[str(a)]['rightcount']
        }

for b in list_b:
    if str(b) in entry_counter.keys():
        entry_counter[str(b)]['rightcount'] = entry_counter[str(b)]['rightcount'] + 1

total = 0

for key, value in entry_counter.items():
    total += value['leftcount'] * int(key) * value['rightcount']

print(total)