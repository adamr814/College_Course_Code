#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
int  i, j, sign, amount;
char filename[10];
int  filesize;
FILE *stream;
    printf("Enter file size: ");
    scanf("%d", &filesize);
    printf("Enter file name: ");
    scanf("%s", &filename);

    stream = fopen(filename, "w");
    for (j = 0; j < filesize; j++) {
        fprintf(stream, "R\n");
        for (i = 0; i < (rand()%100); i++) {
            sign   = rand()%2;
            amount = rand()%1000;
            if (sign == 0) fprintf(stream, "%c%d\n", '-', amount);
                      else fprintf(stream, "%c%d\n", '+', amount);
        }
        fprintf(stream, "W\n");
    }
    fclose(stream);
    return 0;
}