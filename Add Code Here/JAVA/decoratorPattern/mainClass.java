package decoratorPattern;
import java.util.*;
import java.util.concurrent.TimeUnit;  

class mainClass {
    public static void main(String[] args) {
        mainClass clazz = new mainClass();
        clazz.mainWork();
        
    }
    
    private void mainWork() {
       simpleBase base=new simpleBase();
       onionToppings toppings=new onionToppings(base);
       cheeseToppings doubleCheese=new cheeseToppings(toppings);
       cheeseToppings trippleCheese=new cheeseToppings(doubleCheese);
       System.out.println("The cost of your pizza is: "+trippleCheese.cost());
    }
    
    
    }