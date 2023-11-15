/*
Adam Roy
Program 3
CSCI 451
*/

#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>

int main(){
    key_t key = ftok(".", 'A');
    int semid = semget(key, 1, IPC_CREAT);

    if (semid == -1){
        //std::cerr << "Error: Unable to open the semaphore" << std::endl;
        return 1;
    }
    if(semctl(semid, 0, IPC_RMID) == -1){
        //std::cerr << "Error: Unable to remove the semaphore" << std::endl;
        return 1;
    }
    std::cout << "Executing process #3." << std::endl;
    return 0;
}