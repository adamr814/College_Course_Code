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
    //pthread_t threadID = pthread_self();
    pthread_detach(pthread_self());
    std::string inFileName = static_cast<const char*>(arg);
    std::ifstream inFile(inFileName);
    if(!inFile.is_open()){
        pthread_mutex_lock(&m);
        std::cerr << pthread_self() << " failed to open " << inFileName << std::endl;
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
    std::cout << "The balance after " << pthread_self() << " completed: $" << globalBalance << std::endl;
    return NULL;
}

int main(){
    pthread_t threads[5];
    const char* filenames[5] = {"data1.in", "data2.in", "data3.in", "data4.in", "data5.in"};

    for (int i=0; i < 5; i++){
        pthread_create(&threads[i], nullptr, threadFunc, (void*)filenames[i]);
        usleep(20000); //See Note
    }

    return 0;
}

/*
I have noticed with the use of a delay my OS uses the same thread because it
executes the thread function very quickly and presumably to save on resources
it just spawns the same thread again but when decreasing the delay I could get
it to use multiple threads so it does work properly. Maybe I will make the input
files huge so it takes awhile to process it all... (did it with filesize 10000 on
the fourth data.in and that was the only one that needed a new thread)
*/