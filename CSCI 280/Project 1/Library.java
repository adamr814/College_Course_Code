//Adam Roy
//CSCI 280
//Project 1

import java.util.Scanner;

class Book{
    //Declaring Variables
    public String bookName;
    public String authorName;
    public String ISBN;
    public int availability;
    public int bookQuantity;

    Scanner kb = new Scanner(System.in);
    //Constructor for book class
    public Book(){
        System.out.print("Enter the book ISBN: ");
        this.ISBN = kb.nextLine();
        System.out.print("Enter book title: ");
        this.bookName = kb.nextLine();
        System.out.print("Enter name of author: ");
        this.authorName = kb.nextLine();
        System.out.print("Enter the number of copies: ");
        this.bookQuantity = kb.nextInt();
        this.availability = this.bookQuantity;}}

class Subscriber{
    String firstName;
    String lastName;
    String acctType;
    String regNum;

    Book borrowBook[] = new Book[3];
    public int bookCount = 0;
    Scanner kb = new Scanner(System.in);
    //Constructor for subscriber class
    public Subscriber(){
        System.out.print("Enter first name: ");
        this.firstName = kb.nextLine();
        System.out.print("Enter last name: ");
        this.lastName = kb.nextLine();
        System.out.print("Enter account type (P = Professor S = Student): ");
        this.acctType = kb.nextLine();
        System.out.print("Enter ID Number: ");
        this.regNum = kb.nextLine();}}

class Books{
    //This piece creates an array of objects to store "books" in the library
    Book libBooks[] = new Book[50];
    public static int count;
    Scanner kb = new Scanner(System.in);
    public int compareBooks(Book b1, Book b2){
        if(b1.bookName.equalsIgnoreCase(b2.bookName)){
            System.out.println("Book of this name is already in the system");
            return 0;}
        if(b1.ISBN.equalsIgnoreCase(b2.ISBN)){
            System.out.println("Book of this ISBN is already in the system");
            return 0;}
        return 1;}

    public void addBook(Book b){
        for(int i = 0; i<count; i++){
            if(this.compareBooks(b, this.libBooks[i])==0) return;}
        if(count < 25){
            libBooks[count] = b;
            count++;}
        else{
            System.out.println("Cannot add any more books to the system");}}

    public void searchISBN(){
        String ISBN;
        System.out.print("Enter ISBN to search for: ");
        ISBN = kb.nextLine();
        int flag = 0;
        System.out.println("| ISBN     | Book Name     | Author     | Available     | Total     |");
        for(int i=0; i<count; i++){
            if(ISBN.equalsIgnoreCase(libBooks[i].ISBN)){
                String str = String.format("| %-9s| %-14s| %-11s| %-14s| %-10s|", libBooks[i].ISBN, libBooks[i].bookName, libBooks[i].authorName, libBooks[i].availability, libBooks[i].bookQuantity);
                System.out.println(str);
            flag++;
            return;}}
        if(flag == 0){System.out.println("No book of" + ISBN + "found");}}
    
    public void searchAuthor(){
        String bookAuthor;
        System.out.print("Enter an author to search for: ");
        bookAuthor = kb.nextLine();
        int flag = 0;
        System.out.println("| ISBN     | Book Name     | Author     | Available     | Total     |");
        for(int i=0; i<count; i++){
            if(bookAuthor.equalsIgnoreCase(libBooks[i].authorName)){
                String str = String.format("| %-9s| %-14s| %-11s| %-14s| %-10s|", libBooks[i].ISBN, libBooks[i].bookName, libBooks[i].authorName, libBooks[i].availability, libBooks[i].bookQuantity);
                System.out.println(str);
            flag++;
            return;}}
        if(flag == 0){System.out.println("No books by " + bookAuthor + " found");}}
    
    public void displayBooks(){
        System.out.println("| ISBN     | Book Name     | Author     | Available     | Total     |");
        for(int i=0; i<count; i++){
            String str = String.format("| %-9s| %-14s| %-11s| %-14s| %-10s|", libBooks[i].ISBN, libBooks[i].bookName, libBooks[i].authorName, libBooks[i].availability, libBooks[i].bookQuantity);
                System.out.println(str);}}
    
    public void updateQuantity(){
        System.out.print("Enter ISBN of book to update: ");
        String ISBN = kb.nextLine();
        for(int i = 0; i<count; i++){
            if(ISBN.equalsIgnoreCase(libBooks[i].ISBN)){
                System.out.print("Enter quantity change: ");
                int quantity = kb.nextInt();
                libBooks[i].bookQuantity += quantity;
                libBooks[i].availability += quantity;
                return;}}}

    public void removeBook(){
        System.out.print("Enter ISBN of book: ");
        String ISBN = kb.nextLine();
        for(int i=0; i < count; i++){
            if(libBooks[i].ISBN.equalsIgnoreCase(ISBN)){
                System.out.print("Permenantly delete book? 1(Yes)|0(No): ");
                int choice = kb.nextInt();
                if(choice == 1){
                   libBooks[i] = null;
                   count--;
                   //This section is prone to crashing due to java being unable to read null
                   //would have been better to recycle null into new book rather than just trying to resize array
                   return;}
                else{
                    System.out.println("Book was not removed");
                    return;}}}}

    public void displayMenu(){
        System.out.println(
            "\n**************************************************\n" +
            " 1: Manage books\n" +
            " 2: Search for a book\n" +
            " 3: Show all books\n" +
            " 4: Manage Subscribers\n" +
            " 5: Show all subscribers\n" +
            " 6: Check in book\n" +
            " 7: Check out book\n" +
            "-1: Exit Application\n" +
            "**************************************************\n");
        System.out.print("Enter choice: ");}

    public int isAvailable(String ISBN){
        for(int i=0; i<count; i++){
            if(ISBN.equalsIgnoreCase(libBooks[i].ISBN)){
                if(libBooks[i].availability > 0){
                    System.out.println("Book is available to check out");
                    return i;}
            System.out.println("Book is unavailavle to check out");
            return -1;}}
        System.out.println("No book of ISBN " + ISBN + " in library");
        return -1;}

    public Book checkOutBook(){
        System.out.print("Enter ISBN of book to check out: ");
            String ISBN = kb.nextLine();
            int bookIndex = isAvailable(ISBN);
            if (bookIndex != -1) {
                libBooks[bookIndex].availability--;
                return libBooks[bookIndex];}
            return null;}

    public void checkInBook(Book b){
        for (int i=0; i<count; i++){
            if (b.equals(libBooks[i])){
                libBooks[i].availability++;
                return;}}}}

class Subscribers{
    Scanner kb = new Scanner(System.in);
    Subscriber libSubscribers[] = new Subscriber[50];
    public static int count = 0;

    public void addSubscriber(Subscriber s){
        for (int i = 0; i < count; i++){
            if (s.regNum.equalsIgnoreCase(libSubscribers[i].regNum)){
                System.out.println(
                    "This ID number " + s.regNum + " is already in the system");
                return;}}
        if (count <= 50){
            libSubscribers[count] = s;
            count++;}}

    public void removeSub(){
        System.out.print("Enter ID number: ");
        String regNum = kb.nextLine();
        for(int i=0; i < count; i++){
            if(libSubscribers[i].regNum.equalsIgnoreCase(regNum)){
                System.out.print("Permenantly delete subscriber? 1(Yes)|0(No): ");
                int choice = kb.nextInt();
                if(choice == 1){
                   libSubscribers[i] = null;
                   count--;
                   //This section is prone to crashing due to java being unable to read null
                   //would have been better to recycle null into new sub rather than just trying to resize array
                   return;}
                else{
                    System.out.println("Subscriber was not removed");
                    return;}}}}
    
    public void editDetails(int ch){
        System.out.print("Enter ID number: ");
        String regNum = kb.nextLine();
        String updt;
        for(int i=0; i<count; i++){
            if(libSubscribers[i].regNum.equalsIgnoreCase(regNum)){
                switch(ch){
                    case 1:    
                        System.out.print("Enter updated first name: ");
                        updt = kb.nextLine();
                        libSubscribers[i].firstName = updt;
                        break;
                    case 2:
                        System.out.print("Enter updated last name: ");
                        updt = kb.nextLine();
                        libSubscribers[i].lastName = updt;
                        break;
                    case 3:
                        System.out.print("Enter updated account type (S or P): ");
                        updt = kb.nextLine();
                        libSubscribers[i].acctType = updt;
                        break;
                    case 4:
                        System.out.print("Enter updated ID number: ");
                        updt = kb.nextLine();
                        libSubscribers[i].regNum = updt;}
                break;}}}
        
    public void displayAllSubs(){
        System.out.println("\n| First Name     | Last Name     | Account Type     | ID Number     |");
        for (int i = 0; i < count; i++){
            String str = String.format("| %-15s| %-14s| %-17s| %-14s|", libSubscribers[i].firstName, libSubscribers[i].lastName, libSubscribers[i].acctType, libSubscribers[i].regNum);
            System.out.println(str);}}
    
    public int isSub(){
        System.out.print("Enter ID number: ");
        String regNum = kb.nextLine();
        for (int i = 0; i < count; i++){
            if(libSubscribers[i].regNum.equalsIgnoreCase(regNum)){
                return i;}}
        System.out.println("Not a registered subscriber, please register subscriber");
        return -1;}

    public void checkOutBook(Books Book){
        int subStatus = this.isSub();
        if(subStatus != -1){
            System.out.println("Displaying all books");
            Book.displayBooks();
            Book b = Book.checkOutBook();
            if(b != null){
                if(libSubscribers[subStatus].bookCount <= 2){
                    System.out.println("Adding book to ID");
                    libSubscribers[subStatus].borrowBook[libSubscribers[subStatus].bookCount] = b;
                    libSubscribers[subStatus].bookCount++;
                    return;}
                else{
                    System.out.println("Student cannot borrow more than 2 books");
                return;}}
            System.out.println("The selected book is unavailable");}}
    
    public void checkInBook(Books Book){
        int subStatus = this.isSub();
        if(subStatus != -1){
            System.out.println("| ISBN     | Book Name     | Author     |");
            Subscriber s = libSubscribers[subStatus];
            for(int i=0; i< s.bookCount; i++){
                String str = String.format("| %-9s| %-14s| %-11s", s.borrowBook[i].ISBN, s.borrowBook[i].bookName, s.borrowBook[i].authorName);
                System.out.println(str);}
            System.out.println("Enter ISBN of book to ckeck in");
            String ISBN = kb.nextLine();
            for(int i=0; i<s.bookCount; i++){
                if(ISBN.equalsIgnoreCase(s.borrowBook[i].ISBN)){
                    Book.checkInBook(s.borrowBook[i]);
                    s.borrowBook[i] = null;
                    return;}}
            System.out.println("Book of ISBN " + ISBN + " cannot be found");}}}

public class Library{
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        System.out.print("********  Library Management System V2.6  ********\n");
        Books obj = new Books();
        Subscribers objSub = new Subscribers();
        int choice;
        int searchChoice;
        do{
            obj.displayMenu();
            choice = kb.nextInt();
            switch (choice){
            case 1:
                System.out.println("\n1: Add book to system\n" +
                "2: Remove book from system\n" +
                "3: Edit book quantity");
                System.out.print("\nEnter Choice: ");
                searchChoice = kb.nextInt();
                switch(searchChoice){
                case 1:
                    Book b = new Book();
                    obj.addBook(b);
                    break;
                case 2:
                    obj.removeBook();
                    break;
                case 3:
                    obj.updateQuantity();}
            break;
            case 2:
                System.out.println("1: Search by ISBN");
                System.out.println("2: Search by author");
                System.out.print("\nEnter Choice: ");
                searchChoice = kb.nextInt();
                switch (searchChoice){
                case 1:
                    obj.searchISBN();
                    break;
                case 2:
                    obj.searchAuthor();}
            break; 
            case 3:
                obj.displayBooks();
                break;
            case 4:
                System.out.println("\n1: Add subscriber to system\n" +
                "2: Remove subscriber from system\n" +
                "3: Edit subscriber details");
                System.out.print("\nEnter Choice: ");
                searchChoice = kb.nextInt();
                switch(searchChoice){
                case 1:
                    Subscriber s = new Subscriber();
                    objSub.addSubscriber(s);
                    break; 
                case 2:
                    objSub.removeSub();
                    break;
                case 3:
                    System.out.println("\n1: Change first name\n" +
                    "2: Change last name\n" +
                    "3: Change account type\n" +
                    "4: Change ID number");
                    System.out.print("\nEnter Choice: ");
                    searchChoice = kb.nextInt();
                    switch(searchChoice){
                        case 1:    
                            objSub.editDetails(1);
                            break;
                        case 2:
                            objSub.editDetails(2);
                            break;
                        case 3:
                            objSub.editDetails(3);
                            break;
                        case 4:
                            objSub.editDetails(4);
                            break;
                        default:
                            System.out.println("Not a valid option returning to menu");}
                break;}
            break;
            case 5:
                objSub.displayAllSubs();
                break;
            case 6:
                objSub.checkInBook(obj);
                break;
            case 7:
                objSub.checkOutBook(obj);
                break;     
            case -1:
                System.exit(0);
            default:
                System.out.println("Invalid Please Enter valid option");}}
        while (choice != -1);
    kb.close();}}