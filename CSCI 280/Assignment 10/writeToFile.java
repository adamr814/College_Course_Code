/*
 * Adam Roy
 * CSCI 280
 * Short Assignment 10
 */

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Scanner;

class writeToFile{
    public static void main(String args[]){
        Scanner kb = new Scanner(System.in);
        try{
            FileOutputStream fOut = new FileOutputStream("Output.txt");
            System.out.print("Enter a line of text\n-> ");
            String l = kb.nextLine();
            String nl = "\n";
            byte[] b = l.getBytes();
            byte[] n = nl.getBytes();
            fOut.write(b);
            fOut.write(n);
            System.out.print("Enter a line of text\n-> ");
            l = kb.nextLine();
            b = l.getBytes();
            fOut.write(b);
            fOut.close();
        } catch(Exception e){System.out.println("Error writing to file -> " + e);}
        try{
            FileInputStream fIn = new FileInputStream("Output.txt");
            int x;
            while((x = fIn.read()) != -1){
                byte b = (byte) x;
                System.out.print((char) b);}
            fIn.close();
        } catch(Exception e){System.out.println("Error reading from input file -> " + e);}}
    }