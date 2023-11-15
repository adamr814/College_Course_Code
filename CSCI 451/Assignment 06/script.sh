#!/bin/bash

# Compile the programs
g++ program0.cpp -o program0
g++ program1.cpp -o program1
g++ program2.cpp -o program2
g++ program3.cpp -o program3

# Execute the programs in a random order
./program$((0))
./program$((2))
./program$((1))
./program$((2))
./program$((3))
./program$((2))
./program$((1))