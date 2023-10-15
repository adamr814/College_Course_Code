/*
Adam Roy
CSCI 451
HW4
*/

//include statements
#include <iostream>
#include <pthread.h>
#include <fstream>
#include <string>
#include <vector>
#include <unistd.h>

//Declaring global variables an program dependencies
int globalBalance = 0;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
#define NUM_THREADS 5
int threads_done = 0;

//Thread Function
void* threadReader(void* arg){
    std::string inFileName = static_cast<const char*>(arg);
    std::ifstream inFile(inFileName);
    if(!inFile.is_open()){
        pthread_t threadID = pthread_self();
        std::cerr << threadID << " failed to open " << inFileName << std::endl;
        return NULL;
    }

    std::string line;
    while(std::getline(inFile, line)){
        if(line == "R"){
            pthread_mutex_lock(&m);
        }
        else if(line == "W"){
            pthread_mutex_unlock(&m);
        }
        else if(line[0] == '+' || line [0] == '-'){
            int value = std::stoi(line.substr(1));
            if (line[0] == '+'){
                globalBalance += value;
            }
            else {
                globalBalance -= value;
            }
        }
    }
    pthread_detach(pthread_self());
    pthread_t threadID = pthread_self();
    usleep(1000000);
    std::cout << "The balance after " << threadID << "completed: $" << globalBalance << std::endl;
    return NULL;
}

int main(){
    for(int i = 0; i < NUM_THREADS; i++){
        std::string filename
        pthread_t thread[i];
        if(pthread_create(&thread[i], nullptr, threadReader, (void*)(&filename).c_str()) != 0){
            pthread_t threadID = pthread_self();
            std::cerr << "Error: Failed to create thread with ID: " << threadID << std::endl;
            return 1;
        }
    }
}
