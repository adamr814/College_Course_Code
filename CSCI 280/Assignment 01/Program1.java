/*
CSCI280
Adam Roy
Program: 1
Due: Jan 25th 2023
*/

import java.util.Scanner;

public class Program1{
    public static void sumNum(int value){
        int sum = 0;
        for(int i=value; i<=(value+20); i++){
            sum += i;}
        System.out.println("Total: " + sum);}
    
    public static void main(String[] args){
        Scanner keyboard;
        keyboard = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int valid = 0;
        while(valid != 1){
            int value = keyboard.nextInt();    
            if(value >= 0){
                System.out.println("\nSelected Integer: " + value);
                valid = 1;
                sumNum(value);}  
            else{
                System.out.println("\n* * * * * * * * * * * * * * * * * * * * * * * *\n" +
                "Invalid Input Please Enter A Positive Integer\n" +
                "* * * * * * * * * * * * * * * * * * * * * * * *\n");
                System.out.print("Enter an integer: ");}} keyboard.close();}}