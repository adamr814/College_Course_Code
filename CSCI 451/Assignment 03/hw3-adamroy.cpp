/*
Adam Roy
CSCI 451
HW3
*/

//Include statements and namespace declaration
#include <pthread.h>
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

//Declaring global variables
#define NUM_THREADS 2
#define outFileName "hw3.out"
int inInt = 0;

void* threadFunc1(void* arg){

}

void* threadFunc2(void* arg){

}

int main(){
//opening the hw3.out and checking if its open
ofstream outFile;
outFile.open(outFileName, ios::out);
if (!outFile.is_open()){
    cerr << "Failed to open the output file." << endl;
    return 1;
}

outFile.close();
return 0;
}