import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.function.BinaryOperator;

public class Printer {

    private HashMap<Employee, ArrayList<String>> printHistory = new HashMap<>();

    public Printer(){

    }

    public void printDocument(String document, Employee employee){
        System.out.println(document);

        if(printHistory.containsKey(employee)) {
            printHistory.get(employee).add(document);
        }else {
            printHistory.put(employee, new ArrayList<>(Arrays.asList(document)));
        }
    }

    public List<String> getPrintHistory(Employee employee){
        if(printHistory.containsKey(employee)) return printHistory.get(employee);
        return null;
    }

}
