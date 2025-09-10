package Abstract_classes;

abstract class Animal {
    // Abstract method (does not have a body)
    abstract void sound();

    // Regular method
    void eat() {
        System.out.println("This animal eats food.");
    }
}

class Dog extends Animal {
    // Implementing the abstract method sound()
    void sound() {
        System.out.println("The dog barks.");
    }
}

class Cat extends Animal {
    // Implementing the abstract method sound()
    void sound() {
        System.out.println("The cat meows.");
    }
}

public class yourMain {
    public static void main(String[] args) {
        // Cannot create an object of Animal (abstract class)
        // Animal animal = new Animal(); // This would give an error
        
        // Create objects of Dog and Cat (which are concrete subclasses of Animal)
        Animal dog = new Dog();
        Animal cat = new Cat();

        // Call the implemented methods
        dog.sound(); // "The dog barks."
        cat.sound(); // "The cat meows."

        // Call the regular method (inherited from Animal class)
        dog.eat(); // "This animal eats food."
        cat.eat(); // "This animal eats food."
    }
}
