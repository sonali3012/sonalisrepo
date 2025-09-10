package Interface_classes;

/* An interface called Vehicle
   Two classes (Car and Bike) implementing the Vehicle interface
   A main method to test the implementation */

interface Vehicle {
    void start();
    void stop();
}

class Car implements Vehicle {
    public void start() {
        System.out.println("Car starts using a button");
    }

    public void stop() {
        System.out.println("Car stops using handbrake and brakes");
    }
}

class Bike implements Vehicle {
    public void start() {
        System.out.println("Bike starts with keys");
    }

    public void stop() {
        System.out.println("Bike is stopped using brakes");
    }
}

public class myMain {
    public static void main(String[] args) {
        // Create objects of Car and Bike, both implementing Vehicle
        Vehicle myCar = new Car();
        myCar.start();
        myCar.stop();

        System.out.println(); // Space between car and bike outputs

        Vehicle myBike = new Bike();
        myBike.start();
        myBike.stop();
    }
}
