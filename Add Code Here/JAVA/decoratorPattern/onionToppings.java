package decoratorPattern;

public class onionToppings extends IPizzaIngr {

    IPizza pizza;
    public onionToppings(IPizza pizza) {
        this.pizza=pizza;
    }

    @Override
    public int cost() {
        return pizza.cost()+ 20;
    }
    
}
