Data_X = []
Data_Y = []

#Read Data
Train_Data = input("Train data file:")
f = open(Train_Data, "r")
if f.mode == "r":
	fl = f.readlines()
	for line in fl:
		Data = line.split()
		Data_X.append([1.0] + [float(i) for i in Data[0:4]])
		Data_Y.append(int(Data[4]))
f.close()

Train_Length = len(Data_Y)

TestData_X = []
TestData_Y = []

#Read Data
Test_Data = "PLA_Test_data_18"
f = open(Test_Data, "r")
if f.mode == "r":
	fl = f.readlines()
	for line in fl:
		TestData = line.split()
		TestData_X.append([1.0] + [float(i) for i in TestData[0:4]])
		TestData_Y.append(int(TestData[4]))
f.close()

Test_Length = len(TestData_Y)

import numpy as np

Data_X = np.array(Data_X)
Data_Y = np.array(Data_Y)
weight = np.array([0.0] * 5)

def GoNext(Pos):
	if Pos < Train_Length-1:
		Pos += 1
	else:
		Pos = 0
	return Pos

def sign(x):
	return -1 if x <= 0 else 1

def Test(X, Y, W):
	ErrorCount = 0
	Length = len(Y)
	for i in range(Length):
		if sign(np.inner(W, X[i])) != Y[i]:
			ErrorCount += 1
	ErrorRate = float(ErrorCount)/Length
	return ErrorRate

def PLA(X, Y, cycle, updatecount):
	weight = np.array([0.0] * 5)

	if updatecount == -1:
		Success = 0
		LastFail = -1
		Current_Id = 0
		UpdateCount = 0
		while(not Success):
			Current_pos = cycle[Current_Id]

			#Get the sign of current point
			Sign = sign(np.inner(weight, X[Current_pos]))

			#If current point is success
			if Sign == Y[Current_pos]:
				#Success, if the initial line is correct
				if LastFail == -1 and Current_Id == Length-1:
					Success = 1
					continue
				#check if it went for a full round
				if Current_pos == LastFail:
					Success = 1
					continue

				#If not, check next point
				Current_Id = GoNext(Current_Id)
				continue
			#If current point fails:
			else:
				LastFail = Current_pos
				# print("Before: ", weight)
				# print("Y: ", Data_Y[Current_pos]),
				# print("X: ", Data_X[Current_pos])
				# print("X * Y: ", -1 * Data_X[Current_pos])
				weight = [sum(x) for x in zip(weight, 0.5 * Y[Current_pos] * X[Current_pos])]
				#print("After: ", weight)
				UpdateCount += 1
				Current_Id = GoNext(Current_Id)
				continue

		print("Success after ", UpdateCount, " updates")
		return [weight, UpdateCount]

	else:
		PocketWeight = np.array([0.0] * 5)
		PocketErrorRate = Test(TestData_X, TestData_Y, PocketWeight)
		Success = 0
		LastFail = -1
		Current_Id = 0
		UpdateCount = 0
		while(UpdateCount < updatecount):
			Current_pos = Cycle[Current_Id]

			#Get the sign of current point
			Sign = sign(np.inner(weight, X[Current_pos]))

			#Success, if the initial line is correct
			if LastFail == -1 and Current_Id == Train_Length-1:
				if Sign == Y[Current_pos]:
					Success = 1
					continue
			#If current point is success
			if Sign == Y[Current_pos]:
				#check if it went for a full round
				if Current_pos == LastFail:
					Success = 1
					continue

				#If not, check next point
				Current_Id = GoNext(Current_Id)
				continue
			#If current point fails:
			else:
				LastFail = Current_pos
				# print("Before: ", weight)
				# print("Y: ", Data_Y[Current_pos]),
				# print("X: ", Data_X[Current_pos])
				# print("X * Y: ", -1 * Data_X[Current_pos])
				weight = [sum(x) for x in zip(weight, 0.5 * Y[Current_pos] * X[Current_pos])]
				#print("After: ", weight)

				CurrentTestErrorRate = Test(TestData_X, TestData_Y, weight)
				#print(CurrentTestErrorRate, " v.s. ", PocketErrorRate)
				if CurrentTestErrorRate < PocketErrorRate:
					PocketWeight = weight
					PocketErrorRate = Test(TestData_X, TestData_Y, PocketWeight)

				UpdateCount += 1
				Current_Id = GoNext(Current_Id)
				continue

		return weight

import random as rd

Cycle = list(range(Train_Length))

SumofErrorRate = 0
TotalIter = 2000
for iter in range(TotalIter):
	#print("Iter ", iter, ": ", end = "")
	rd.shuffle(Cycle)
	NumofUpdate = input("Limited Update: ")
	FinalWeight = PLA(Data_X, Data_Y, Cycle, NumofUpdate)
	
	#Test:
	TestErrorRate = Test(TestData_X, TestData_Y, FinalWeight)

	print("Iter ", iter, ": ", TestErrorRate)

	SumofErrorRate += TestErrorRate

AvgErrorRate = SumofErrorRate/TotalIter
print("Average Error Rate: ", AvgErrorRate)