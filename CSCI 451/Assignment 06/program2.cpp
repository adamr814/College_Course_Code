/*
Adam Roy
Program 2
CSCI 451
*/

#include <iostream>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>

int main() {
    key_t key = ftok(".", 'A');
    int semid = semget(key, 1, IPC_CREAT);

    if (semid == -1) {
        //std::cerr << "Error: Unable to open the semaphore" << std::endl;
        return 1;
    }
    struct sembuf sops = {0, 1, 0};
    if (semop(semid, &sops, 1) == -1) {
        //std::cerr << "Error: Unable to increment the semaphore" << std::endl;
        return 1;
    }
    std::cout << "Executing process #2." << std::endl;
    usleep(500000);

    return 0;
}