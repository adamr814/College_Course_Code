/*
Adam Roy
CSCI 451
HW3
*/

//Include statements and namespace declaration
#include <pthread.h>
#include <iostream>
#include <fstream>
#include <mutex>

//Declaring global variable and essential program dependencies
int globalValue;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cv = PTHREAD_COND_INITIALIZER;
bool mutexLock = false;

void* threadFunc1(void* inFileName_ptr){
    const char* inFilename = static_cast<const char*>(inFileName_ptr);
    std::ifstream inputFile(inFilename);
    
    if(!inputFile.is_open()){
        std::cerr << "Error: Unable to open file " << inFilename << std::endl;
        return nullptr;}
        
    int data;
    while(inputFile >> data){
        pthread_mutex_lock(&m);
        while(mutexLock){
            pthread_cond_wait(&cv, &m);}

            globalValue = data;
            mutexLock = true;
            pthread_mutex_unlock(&m);
            pthread_cond_signal(&cv);}

    inputFile.close();

    pthread_mutex_lock(&m); //P2
    globalValue = -1;
    mutexLock = true;
    pthread_mutex_unlock(&m);
    pthread_cond_signal(&cv);
    return nullptr;}

void* threadFunc2(void* outFileName_ptr){
    const char* outFileName = static_cast<const char*>(outFileName_ptr);
    std::ofstream outFile(outFileName);

    if(!outFile.is_open()){
        std::cerr << "Error: Unable to open output file" << outFileName << std::endl;
        return nullptr;}

    while(true){
        pthread_mutex_lock(&m);
        while(!mutexLock){
            pthread_cond_wait(&cv, &m);}

        if(globalValue == -1){ //P1
            pthread_mutex_unlock(&m);
            break;}

        if(globalValue % 2 == 0){
            outFile << globalValue << std::endl;
            outFile << globalValue << std::endl;
            std::cout << "hw3.out <-- " << globalValue << std::endl;
            std::cout << "hw3.out <-- " << globalValue << std::endl;}
        else{ 
            outFile << globalValue << std::endl;
            std::cout << "hw3.out <-- " << globalValue << std::endl;}

            mutexLock = false;
            pthread_mutex_unlock(&m);
            pthread_cond_signal(&cv);}

    outFile.close();
    return nullptr;}

int main(){
//opening the hw3.out and checking if its open
std::string inFileName = "hw3.in";
std::string outFileName = "hw3.out";
std::ofstream outFile;

pthread_t thread1;
pthread_t thread2;

if(pthread_create(&thread1, nullptr, threadFunc1, (void*)inFileName.c_str()) != 0){
    std::cerr << "Error: Failed to create thread 1" << std::endl;
    return 1;}

if(pthread_create(&thread2, nullptr, threadFunc2, (void*)outFileName.c_str()) != 0){
    std::cerr << "Error: Failed to create thread 2" << std::endl;
    return 1;}

pthread_join(thread1, nullptr);
pthread_join(thread2, nullptr);
return 0;
}

/*
Problems and solutions

P1:
this was the main problem earlier and I overlooked it, essentially when checking for the
end of the file (non-recursively) the thread would never enter the case where it could finish
its task therefore it was stuck in a loop looking for -1 which never came since thread 1 was
done passing values to thread 2 so the thread could never exit and the main function could
never return 0 exiting the program. - This was fixed by placing the check for -1 at the top
of the while loop which meant that unless -1 was seen it would continue to loop and search
for data instead of just getting to the EOF loop with no -1 and jumping into the infinite state

P2:
This was another large problem, a version of the code exists where the program would execute
properly but it would only output the second to last number and never the last number. essentially
what was happening is before it was sending the last number to the T2 it would instead send the EOF
and never print the last number. - This was solved by moving the set global to -1 to the very end
of the thread function making sure it was the last thing the function did after it had no more data
instead of breaking out of the loop if it found a EOF.
*/