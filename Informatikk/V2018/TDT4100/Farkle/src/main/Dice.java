package main;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class Dice {
	
	private List<Integer> validRolls;
	private int face;
	private Random rand;
	private boolean isSetAside;
	
	
	public Dice() {
		this.validRolls = new ArrayList<Integer>(Arrays.asList(1,5));
		this.rand = new Random();
		this.face = 0;
		this.isSetAside = false;
	}
	
	public List<Integer> getValidRolls(){
		return validRolls;
	}
	
	public void roll() {
		if(!getIsSetAside()) {
			face = rand.nextInt(6) + 1;	
		}
		
	}
	
	public boolean getIsSetAside() {
		return this.isSetAside;
	}
	
	public int getFace() {
		return this.face;
	}
	
	public boolean isValidRoll() {
		
		return validRolls.contains(face);
	}
	
	public void setIsSetAside() {
		this.isSetAside = true;
	}
	
	public static void main(String[] args) {
		Dice d = new Dice();
		System.out.println(d.getValidRolls());
		d.roll();
		System.out.println(d.face);
		System.out.println(d.isValidRoll());
	}
}
