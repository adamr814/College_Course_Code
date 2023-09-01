/*
Adam Roy
CSCI 451
HW 1
*/

//Include Statements: Including iostream for display output and stdlib.h for wget and grep.
#include <iostream>
#include <stdlib.h>
using namespace std;

//Main function: contains the link to crawl and the recursive function to grep and output findings.
int main(){
    system("wget -q http://undcemcs01.und.edu/~ronald.marsh/PROJECTS/PROJECTS.HTML");
    system("grep -v -E '(<|BGCOLOR|LINK|VLINK|ALINK|BACKGROUND|Movies|Games|Items|Last|2/4/2020)' *.HTML");
    system("unlink *.HTML");
    cout << "Successfully Unlinked File\n";
    return 0;}