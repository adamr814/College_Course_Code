/*
Adam Roy
CSCI 451
HW2
*/

//Include statements and namespace declaration
#include <iostream>
#include <stdlib.h>
#include <pthread.h>
#include <fstream>
#include <cstring>
using namespace std;

//Declaring global variables
#define NUM_THREADS 2
const char* wordToFind1 = "easy";
const char* wordToFind2 = "polar";
int wordCount1 = 0;
int wordCount2 = 0;
pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER;


void* worker1(void* arg) {
    char* threadData = (char*)arg;
    char* dataCopy = strdup(threadData);
    char* token = strtok(dataCopy, " ");
    while(token != nullptr){
        if (strcmp(token, wordToFind1) == 0){
            pthread_mutex_lock(&mutex1);
            wordCount1++;
            pthread_mutex_unlock(&mutex1);
        }
        token = strtok(nullptr, " ");
    }
    free(dataCopy);
    pthread_exit(nullptr);
}

void* worker2(void* arg) {
    char* threadData = (char*)arg;
    char* dataCopy = strdup(threadData);
    char* token = strtok(dataCopy, " ");
    while(token != nullptr){
        if (strcmp(token, wordToFind2) == 0){
            pthread_mutex_lock(&mutex2);
            wordCount2++;
            pthread_mutex_unlock(&mutex2);
        }
        token = strtok(nullptr, " ");
    }
    free(dataCopy);
    pthread_exit(nullptr);
}

int main() {
    //Declaring constants, the url to download and what to name the file
    const char* url = "http://undcemcs01.und.edu/~ronald.marsh/CLASS/CS451/hw3-data.txt";
    const char* filename = "download.txt";

    //Downloading the file from the url and checking if it was downloaded properly (or at all) else exit
    string wgetCmd = "wget -q -O " + string(filename) + " " + url;
    int fileCheck = system(wgetCmd.c_str());
    if(fileCheck != 0) {
        cerr << "Failed to download the file" << endl;
        return 1;
    }

    //Opening the file with read/write access and checking if it opens properly else exit
    ifstream inputFile(filename, ios::binary);
    if (!inputFile.is_open()){
        cerr << "Failed to open the downloaded file" << endl;
        return 1;
    }

    //Gets the size of the file in order to allocate the proper amount of memory
    inputFile.seekg(0, ios::end);
    streampos fileSize = inputFile.tellg();
    inputFile.seekg(0, ios::beg);

    if(fileSize < 0){
        cerr << "Failed to determine the file size" << endl;
    }

    //Allocates the space in memory for the file and then places the file into an array before closing the input file
    char* fileData = new char[fileSize];
    inputFile.read(fileData, fileSize);
    inputFile.close();

//This is the point in which threads are created and stuff starts to get weird

    //Create the threads and indicate what worker function to use and what data to use
    pthread_t threads[NUM_THREADS];

    for(int i = 0; i < NUM_THREADS; i++){
        pthread_create(&threads[i], nullptr, worker1, (void*)fileData);
    }
    for(int i = 0; i < NUM_THREADS; i++){
        pthread_join(threads[i], nullptr);
    }

    for(int i = 0; i < NUM_THREADS; i++){
        pthread_create(&threads[i], nullptr, worker2, (void*)fileData);
    }
    for(int i = 0; i < NUM_THREADS; i++){
        pthread_join(threads[i], nullptr);
    }

    cout << "Occurrences of '" << wordToFind1 << "': " << wordCount1 << endl;
    cout << "Occurrences of '" << wordToFind2 << "': " << wordCount2 << endl;

    pthread_mutex_destroy(&mutex1);
    pthread_mutex_destroy(&mutex2);

    //Cleaning up files and freeing up memory
    delete[] fileData;
    system("unlink download.txt");
    return 0;
}