//Adam Roy
//CSCI 280
//Assignment 7

class Account{
    private String ID;
    private String Name;
    private int Balance;

public Account(String ID, String Name){
    this.ID = ID;
    this.Name = Name;}

public Account(String ID, String Name, int Balance){
    this.ID = ID;
    this.Name = Name;
    this.Balance = Balance;}

public String getID(){
    return this.ID;}
public String getName(){
    return this.Name;}
public int getBalance(){
    return this.Balance;}

public void setID(String ID){
    this.ID = ID;}
public void setName(String Name){
    this.Name = Name;}
public void setBalance(int Balance){
    this.Balance = Balance;}

public int credit(int amount){
    this.Balance += amount;
    return Balance;}

public int debit(int amount){
    if(amount <= Balance){
        this.Balance -= amount;}
    else{
        System.out.print("\n*** Not enough funds in account ***");}
    return Balance;}

public int interAccountTransfer(Account transferTo, int amount){
    if(amount <= this.Balance){
        this.debit(amount);
        transferTo.credit(amount);}
    else{
        System.out.print("\n*** Not enough funds in account ***");}
    return Balance;}}

public class Bank{
    public static void main(String[] args){
        Account acctObj1 = new Account("00001", "Mike Meyers");
        Account acctObj2 = new Account("00002", "Elon Musk");
        Account acctObj3 = new Account("00003", "Jeff Bezos", 1000000000);

        System.out.println("\nName on account               - " + acctObj1.getName() + "\nAccount number                - " + acctObj1.getID() + "\n(Credit  ) Balance of account - $" + acctObj1.credit(500));
        System.out.println("\nName on account               - " + acctObj2.getName() + "\nAccount number                - " + acctObj2.getID() + "\n(Credit  ) Balance of account - $" + acctObj2.credit(1500));
        System.out.println("\nName on account               - " + acctObj1.getName() + "\nAccount number                - " + acctObj1.getID() + "\n(Debit   ) Balance of account - $" + acctObj1.debit(300));
        System.out.println("\nName on account               - " + acctObj1.getName() + "\nAccount number                - " + acctObj1.getID() + "\n(Debit   ) Balance of account - $" + acctObj1.debit(300));
        System.out.println("\nName on account               - " + acctObj3.getName() + "\nAccount number                - " + acctObj3.getID() + "\n(Transfer) Balance of account - $" + acctObj3.interAccountTransfer(acctObj1, 4000));
        System.out.println("\nName on account               - " + acctObj1.getName() + "\nAccount number                - " + acctObj1.getID() + "\n(Balance ) Balance of account - $" + acctObj1.getBalance());

    }
}