import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.stream.Collectors;

public class Person implements Iterable<Person> {

    private final String name;
    private Person mother, father;
    private Gender gender = null;
    private Collection<Person> children;

    public Person(String name){
        this.name = name;
        this.children = new ArrayList<Person>();
    }

    public Person getMother(){
        return this.mother;
    }

    public Person getFather(){
        return this.father;
    }

    public Gender getGender(){
        return this.gender;
    }

    public void setGender(Gender gender){
        this.gender = gender;
    }

    public String getName(){
        return this.name;
    }

    public int getChildCount(){
        return this.children.size();
    }

    public boolean hasChild(Person c){
        return this.children.contains(c);
    }

    public Collection<Person> getChildren(Gender gender){
        return children.stream().filter(c -> c.getGender() == gender || gender == null).collect(Collectors.toList());
    }

    @Override
    public Iterator<Person> iterator(){
        return children.iterator();
    }

    public void addChild(Person child){
        if(this.gender == Gender.MALE){
            if(child.father != null){
                child.father.children.remove(child);
            }
            child.father = this;
        }else if(this.gender == Gender.FEMALE){
            if(child.mother != null){
                child.mother.children.remove(child);
            }
            child.mother = this;
        }
        children.add(child);
    }


    public static void main(String[] args){
        Person sander = new Person("Sander");
        sander.setGender(Gender.MALE);
        Person sara = new Person("Sara");
        sara.setGender(Gender.FEMALE);
        Person filip = new Person("Filip");
        filip.setGender(Gender.MALE);

        sander.addChild(sara);
        sander.addChild(filip);

        for(Person p : sander){
            System.out.println(p);
        }
    }
}
