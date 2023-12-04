CC = g++
CFLAGS = -Wall -std=c++11

all: grandpa grandchild

grandpa: hw7-adamroy.cpp
	$(CC) $(CFLAGS) -o grandpa hw7-adamroy.cpp

grandchild: p.cpp
	$(CC) $(CFLAGS) -o p p.cpp

clean:
	rm -f grandpa p