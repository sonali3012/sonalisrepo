package Concrete_classes;

/*
Define three attributes:
brand (String)
model (String)
price (int)
Create a constructor

The constructor should take three parameters (brand, model, and price) and initialize the attributes.
Define a method displayInfo()

This method should print all the details of the car.
Create a main method inside another class (e.g., Main)

Inside main(), create an object of the Car class with values.
Call displayInfo() on the created object.
 */

public class Car {
    public String brand;
    private String model;
    public int price;

    public Car(String brand, String model, int price) {
        this.brand = brand;
        this.model = model;
        this.price = price;
    }

    public String getmodel() {
        return getmodel();
    }

    public void setmodel(String model) {
        this.model = model;
    }

    @Override
    public String toString() {
        return "Brand: " + brand + ", Model: " + model + ", Price: $" + price;
    }

    public static void main(String[] args) {
        Car car = new Car("Porsche", "500", 2000000);
        System.out.println(car.toString());

        car.setmodel("79");
        System.out.println(car.toString());
    }
}