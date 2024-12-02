def checksafe(line):
        safe = True 
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
        return safe

safe_count = 0
with open("day02/input.txt", "r") as data:
    for line in data:
        line = list(map(int, line.split()))
        verysafe = checksafe(line)
        if verysafe:
            safe_count += 1
        else:
            i = 0
            while i < len(line):
                myline = line.copy()
                myline.pop(i)
                if checksafe(myline) == True:
                    print(myline)
                    safe_count += 1 
                    break
                i+=1


print(safe_count)
