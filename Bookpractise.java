/*
Concrete class
Create a Book class with:
Attributes: title, author, price
A method displayInfo() to print book details
A constructor to initialize all attributes
Then, create an object of Book and call displayInfo().
     */


package Concrete_classes;

public class Bookpractise {

    public String title;
    private String author;
    public double price;

    public Bookpractise(String title, String author, double price) {
        this.title = title;
        this.author = author;
        this.price = price;
    }

    public String getauthor() {
        return author;
    }

    public void setauthor(String author) {
        this.author = author;
    }

    @Override
    public String toString() {
        return "Book title: " + title + ", Author: " + author + ", price: $" + price;
    }

    public static void main(String[] args) {
        Bookpractise Book = new Bookpractise("The Great Gatsby", "Fitzgerald", 10);
        System.out.println(Book.toString());

        Book.setauthor("Selena Gomez");
        System.out.println(Book.toString());

    }
}