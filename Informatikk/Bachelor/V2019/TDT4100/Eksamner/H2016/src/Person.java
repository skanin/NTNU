import java.security.spec.ECField;
import java.util.ArrayList;
import java.util.Collection;

public class Person {

    private final String name;
    private Collection<Course> courses;
    private Collection<Exam> exams;

    public Person(String name){
        this.name = name;
        this.courses = new ArrayList<>();
        this.exams = new ArrayList<>();
    }

    public String getName(){
        return name;
    }

    public boolean hasCourse(String code){
        return courses.stream().anyMatch(c -> c.getCode().equals(code));
    }

    public boolean addCourse(Course c){
        if(hasCourse(c.getCode())){
            for(Course ex : courses) {
                if (ex.getCode().equals(c.getCode()) && ex.getTime().equals(c.getTime())) {
                    return false;
                }
            }
        }
        courses.add(c);
        return true;
    }

    public Exam addExam(Course c, char grade){
        if(!hasPassed(c.getCode())){
            Exam e = new Exam(grade, c);
            exams.add(e);
            return e;
        }
        return null;
    }

    public Exam getLastExam(String code){

    }


    public boolean hasPassed(String code){
        return exams.stream().anyMatch(e -> e.getCourse().getCode().equals(code) && e.isPass());
    }

    public static void main(String[] args){
        Course c = new Course("TDT4100");
        c.setTime("S2019");

        Person p = new Person("Sander");
        p.addCourse(c);
        System.out.println(p.hasCourse("TDT4100"));
    }
}
