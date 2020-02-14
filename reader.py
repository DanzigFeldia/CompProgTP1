def reader(filePath):
    with open(filePath, 'r') as f:
        file = f.read()
        lines = file.split("\n")
        (R,C,F,N,B,T) = str(lines[0]).split() #first line


    return (R,C,F,N,B,T)
