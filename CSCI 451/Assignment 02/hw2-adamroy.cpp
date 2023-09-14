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
#define NUM_THREADS 2 //****** This is problematic with compilers please read note at bottom ******
const char* wordToFind1 = "easy";
const char* wordToFind2 = "polar";
int wordCount1 = 0;
int wordCount2 = 0;

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER;


void* worker(void* arg) {
    char* threadData = (char*)arg;
    char* token = strtok(threadData, " ");
    while(token != nullptr){
        if (strcmp(token, wordToFind1) == 0){
            pthread_mutex_lock(&mutex1);
            wordCount1++;
            pthread_mutex_unlock(&mutex1);
        }
        else if (strcmp(token, wordToFind2) == 0){
            pthread_mutex_lock(&mutex2);
            wordCount2++;
            pthread_mutex_unlock(&mutex2);
        }
        token = strtok(nullptr, " ");
    }
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
        pthread_create(&threads[i], nullptr, worker, (void*)fileData);
    }
    for(int i = 0; i < NUM_THREADS; i++){
        pthread_join(threads[i], nullptr);
    }

    cout << "Occurrences of the word '" << wordToFind1 << "' : " << wordCount1 << endl;
    cout << "Occurrences of the word '" << wordToFind2 << "': " << wordCount2 << endl;

    pthread_mutex_destroy(&mutex1);
    pthread_mutex_destroy(&mutex2);

    //Cleaning up files and freeing up memory
    delete[] fileData;
    system("unlink download.txt");
    return 0;
}
/*
Known bugs:

    Sometimes when changing the value of NUM_THREADS it messes up the count
    I believe that it has something to do with the compiler overwriting the
    compiled file but if compiled again it usually fixes it. I have tested
    1-5 threads and 800 threads and all output the right amount of words
    in the count but immediately after compiling it gives numbers that are
    off (SOMETIMES) kinda weird...
*/