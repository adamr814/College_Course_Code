//Adam Roy
//CSCI 280
//Assignment 6

import java.util.Scanner;

public class Person{
    String Name;
    String Address;
   
    //Default constructor
    public Person(){
        Name = null;
        Address = null;}
    //Defined constructor
    public Person(String Name, String Address){
        this.Name = Name;
        this.Address = Address;
    }
    public String getName(){
        return this.Name;}
    public String getAddress(){
        return this.Address;}

    public void setName(String Name){
        this.Name = Name;}
    public void setAddress(String Address){
        this.Address = Address;}
    public static void main(String[] args){
        Teacher teacher = new Teacher("Fatima", "Monaco");
        if(teacher.addCourse("CS101")){
            System.out.println("The course CS101 was added to the registrar.");}
        else{System.out.println("The course CS101 cannot be added to the registrar.");}

        if(teacher.addCourse("CS102")){
            System.out.println("The course CS102 was added to the registrar.");}
        else{System.out.println("The course CS102 cannot be added to the registrar.");}

        if(teacher.addCourse("CS103")){
            System.out.println("The course CS103 was added to the registrar.");}
        else{System.out.println("The course CS103 cannot be added to the registrar.");}

        if(teacher.addCourse("CS104")){
            System.out.println("The course CS104 was added to the registrar.");}
        else{System.out.println("The course CS104 cannot be added to the registrar.");}

        if(teacher.addCourse("CS105")){
            System.out.println("The course CS105 was added to the registrar.");}
        else{System.out.println("The course CS105 cannot be added to the registrar.");}

        if(teacher.addCourse("CS106")){
            System.out.println("The course CS106 was added to the registrar.");}
        else{System.out.println("The course CS106 cannot be added to the registrar.");}

        if(teacher.addCourse("CS106")){
            System.out.println("The course CS106 was added to the registrar.");}
        else{System.out.println("The course CS106 cannot be added to the registrar.");}


        if(teacher.removeCourse("CS104")){
            System.out.println("The course CS104 was removed from the registrar.");}
        else{System.out.println("The course CS104 cannot be removed from the registrar.");}

        if(teacher.removeCourse("CS105")){
            System.out.println("The course CS105 was removed from the registrar.");}
        else{System.out.println("The course CS105 cannot be removed from the registrar.");}

        if(teacher.removeCourse("CS106")){
            System.out.println("The course CS106 was removed from the registrar.");}
        else{System.out.println("The course CS106 cannot be removed from the registrar.");}
    

        Student student = new Student("Armacost", "Grand Forks");
        student.addCourseGrade("CS101", 93);
        student.addCourseGrade("CS102", 97);
        student.addCourseGrade("CS103", 84);
        student.printGrades();
        String str = String.format("Average Grade Point: %.1f", student.getGradeAverage());
        System.out.print(str);}}

class Student extends Person{
    Scanner kb = new Scanner(System.in);
    int numCourses;
    String[] courses;
    int[] grades;
    
    //Student Constructor
    public Student(String Name, String Address){
        super(Name, Address);
        this.numCourses = 0;
        this.courses = new String[30];
        this.grades = new int[30];}
    
    public void addCourseGrade(String course, int grade){
        if(numCourses < 30){
            this.courses[numCourses] = course;
            this.grades[numCourses] = grade;
            numCourses++;}
        else{System.out.println("Cannot add more courses to this student");}}

    public void printGrades(){
        System.out.println("| Course | Grade |");
        for(int i=0; i<numCourses; i++){
            String str = String.format("|  %-5s |  %-2.2s   |", courses[i], grades[i]);
            System.out.println(str);}}

    public float getGradeAverage(){
        float total = 0;
        for(int i=0; i<numCourses; i++){
            total+=grades[i];}
        return total/numCourses;}}

class Teacher extends Person{
    int numCourses;
    String[] courses;
    public Teacher(String Name, String Address){
        super(Name, Address);
        this.numCourses = 0;
        this.courses = new String[30];}
    
    public boolean addCourse(String course){
        for(int i=0; i<numCourses; i++){
            if(courses[i] == course){
                return false;}}
        courses[numCourses++] = course;
        return true;}

    public boolean removeCourse(String course){
        for(int i=0; i<numCourses; i++){
            if(courses[i] == course){
                String temp = courses[i];
                courses[i] = courses[numCourses-1];
                courses[numCourses-1] = temp;
                numCourses--;
                return true;}}
        return false;}}
