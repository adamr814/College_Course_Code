/*
Adam Roy
CSCI 451
HW3
*/

//Include statements and namespace declaration
#include <pthread.h>
#include <iostream>
#include <fstream>
#include <string>
#include <condition_variable>
#include <mutex>

//Declaring global variable and essential program dependencies
int globalValue;
std::mutex m;
std::condition_variable cv;
bool mutexLock = false;

void* threadFunc1(void* filename_ptr){
    const char* filename = static_cast<const char*>(filename_ptr);
    std::ifstream inputFile(filename);
    
    if(inputFile.is_open)){
        while(true){
            int data;
            if(inputFile >> data){
                std::unique_lock
            }
        }
    }
}

void* threadFunc2(void* arg){

}

int main(){
//opening the hw3.out and checking if its open
std::string inFileName = "hw3.in";
std::string outFileName = "hw3.out";
std::ofstream outFile;

outFile.open(outFileName, std::ios::out);
if (!outFile.is_open()){
    std::cerr << "Failed to open the output file." << std::endl;
    return 1;
}
thread thread1(threadFunc1, inFileName);

outFile.close();
return 0;
}