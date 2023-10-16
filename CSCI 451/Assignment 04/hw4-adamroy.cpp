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
int NUM_THREADS = 5;
int threads_done = 0;

//Thread Function
void* threadFunc(void* arg){
    std::string inFileName = static_cast<const char*>(arg);
    std::ifstream inFile(inFileName);
    if(!inFile.is_open()){
        pthread_t threadID = pthread_self();
        pthread_mutex_lock(&m);
        std::cerr << threadID << " failed to open " << inFileName << std::endl;
        pthread_mutex_unlock(&m);
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
    //usleep(1000000);
    std::cout << "The balance after " << threadID << "completed: $" << globalBalance << std::endl;
    return NULL;
}

int main(){
    for(int i = 0; i < NUM_THREADS; i++){
        std::string filename = "data" + std::to_string(i) + ".in";
        //std::string* filename_ptr = new std::string(filename);
        pthread_t thread[i];
        if(pthread_create(&thread[i], NULL, threadReader, (void*)&filename) != 0){
            pthread_t threadID = pthread_self();
            pthread_mutex_lock(&m);
            std::cerr << "Error: Failed to create thread with ID: " << threadID << std::endl;
            pthread_mutex_lock(&m);
            return 1;
        }
    }
}
