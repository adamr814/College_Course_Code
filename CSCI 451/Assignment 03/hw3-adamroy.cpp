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
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
bool mutexLock = false;
bool endOfFile = false;

void* threadFunc1(void* inFileName_ptr){
    const char* inFilename = static_cast<const char*>(inFileName_ptr);
    std::ifstream inputFile(inFilename);
    
    if(inputFile.is_open()){
        int data;
        while(inputFile >> data){
            pthread_mutex_lock(&m);
            while(mutexLock){
                pthread_cond_wait(&cv, &m);
            }
            globalValue = data;
            mutexLock = true;
            pthread_mutex_unlock(&m);
            pthread_cond_signal(&cv);
        }
        pthread_mutex_lock(&m);
        endOfFile = true;
        pthread_mutex_unlock(&m);
        pthread_cond_signal(&cv);
        inputFile.close();
    } else {
        std::cerr << "Error: Unable to open file " << inFilename << std::endl;
    }
    return nullptr;}

void* threadFunc2(void* outFileName_ptr){
    const char* outFileName = static_cast<const char*>(outFileName_ptr);
    std::ofstream outFile(outFileName);

    //this section checks the state of the mutex and waits until the input value is passed
    if(outFile.is_open()){
        while(true){
            pthread_mutex_lock(&m);
            while(!mutexLock){
                pthread_cond_wait(&cv, &m);
            }
    /*
    From here we need to check if the global value is odd or even and print to output accordingly
    but first we need to make sure we aren't at the end of the file which causes an infinite loop (oops)
    it was causing the program to never exit because the thread was never done and constantly spinning
    */
            if(mutexLock == true){
                if(globalValue % 2 == 0){
                    outFile << globalValue << std::endl;
                    outFile << globalValue << std::endl;
                    std::cout << "hw3.out <-- " << globalValue << std::endl; //console output for testing purposes
                    std::cout << "hw3.out <-- " << globalValue << std::endl; //console output for testing purposes
                }else{ 
                    outFile << globalValue << std::endl;
                    std::cout << "hw3.out <-- " << globalValue << std::endl; //console output for testing purposes
                }

            mutexLock = false;
            pthread_cond_signal(&cv);}
            else if (endOfFile){
                pthread_mutex_unlock(&m);
                break;}
            pthread_mutex_unlock(&m);
        }
        outFile.close();
    } else {
        std::cerr << "Error: Unable to open output file" << outFileName << std::endl;}
        return nullptr;}

int main(){
//opening the hw3.out and checking if its open
std::string inFileName = "hw3.in";
std::string outFileName = "hw3.out";
std::ofstream outFile;

outFile.open(outFileName, std::ios::out);
if (!outFile.is_open()){
    std::cerr << "Error: Failed to open the output file." << std::endl;
    return 1;
}

pthread_t thread1;
pthread_t thread2;

if(pthread_create(&thread1, nullptr, threadFunc1, (void*)inFileName.c_str()) != 0){
    std::cerr << "Error: Failed to create thread 1" << std::endl;
    return 1;
}
if(pthread_create(&thread2, nullptr, threadFunc2, (void*)outFileName.c_str()) != 0){
    std::cerr << "Error: Failed to create thread 2" << std::endl;
    return 1;
}

pthread_join(thread1, nullptr);
pthread_join(thread2, nullptr);
return 0;
}