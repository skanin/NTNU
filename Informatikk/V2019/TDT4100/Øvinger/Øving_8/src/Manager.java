import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.function.BinaryOperator;

public class Manager implements Employee {

    private List<Employee> employees;

    public Manager(Collection<Employee> employees){
        this.employees = new ArrayList<>(employees);
    }

    private Employee getEmployee(){
        return employees.get((int) Math.floor(Math.random() * employees.size()));
    }

    public double doCalculations(BinaryOperator<Double> op, double val1, double val2){
        return getEmployee().doCalculations(op, val1, val2);
    }

    public void printDocument(String document){
        getEmployee().printDocument(document);
    }

    public int getTaskCount(){
        return employees.stream().mapToInt(e -> e.getTaskCount()).sum();
    }

    public int getResourceCount(){
        return 1 + employees.stream().mapToInt(e -> e.getResourceCount()).sum();
    }

}
