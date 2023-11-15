/*
Adam Roy
Program 0
CSCI 451
*/

#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <cstring>

int main() {
    key_t key = ftok(".", 'A');
    int semid = semget(key, 1, IPC_CREAT);

    if (semid == -1) {
        std::cerr << "Error: Unable to open the semaphore" << std::endl;
        return 1;
    }

    struct sembuf wait_operation = {0, -1, 0};
    semop(semid, &wait_operation, 1);

    std::cout << "Executing process #0." << std::endl;
    struct sembuf signal_operation = {0, 1, 0};
    semop(semid, &signal_operation, 1);

    return 0;
}