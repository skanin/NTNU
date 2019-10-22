public class Exam implements Comparable<Exam>{

    private Course course;
    private char grade;

    public Exam(char grade, Course course){
        if("ABCDEF".indexOf(Character.toUpperCase(grade)) == -1) throw new IllegalArgumentException("");
        this.grade = Character.toUpperCase(grade);
        this.course = course;
    }


    public boolean isPass(){
        return grade != 'F';
    }

    public char getGrade(){
        return grade;
    }

    public Course getCourse(){
        return course;
    }

    @Override
    public int compareTo(Exam e){
        return course.compareTo(e.getCourse());
    }

}
