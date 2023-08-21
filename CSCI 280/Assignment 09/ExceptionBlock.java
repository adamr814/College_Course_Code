/*
 * Adam Roy
 * CSCI 280
 * Short Assignment 9
 */

import java.util.Scanner;

public class ExceptionBlock{
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        System.out.println("Enter two integer values");
        int eCounter = 0;
        while(true){
            try{
                int x = getNums();
                System.out.println("The sum is " + x + " after " + eCounter + " error(s) were entered.");
                break;} 
            catch(Exception e){
                System.out.print("\n****  Invalid values entered  ****\n\n");
                eCounter++;}}}

    public static int getNums(){
        Scanner kb = new Scanner(System.in);
        int a=0;
        int b=0;
        System.out.print("Enter first number : ");
        a = kb.nextInt();
        System.out.print("Enter second number: ");
        b = kb.nextInt();
        int sum = a + b;
        kb.close();
        return sum;}}
    
    
    
    /*public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        System.out.println("Enter two integer values");
        int eCount=0;
        int a = 0;
        int b = 0;
        while(true){
            try{
                System.out.print("Enter first number : ");
                a = Integer.parseInt(kb.nextLine());
                break;} 
            catch(Exception e){
                System.out.print("\n****  Invalid value entered  ****\n\n");
                eCount++;}}
        while(true){
            try{
                System.out.print("Enter second number: ");
                b = Integer.parseInt(kb.nextLine());
                break;} 
            catch(Exception e){
                System.out.print("\n****  Invalid value entered  ****\n\n");
                eCount++;}}
        int sum = a + b;
        System.out.println("The sum is " + sum + " after " + eCount + " error(s) were entered.");
        kb.close();}}*/