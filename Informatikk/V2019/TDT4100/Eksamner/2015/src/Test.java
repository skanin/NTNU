import java.util.ArrayList;
import java.util.Collection;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class Test {

    public Collection<Person> getMatchingPersons1(Collection<Person> persons, Predicate<Person> predicate){
        Collection<Person> result = new ArrayList<Person>();
        for(Person p : persons){
            if(predicate.test(p)){
                result.add(p);
            }
        }
        return result;
    }

    public Collection<Person> getMatchingPersons2(Collection<Person> persons, Predicate<Person> predicate){
        return persons.stream().filter(predicate).collect(Collectors.toList());
    }

}
