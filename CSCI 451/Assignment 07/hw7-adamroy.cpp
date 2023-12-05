/*
Adam Roy
CSCI 451
Assignment 07 - Grandpa
*/

//include statements
#include <iostream>
#include <sys/wait.h>
#include <semaphore.h>
#include <unistd.h>
#include <fstream>
#include <sys/ipc.h>
#include <sys/shm.h>

//main program
int main(int argc, char *argv[]){
    if (argc < 2){
        std::cerr << "Usage: " << argv[0] << " <filename>" << std::endl;
        return 1;
    }
    const char* filename = argv[1];
    std::cout << "Using file: " << filename << std::endl;

    sem_unlink("_sem");
    //Initialize the semaphore
    sem_t* semaphore = sem_open("_sem", O_CREAT, 0666, 1);
    if(semaphore == SEM_FAILED){
        std::cerr << "Error with semaphore" << std::endl;
        return 0;
    }

    //section to generate shared memory
    key_t key = ftok(".", 'M');
    int shmid = shmget(key, sizeof(int), IPC_CREAT | 0666);
    int *sharedCounter = (int *)shmat(shmid, nullptr, 0);
    *sharedCounter = 0;

    //Creates an array of pipes
    int pipe_fds[9][2];

    for (int i = 0; i < 9; ++i){        
        if (pipe(pipe_fds[i]) == -1){
            std::cerr << "Error creating pipe" << std::endl;
            sem_close(semaphore);
            sem_unlink("_sem");
            return 1;
        }
    }

    //Forks the grandchild program
    for (int i = 1; i <= 9; ++i) {
        pid_t pid = fork();

        if (pid == -1){
            std::cerr << "Fork error" << std::endl;
            sem_close(semaphore);
            sem_unlink("_sem");
            return 1;
        }
        else if (pid == 0){
            char indexString[2], shmidString[10];
            snprintf(indexString, sizeof(indexString), "%d", i);
            snprintf(shmidString, sizeof(shmidString), "%d", shmid);
            close(pipe_fds[i - 1][0]);
            execlp("./p", "./p", filename, "_sem", indexString, shmidString, nullptr);
            
            std::cerr << "Execution error" << std::endl;
            sem_close(semaphore);
            sem_unlink("_sem");
            return 1;
        } else {
            waitpid(pid, nullptr, 0);
        }
    }
    
    for (int i = 0; i < 9; ++i){
        close(pipe_fds[i][1]);
    }

    //Read data from child process
    char buffer[15];
    ssize_t bytesRead;

    std::ofstream outfile("hw7.out", std::ios::app);
    if(!outfile.is_open()){
        std::cerr << "Error opening outfile" << std::endl;
        return 1;
    }

    for (int i = 0; i < 9; ++i){
        while ((bytesRead = read(pipe_fds[i][0], buffer, sizeof(buffer))) > 0) {
            sem_wait(semaphore);
            outfile << buffer << std::endl;
            sem_post(semaphore);        
        }
    }
    outfile << *sharedCounter;
    outfile.close();

    for (int i = 1; i <= 9; ++i){
        wait(nullptr);
    }
    sem_close(semaphore);
    sem_unlink("_sem");
    shmdt(sharedCounter);
    shmctl(shmid, IPC_RMID, nullptr);
    return 0;
}