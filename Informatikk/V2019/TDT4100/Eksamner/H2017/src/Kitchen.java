import java.util.*;
import java.util.function.Predicate;

public class Kitchen {

    private Collection<KitchenListener> listeners = new ArrayList<>();
    private Map<Table, Collection<Course>> courseQueue = new HashMap<Table, Collection<Course>>();


    public void menuItemAdded(Table table, MenuItem item){
        if(item instanceof Course){
            produceCourse(table, (Course) item);
        }else if (item instanceof Meal){
            for(Course c : (Meal) item){
                produceCourse(table, c);
            }
        }

    }

    public void addListener(KitchenListener listener){
        if(!listeners.contains(listener)) listeners.add(listener);
    }

    public void removeListener(KitchenListener listener){
        this.listeners.remove(listener);
    }

    private void fireCourseReady(Table table, Course course){
        for(KitchenListener l : listeners){
            l.courseReady(table, course);
        }
    }

    private void produceCourse(Table table, Course course) {
        Collection<Course> courses = courseQueue.get(table);
        if(courses == null){
            courseQueue.put(table, new ArrayList<>());
            courses = courseQueue.get(table);
        }
        courses.add(course);
        courseQueue.put(table, courses);
    }

    private void courseProduced(Table table, Course course) {
        Collection<Course> courses = courseQueue.get(table);
        courses.remove(course);
        fireCourseReady(table, course);
    }


}
