import numpy as np
import random as rd
import matplotlib.pyplot as plt

#Read Data
Data_X = []
Data_Y = []
Train_Data = input("Train data file:")
f = open(Train_Data, "r")
if f.mode == "r":
	fl = f.readlines()
	for line in fl:
		Data = line.split()
		Data_X.append([1.0] + [float(i) for i in Data[0:4]])
		Data_Y.append(int(Data[4]))
f.close()
Data_X = np.array(Data_X)
Data_Y = np.array(Data_Y)

def Test(X, Y, W):
	ErrorCount = 0
	Length = len(Y)
	for i in range(Length):
		if sign(np.inner(W, X[i])) != Y[i]:
			ErrorCount += 1
	ErrorRate = float(ErrorCount)/Length
	return ErrorRate

def GoNext(Pos, Length):
	if Pos < Length-1:
		Pos += 1
	else:
		Pos = 0
	return Pos

def PLA(X, Y, cycle, InitWeight, LearningRate):
	Length = len(Y)
	Weight = InitWeight
	Success = 0
	LastFail = -1
	Current_Id = 0
	UpdateCount = 0
	while(not Success):
		Current_Pos = cycle[Current_Id]
		#If the current point is correct, check if we can halt, else continue
		if Y[Current_Pos] * np.inner(Weight, X[Current_Pos]) > 0:
			#Went for a full round without mistake with initial weight (NOT likely to happen)
			if LastFail == -1 and Current_Id == Length-1:
				Success = 1
				continue
			#Went for a full round with out mistake from last point we updated
			elif Current_Pos == LastFail:
				Success = 1
				continue
			#Otherwise go to the next point
			else:
				Current_Id = GoNext(Current_Id, Length)
				continue
		#If the current point is error, update the weight
		else:
			LastFail = Current_Pos
			#Update the weight
			Weight += LearningRate * Y[Current_Pos] * X[Current_Pos]
			UpdateCount += 1
			Current_Id = GoNext(Current_Id, Length)
			continue
	return UpdateCount

TotalIter = 1126
TrackUpdateCount = []
Cycle = list(range(len(Data_Y)))
for iter in range(TotalIter):
	rd.shuffle(Cycle)
	TrackUpdateCount.append(PLA(Data_X, Data_Y, Cycle, np.array([0.0] * len(Data_X[0])), 1.0))

print("Average Update: ", sum(TrackUpdateCount)/TotalIter)

#Plotting...
plt.hist(TrackUpdateCount, bins = 30)
plt.xlabel("Number of updates")
plt.ylabel("Frequency")
plt.show()