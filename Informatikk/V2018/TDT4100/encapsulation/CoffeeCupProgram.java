package encapsulation;

import java.util.Random;

public class CoffeeCupProgram {

	private CoffeeCup cup;
	private Random r;
	
	public void init(){
		cup = new CoffeeCup();
		r = new Random(123456789L);
	}
	
	public void run(){
		part1();
		part2();
	}
	
	private void part1(){
		cup.increaseCupSize(40.0);
		cup.fillCoffee(20.5);
		cup.drinkCoffee(Math.floor(r.nextDouble()*20.5));
		cup.fillCoffee(32.5);
		cup.drinkCoffee(Math.ceil(r.nextDouble()*38.9));
		cup.drinkCoffee(Math.ceil(r.nextDouble()*42));
		cup.increaseCupSize(17);
		//cup.drinkCoffee(40); // Volume = 5, capacity = 57, drinkCoffee som utløser	
		//cup.drinkCoffee(Math.ceil(r.nextDouble()*42)); // Volume = 5, capacity = 57
		//cup.drinkCoffee(Math.floor(r.nextDouble()*20.5)); // Volume = 5, capacity = 57
		cup.fillCoffee(32.5);
		cup.drinkCoffee(Math.ceil(r.nextDouble()*38.9)); 
		//cup.drinkCoffee(Math.ceil(r.nextDouble()*42)); // Volume = 2.5, capacity = 57
		cup.increaseCupSize(17);
	}
	
	private void part2(){
		cup = new CoffeeCup(40.0, 20.5);
		r = new Random(987654321L); // Capacity = 40, volume = 20.5
		cup.drinkCoffee(Math.floor(r.nextDouble()*20.5));
		cup.fillCoffee(Math.floor(r.nextDouble()*30)); // Capacity = 40, volume = 14.5
		cup.drinkCoffee(Math.ceil(r.nextDouble()*38.9)); // Capacity = 40, volume = 38.5
		cup.drinkCoffee(Math.ceil(r.nextDouble()*42)); // C = 40, V = 36.5
		cup.increaseCupSize(Math.floor(r.nextDouble()*26)); // C = 40, V = 6.5
		//cup.fillCoffee(Math.ceil(r.nextDouble()*59)); // C = 40, V = 6.5
		// fillCoffee utløser unntak av typer IllegalArgumentException
		//cup.drinkCoffee(Math.ceil(r.nextDouble()*42)); // C = 40, V = 6.5
		// drinkCoffee utløser unntak av typen IllegalArgumentException
		cup.increaseCupSize(Math.floor(r.nextDouble()*35)); // C = 40, V = 6.5
		cup.fillCoffee(Math.floor(r.nextDouble()*30)); // C = 63, V = 6.5
		cup.increaseCupSize(Math.floor(r.nextDouble()*26)); // C = 63, V = 6.5??? 
	}
	
	
	public static void main(String[] args) {
		CoffeeCupProgram program = new CoffeeCupProgram();
		program.init();
		program.run();
	}

}