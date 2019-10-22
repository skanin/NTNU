public abstract class MenuItem {

    private final String name, description;

    public MenuItem(String name, String description){
        this.description = description;
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    public String getDescription() {
        return description;
    }
}
