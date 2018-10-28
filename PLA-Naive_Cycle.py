Data_X = []
Data_Y = []
Length = 0

#Read Data
Train_Data = input("Train data file:")
f = open(Train_Data, "r")
if f.mode == "r":
	fl = f.readlines()
	for line in fl:
		Length += 1
		Data = line.split()
		Data_X.append([1.0] + [float(i) for i in Data[0:4]])
		Data_Y.append(int(Data[4]))
f.close()


import numpy as np

Data_X = np.array(Data_X)
Data_Y = np.array(Data_Y)

def GoNext(Pos):
	if Pos < Length-1:
		Pos += 1
	else:
		Pos = 0
	return Pos

def sign(x):
	return -1 if x <= 0 else 1

Cycle = list(range(Length))

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
				weight = [sum(x) for x in zip(weight, Y[Current_pos] * X[Current_pos])]
				#print("After: ", weight)
				UpdateCount += 1
				Current_Id = GoNext(Current_Id)
				continue

		print("Success after ", UpdateCount, " updates")
		return [weight, UpdateCount]

	else:
		Success = 0
		LastFail = -1
		Current_Id = 0
		UpdateCount = 0
		while(UpdateCount < updatecount):
			Current_pos = Cycle[Current_Id]

			#Get the sign of current point
			Sign = sign(np.inner(weight, X[Current_pos]))

			#Success, if the initial line is correct
			if LastFail == -1 and Current_Id == Length-1:
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
				weight = [sum(x) for x in zip(weight, Y[Current_pos] * X[Current_pos])]
				#print("After: ", weight)
				UpdateCount += 1
				Current_Id = GoNext(Current_Id)
				continue

		return weight

Finalweight = PLA(Data_X, Data_Y, Cycle, -1)[0]

#Test:
for i in range(Length):
	if sign(np.inner(Finalweight, Data_X[i])) != Data_Y[i]:
		print("Fuck")