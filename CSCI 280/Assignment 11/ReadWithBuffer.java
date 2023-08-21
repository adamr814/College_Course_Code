/*
 * Adam Roy
 * CSCI 280
 * Short Assignment 11
 */

import java.io.*;
import java.util.Scanner;


public class ReadWithBuffer{
    public static void main(String args[]) throws Exception{
        FileReader fRead = new FileReader("input.txt");
        BufferedReader bRead = new BufferedReader(fRead);
        String inStr = bRead.readLine();
        bRead.close();

        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter A string\n-> ");
        String kbStr = kb.readLine();
        System.out.print("The string you entered\n-> " + kbStr + "\n\n");

        StringReader sRead = new StringReader(inStr);
        int i;
        while((i=sRead.read()) != -1){
            System.out.println((char)i);}

        FileWriter fWrite = new FileWriter("output.txt");
        PrintWriter pWrite = new PrintWriter(fWrite);
        pWrite.println(kbStr);
        pWrite.close();}}