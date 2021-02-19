package patterns.delegation.office;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.concurrent.ThreadLocalRandom;

public class Manager implements Employee{
	
	private List<Employee> employees;
	private int taskCount;
	
	public Manager(Collection<Employee> employees) {
		if(employees.isEmpty()) {
			throw new IllegalArgumentException("Employees can't be empty");
		}
		this.employees = new ArrayList<>(employees);
		taskCount = 0;
	}
	
	@Override
	public double doCalculations(BinaryOperator<Double> operation, double value1, double value2) {
		taskCount++;
		int randomNumb = ThreadLocalRandom.current().nextInt(0, employees.size());
		return employees.get(randomNumb).doCalculations(operation, value1, value2);
	}

	@Override
	public void printDocument(String document) {
		int randomNumb = ThreadLocalRandom.current().nextInt(0, employees.size());
		employees.get(randomNumb).printDocument(document);
		taskCount++;
	}

	@Override
	public int getTaskCount() {
		return taskCount;
	}

	@Override
	public int getResourceCount() {
		int sum = 1;
		for(Employee e: employees) {
			sum += e.getResourceCount();
		}
		return sum;
	}
	public static void main(String[] args) {
		Clerk[] clerks = {new Clerk(new Printer()), new Clerk(new Printer()), new Clerk(new Printer()), new Clerk(new Printer()), new Clerk(new Printer()), new Clerk(new Printer()), new Clerk(new Printer())};
		Manager[] managers1 = {new Manager(Arrays.asList(clerks))};
		Manager[] managers2 = {new Manager(Arrays.asList(managers1))};
		
		Manager topManager1 = new Manager(Arrays.asList(clerks));
		Manager topManager2 = new Manager(Arrays.asList(managers2));
		
		System.out.println("Kun Clerks: ");
		System.out.println("Task count: " + topManager1.getTaskCount());
		System.out.println("Recource count: " + topManager1.getResourceCount());
		System.out.println();
		System.out.println("Flere nivåer med Managers: ");
		System.out.println("Task count: " + topManager2.getTaskCount());
		System.out.println("Recource count: " + topManager2.getResourceCount());
	}
}
