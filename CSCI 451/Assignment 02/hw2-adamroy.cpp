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

/*const char* wordToFind1 = "easy";
const char* wordToFind2 = "polar";
int wordCount1 = 0;
int wordCount2 = 0*/


void* worker1(void* arg) {
    char* text = (char*)arg; //i think this is the problem.
    cout << arg << endl;
    string wordToFind = "easy";
    int wordLength = wordToFind.length();
    int count1 = 0;
    for(int i = 0; text[i] != '\0'; i++){
        int j;
        for(j = 0; j < wordLength; j++){
            if(text[i + j] != wordToFind[j]){
                break;
            }
        }
        if(j == wordLength){
            count1 ++;
        }
    }
    cout << "Thread " << pthread_self() << ": Word Occurrences = " << count1 << endl;
    pthread_exit(NULL);
}

void* worker2(void* arg) {
    char* text = (char*)arg;
    string wordToFind = "polar";
    int wordLength = wordToFind.length();
    int count2 = 0;
    for(int i = 0; text[i] != '\0'; i++){
        int j;
        for(j = 0; j < wordLength; j++){
            if(text[i + j] != wordToFind[j]){
                break;
            }
        }
        if(j == wordLength){
            count2 ++;
        }
    }
    cout << "Thread " << pthread_self() << ": Word Occurrences = " << count2 << endl;
    pthread_exit(NULL);
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
//test point
    //cout << fileSize << endl;
//end
    if(fileSize < 0){
        cerr << "Failed to determine the file size" << endl;
    }

    //Allocates the space in memory for the file and then places the file into an array before closing the input file
    char* fileData = new char[fileSize];
    inputFile.read(fileData, fileSize);
    inputFile.close();
//test point
    //for(int i = 0; fileData[i] != '\0'; i++){
        //cout << fileData[i];}
//end
    //Create the threads and indicate what worker function to use and what data to use
    pthread_t thread1, thread2;
    int result1 = pthread_create(&thread1, 0, worker1, (void*)&fileData);
    if (result1 != 0){
        cerr << "Thread creation failed" << endl;
    }
    int result2 = pthread_create(&thread2, 0, worker2, (void*)&fileData);
    if(result2 != 0){
        cerr << "Thread creation failed" << endl;
    }

    //Wait for all of the threads to complete their tasks before moving on
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    //Cleaning up files and freeing up memory
    delete[] fileData;
    //system("unlink download.txt");
    return 0;
}