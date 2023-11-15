/*
Adam Roy
CSCI 451
HW5
*/


#include <iostream>
#include <pthread.h>
#include <fstream>

pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
const char* inputFiles[3] = {"hw5-1.in", "hw5-2.in", "hw5-3.in"};
const char* outputFile = "hw5.out";
const int bufferSize = 100;
char buffer[bufferSize];
int bufferIndex = 0;

void* threadFunction(void* threadID) {
    int id = *(int*)threadID;

    std::ifstream inFile(inputFiles[id]);
    if (inFile.is_open()) {
        char ch;
        while (inFile.get(ch)) {
            pthread_mutex_lock(&m);
            buffer[bufferIndex++] = ch;
            pthread_mutex_unlock(&m);
        }
        inFile.close();
    }

    return NULL;
}


int main() {
    pthread_t threads[3];
    int threadIDs[3];

    for (int i = 0; i < 3; i++) {
        threadIDs[i] = i;
    }

    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, threadFunction, &threadIDs[i]);
    }

    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }

    std::ofstream outFile(outputFile, std::ios::out);
    if (outFile.is_open()) {
        pthread_mutex_lock(&m);
        for (int i = 0; i < bufferIndex; i++) {
            outFile << buffer[i];
        }
        pthread_mutex_unlock(&m);
        outFile.close();
    }

    return 0;
}
