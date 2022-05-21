import numpy as np

def normalizeRows(x):
    return 0
    
path = "./Data/Annotations512/Annotations512/annotation512.txt"
path2 = "./Data/1Vehicules512/Vehicules512/"

annotations = open(path, 'r')
outfile = open("annotations.txt", "w")
outfile.close()
outfile = open("annotations.txt", 'a+')
# outfile.truncate(1000000)
annotationsLines = annotations.readlines()
array = []
for i in range(0,1272):
    array.append([])
for i in range (0, len(annotationsLines)):
    splitLine = annotationsLines[i].split(" ")
    array[int(splitLine[0])].append(splitLine)
    print(i)
    
for i in array:
    if(len(i) == 0):
        outfile.write("")
    elif(len(i) == 1):
        toAdd = path2 + i[0][0] + "_co.png"
        toAdd += " " + str(np.min(np.array([int(k) for k in i[0][4:8]]))) + ","
        toAdd += str(np.min(np.array([int(k) for k in i[0][8:12]]))) + ","
        toAdd += str(np.max(np.array([int(k) for k in i[0][4:8]]))) + ","
        toAdd += str(np.max(np.array([int(k) for k in i[0][8:12]]))) + ","
        toAdd += str(normalizeRows(int(i[0][12])))
        outfile.write(toAdd)
        print(i[0])
        outfile.write('\n')
    else:
        toAdd = path2 + i[0][0] + "_co.png"
        for j in i:
            toAdd += " " + str(np.min(np.array([int(k) for k in j[4:8]]))) + ","
            toAdd += str(np.min(np.array([int(k) for k in j[8:12]]))) + ","
            toAdd += str(np.max(np.array([int(k) for k in j[4:8]]))) + ","
            toAdd += str(np.max(np.array([int(k) for k in j[8:12]]))) + ","
            toAdd += str(normalizeRows(int(j[12])))
        outfile.write(toAdd)
        if(toAdd != ""):
            outfile.write("\n")


outfile.close()