def reader(filePath):
    with open(filePath, 'r') as f:
        file = f.read()
        lines = file.split("\n")
        (R,C,F,N,B,T) = str(lines[0]).split() #first line
        rides = {}
        i=0
        for line in lines[1:len(lines)-1]:
            rides[i] = str(line).split()
            i += 1

    return (R,C,F,N,B,T, rides)
