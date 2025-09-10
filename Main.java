package Interface_classes;

interface Animal {
    void makeSound();
}

interface Pet {
    void showAffection();
}

class Cat implements Animal, Pet { 
    public void makeSound() {
        System.out.println("Cats meow");
    }

    public void showAffection() {
        System.out.println("Cats like rubbing themselves onto you");
    }
}
    

public class Main {
    public static void main(String[] args) {
        Cat cat = new Cat();
        cat.makeSound();
        cat.showAffection();
    }
}

