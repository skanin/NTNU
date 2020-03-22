import java.util.ArrayList;
import java.util.Collection;

public class Table implements KitchenListener {

    /*
    private final Menu menu;
    private Collection<Course> courses;
    private Collection<Meal> meals;


    public Table(Menu menu){
        this.menu = menu;
        this.courses = new ArrayList<>();
        this.meals = new ArrayList<>();
    }

    public void addCourse(Course c){
        this.courses.add(c);
    }

    public void addMeal(Meal m){
        this.meals.add(m);
    }

    public double getPrice() throws IllegalStateException {
        try{
            double price = 0.0;
            price += courses.stream().mapToDouble(menu::getPrice).sum();
            price += meals.stream().mapToDouble(menu::getPrice).sum();
            return price;
        } catch(IllegalArgumentException e) {
            throw new IllegalStateException(e);
        }
    }*/

    private Kitchen kitchen;
    private final Menu menu;
    private Collection<MenuItem> menuItems;

    public Table(Menu menu){
        this.menu = menu;
        this.menuItems = new ArrayList<>();
    }

    public void addMenuItem(MenuItem item){
        this.menuItems.add(item);
    }

    public double getPrice() throws IllegalStateException {
        try{
            double total = 0.0;
            for(MenuItem item : menuItems){
                if(item instanceof Course) {
                    total += menu.getPrice((Course) item);
                }else if (item instanceof Meal) {
                    total += menu.getPrice((Meal) item);
                }
            }
            return total;
        }catch (IllegalArgumentException e){
            throw new IllegalStateException(e);
        }
    }

    public void setKitchen(Kitchen kitchen){
        if(this.kitchen != null) {
            kitchen.removeListener(this);
        }
        this.kitchen = kitchen;
        kitchen.addListener(this);
    }

    public void addItem(MenuItem item){
        this.menuItems.add(item);
        if(!(this.kitchen == null)) kitchen.menuItemAdded(this, item);
    }

    public void courseReady(Table table, Course course){

    }
}
