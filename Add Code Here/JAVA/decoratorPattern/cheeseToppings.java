package decoratorPattern;

public class cheeseToppings extends IPizzaIngr {

  
    IPizza pizza;
    public cheeseToppings(IPizza pizza) {
        this.pizza=pizza;
    }

    @Override
    public int cost() {
        return pizza.cost()+ 40;
    }
}
