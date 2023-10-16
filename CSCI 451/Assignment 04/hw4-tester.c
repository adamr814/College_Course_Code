#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
1 Balance: 2910
2 Balance: 5492
3 Balance: 4889
4 Balance: 4583
End Balance: 5436
*/

int main(void) {
char input[43];
int  amount, balance = 0;
FILE *stream;
     stream = fopen("data1.in", "r");
     amount = 0;
     while (1) {
      fscanf(stream, "%s", input);
 //     if (input[0] == 'R') printf("Lock\n");
      if (feof(stream)) break;
      while (1) {
         fscanf(stream, "%s", input);
         if (input[0] == 'W') {
//            printf("Unlock\n");
            break;
         }
         amount += atoi(input);
       }
 //      printf("Amount %d\n", amount);
     }
     balance += amount;
     printf("Balance 1: %d\n", balance);
     fclose(stream);
     
     stream = fopen("data2.in", "r");
     amount = 0;
     while (1) {
      fscanf(stream, "%s", input);
 //     if (input[0] == 'R') printf("Lock\n");
      if (feof(stream)) break;
      while (1) {
         fscanf(stream, "%s", input);
         if (input[0] == 'W') {
//            printf("Unlock\n");
            break;
         }
         amount += atoi(input);
       }
//       printf("Amount %d\n", amount);
     }
     balance += amount;
     printf("Balance 2: %d\n", balance);
     fclose(stream);

     stream = fopen("data3.in", "r");
     amount = 0;
     while (1) {
      fscanf(stream, "%s", input);
 //     if (input[0] == 'R') printf("Lock\n");
      if (feof(stream)) break;
      while (1) {
         fscanf(stream, "%s", input);
         if (input[0] == 'W') {
//            printf("Unlock\n");
            break;
         }
         amount += atoi(input);
       }
 //      printf("Amount %d\n", amount);
     }
     balance += amount;
     printf("Balance 3: %d\n", balance);
     fclose(stream);

     stream = fopen("data4.in", "r");
     amount = 0;
     while (1) {
      fscanf(stream, "%s", input);
 //     if (input[0] == 'R') printf("Lock\n");
      if (feof(stream)) break;
      while (1) {
         fscanf(stream, "%s", input);
         if (input[0] == 'W') {
//            printf("Unlock\n");
            break;
         }
         amount += atoi(input);
       }
//       printf("Amount %d\n", amount);
     }
     balance += amount;
     printf("Balance 4: %d\n", balance);
     fclose(stream);

     stream = fopen("data5.in", "r");
     amount = 0;
     while (1) {
      fscanf(stream, "%s", input);
 //     if (input[0] == 'R') printf("Lock\n");
      if (feof(stream)) break;
      while (1) {
         fscanf(stream, "%s", input);
         if (input[0] == 'W') {
//            printf("Unlock\n");
            break;
         }
         amount += atoi(input);
       }
//       printf("Amount %d\n", amount);
     }
     balance += amount;
     printf("End Balance: %d\n", balance);
     fclose(stream);
     return 0;
}
