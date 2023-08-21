//Adam Roy
//CSCI 330
//HW11

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct graphNode{
char listA[10][100];
int listB[10];};

struct listNode{
char name[42];
struct listNode *next;
struct listNode *prev;
struct graphNode *self;};
struct listNode *head, *tail;
typedef struct listNode link;
long int totalCost;
int traversals;
time_t timeVal;

void makeLinkedList(char currentName[42], char dest[42], int cost){
        int i;
        struct listNode *current = head;
        while(current != NULL){
                if(!strcmp(current->name, currentName)){
                        for(i=0; i<10; i++){
                                if(!strcmp(current->self->listA[i], "")){
                                        strcpy(current->self->listA[i], dest);
                                        current->self->listB[i] = cost;
                                        break;}}}
                current = current -> next;}}

void insert(char insertPlace[42]){
        struct listNode *current = (struct listNode *)malloc(sizeof(struct listNode));
        struct graphNode *dest = (struct graphNode *)malloc(sizeof(struct graphNode));
        current -> self = dest;
        strcpy(current -> name, insertPlace);
        if(head == NULL){
                head = tail = current;
                current -> next = current -> prev = NULL;}
        else{
                struct listNode *temp = head;
                while(temp != NULL){
                        if(strcmp(current->name, temp->name) <= 0){
                                if(temp == head){
                                        current->next = head;
                                        current->prev = NULL;
                                        head->prev = current;
                                        head = current;
                                        break;}
                                else{
                                        current->prev = temp->prev;
                                        temp->prev->next = current;
                                        temp->prev = current;
                                        current->next = temp;
                                        break;}}
                        if(temp == tail){
                                tail -> next = current;
                                current -> prev = tail;
                                tail = current;
                                break;}
                        else{temp = temp->next;}}}}

int drunkardTraversal(char start[42]){
        int count = 0;
        if(!strcmp(start, "Home")){
                return 1;}
        else if(traversals == 10000){
                return 0;}
        else{
                traversals++;
                char dest[100];
                struct listNode *current = head;
                while(current != NULL){
                        if(!strcmp(current->name, start)){break;}
                        else{current = current->next;}}
                int i = rand()%10;
                while(!strcmp(current->self->listA[i], ""))
                {i = rand()%10;}
                        count++;
                        if (count == 1000)
                        {return 0;}
                totalCost += current->self->listB[i];
                drunkardTraversal(current->self->listA[i]);}}

void freeFunc(void){
        struct listNode *temp = head;
        while(temp -> next != NULL){
                temp = temp -> next;
                free(head->self);
                free(head);
                head = temp;}}

int main(void){
        totalCost = 0;
        traversals = 0;
        timeVal = time(NULL);
        srand(timeVal);
        head = NULL;
        tail = NULL;
        char fname[42], dest[42], start[100];
        int fcost;
        FILE *dataFile;
        dataFile = fopen("./hw11.data", "r");
        if (dataFile == NULL){exit(0);}
        while(fscanf(dataFile, "%s", fname) != EOF){
                if(!strcmp(fname, "STOP")){break;}
                else{insert(fname);}}
        while(fscanf(dataFile, "%s %s %d", fname, dest, &fcost) != EOF){
                if(!strcmp(fname, "STOP")){break;}
                else{makeLinkedList(fname, dest, fcost);}}
        fscanf(dataFile, "%s", start);
        int x = drunkardTraversal(start);
        if(x!=0){printf("\nStarting location: %s\nMade it home, it cost %ld steps\n\n", start, totalCost);}
        else{printf("Didn't make it home\n");}
        fclose(dataFile);
        freeFunc();}