def reader(filePath):
    with open(filePath, 'r') as f:
        file = f.read()
        lines = file.split("\n")
        param = str(lines[0]).split() #first line
        (R, C, F, N, B, T) = map(int,param)
        rides = {}
        i=0
        for line in lines[1:len(lines)-1]:
            rides[i] = str(line).split()
            for (j, param) in enumerate(rides[i]):
                rides[i][j] = int(rides[i][j])

            rides[i].append(0) #0 = libre, 1 = pris en charge
            i += 1

    return (R,C,F,N,B,T, rides)
