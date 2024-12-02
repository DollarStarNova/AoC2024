safe_count = 0
with open("day02/input.txt", "r") as data:
    numlines = 0
    for textline in data:
        numlines += 1
        safe = True
        direction = 0
        i = 0
        line = list(map(int, textline.split()))
        
        ordering = 0
        dif = abs(line[1] - line[0])
        if  dif > 3:
            safe = False
        elif dif == 0:
            safe = False
        elif line[1] > line[0]:
            ordering = 1
        else: 
            ordering = -1
        
        i = 2
        while i < len(line):
            dif = abs(line[i] - line[i-1])
            if dif > 3:
                safe = False
                break
            if dif == 0:
                safe = False
                break
            if (line[i] > line[i-1] and ordering == -1):
                safe = False
                break
            if (line[i] < line[i-1] and ordering == 1):
                safe = False
                break
            i+=1
        if safe:
            safe_count += 1



print(numlines)
print(safe_count)
