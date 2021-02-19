package patterns.delegation.office;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Printer {
	
	private Map<Employee, List<String>> employeeRecord;
	
	public Printer() {
		employeeRecord = new HashMap<>();
	}
	
	public void printDocument(String document, Employee employee) {
		System.out.println(document);
	
		if (!employeeRecord.containsKey(employee)){
			employeeRecord.put(employee, new ArrayList<String>());
			employeeRecord.get(employee).add(document);
		}else {
			employeeRecord.get(employee).add(document);
		}
	}

	public List<String> getPrintHistory(Employee employee){
		if(employeeRecord.containsKey(employee)) {
			return employeeRecord.get(employee);
		}
		employeeRecord.put(employee, new ArrayList<String>());
		return employeeRecord.get(employee);
	}
}
