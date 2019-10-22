import java.util.*;
import java.util.function.Predicate;

public class Meal extends MenuItem implements Iterable<Course> {

    private Collection<Course> courses;

    public Meal(String name, String description, Course[] courses){
        super(name, description);
        this.courses = Arrays.asList(courses);
    }

    public void addCourse(Course c){
        this.courses.add(c);
    }

    public void removeCourse(Course c){
        this.courses.remove(c);
    }

    @Override
    public Iterator<Course> iterator(){
        return this.courses.iterator();
    }

    public Course findCourse(Predicate<Course> test){
        for(Course c : courses){
            if(test.test(c)) {
                return c;
            }
        }
        return null;
    }

}
