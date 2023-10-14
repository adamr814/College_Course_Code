/*
Adam Roy
CSCI 451
HW4
*/

//include statements
#include <iostream>
#include <pthread.h>
#include <fstream>

//Declaring global variables an program dependencies
int globalBalance = 0;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
