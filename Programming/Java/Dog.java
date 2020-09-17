
public class Dog {
    String breed;
    int dogAge;
    String color;
    String gender;
    String dogName;
    
    //Lesson from Constructors
    Dog(String name){
        System.out.println("Name of the dog is: " + name);
        dogName = name;
    }
    
    public void setAge(int age){
        dogAge = age;
    }

    public void getAge() {
        System.out.println("Age of the dog is: " + dogAge);
    }

    public void getName(){
        System.out.println("You cant even remember the name of your dog?" + dogName);
    }

    
    //Where stuff will be commanded
    public static void main(String []args) {
        Dog hatdog = new Dog("lmfao");
        hatdog.setAge(13);
        hatdog.getAge();
        hatdog.getName();

    }
}

//There can only be one public class per source file, and should be named the same as the file