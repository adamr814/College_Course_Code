//Adam Roy
//CSCI 280
//Assignment 8

class SavingsAccount{
    private static double interestRate;
    private int Balance;

public SavingsAccount(int Balance){
    this.Balance = Balance;}

public int getBalance(){
    return Balance;}

public static void modifyInterestRate(double rate){
    interestRate = rate;}

public int calculateMonthlyInterest(){
    Balance += (Balance * interestRate / 12);
    return Balance;}}
    
public class Savings{
    public static void main(String[] args){
        SavingsAccount saver1 = new SavingsAccount(2000);
        SavingsAccount saver2 = new SavingsAccount(3000);

        SavingsAccount.modifyInterestRate(0.04);
        System.out.println("Saver 1");
        System.out.println("Balance before interest -> $" + saver1.getBalance());
        System.out.println("Balance after interest  -> $" + saver1.calculateMonthlyInterest());
        System.out.println("\nSaver 2");
        System.out.println("Balance before interest -> $" + saver2.getBalance());
        System.out.println("Balance after interest  -> $" + saver2.calculateMonthlyInterest());
        System.out.println("\n***** Increasing interest to 5% *****");
        SavingsAccount.modifyInterestRate(0.05);
        System.out.println("Saver 1");
        System.out.println("Balance before interest -> $" + saver1.getBalance());
        System.out.println("Balance after interest  -> $" + saver1.calculateMonthlyInterest());
        System.out.println("\nSaver 2");
        System.out.println("Balance before interest -> $" + saver2.getBalance());
        System.out.println("Balance after interest  -> $" + saver2.calculateMonthlyInterest());
    }}