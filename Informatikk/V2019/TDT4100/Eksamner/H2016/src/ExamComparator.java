import java.util.Comparator;

public class ExamComparator implements Comparator<Exam> {

    @Override
    public int compare(Exam e1, Exam e2){
        return e1.getGrade() - e2.getGrade();
    }

}
