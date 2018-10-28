# Perceptron Learning Algorithm
A practie of PLA.

## How to run

Start the program
```
python PLA.py
```

Input the Training data file name
```
Train data file: *INPUT HERE*
```

The program will run PLA on the given data 1126 time, 
and output the average number of updates, 
also with a plot of number of updates v.s. frequency.

## Versions

There are some different implementation to toy around

### PLA.py

This only works with linear-seperable data, else it will not halt.
It runs through the data set in a pre-determined random cycle.

### PLA.m

The matlab version of PLA.py
Run this with matlab:
```
PLA(Train_data_file)
```

### PLA-Naive_Cycle.py

This runs through the data set with the naive cycle(in order).
This also only works with linear-seperable data, else it will not halt.

### PLA-Random_Cycle.py

Basically same as PLA.py

### PLA-Limited_Updates.py

This runs PLA with limited updates.
It will halt after a desired number of updates.
This works withnon-linear-seperable data.

### PLA-Pocket_Algorithm.py

This runs PLA with the pocket algorithm, 
which means that it will record the best result throughout the process, 
and output the best one in a limited time of update.
This works with non-linear-seperable data.

## Built With

* Python 3.6.0 :: Anaconda custom (64-bit)

## Authors

* **SaKaTetsu** - *Initial work* - [SaKaTetsu](https://github.com/SaKaTetsu)
