import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Collection;

public class Family {

    private Collection<Person> members;

    public Family(){
        this.members = new ArrayList<Person>();
    }


    public void addMember(Person person){
        if(!members.contains(person)) members.add(person);
    }

    public Person findMember(String name){
        for(Person p : members){
            if(p.getName().equals(name)) return p;
        }
        return null;
    }

    public void save(OutputStream out){

    }

}
