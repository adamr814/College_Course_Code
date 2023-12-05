/*
Adam Roy
CSCI 451
Assignment 07 - Grandchild
*/
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <fcntl.h>
#include <fstream>
#include <semaphore.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main(int argc, char *argv[]){
    const char* filename = argv[1];
    const char* semName = argv[2];
    int index = std::atoi(argv[3]);
    int shmid = std::atoi(argv[4]);
    int pipe_fd = std::atoi(argv[5]);
    
    int *sharedCounter = (int *)shmat(shmid, nullptr, 0);
    sem_t* semaphore = sem_open(semName, O_RDONLY);
    sem_wait(semaphore);

    std::ifstream inputFile(filename);
    if(!inputFile){
        std::cerr << "Error opening input file" << std::endl;
        sem_post(semaphore);
        return 1;
    }

    /*int pipe_fd;
    if (sscanf(argv[4], "%d", &pipe_fd) != 1){
        std::cerr << "Error reading pipe descriptor" << std::endl;
        sem_post(semaphore);
        return 1;
    }*/

    //dup2(pipe_fd, STDERR_FILENO);

    //int offset = 0;

    while(!inputFile.eof()){
        int n = rand() % 10 + 1;
        *sharedCounter += n;
        char buffer[11];
        inputFile.read(buffer, n);

        if(inputFile.eof()){
            break;
        }
        else {
            buffer[inputFile.gcount()] = '\0'; 
            std::string grandchildName = "_p" + std::to_string(index);
            //std::cout << grandchildName << buffer << std::endl;
            write(pipe_fd, buffer, inputFile.gcount());
            //offset += inputFile.gcount();
        }
    }
    //dup2(STDERR_FILENO, STDERR_FILENO);
    sem_post(semaphore);
    return 0;
}