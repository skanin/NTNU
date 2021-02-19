package main;

public class Player {
	
	private final String name;
	private int score;
	protected static int COUNTER = 0;
	private final int id;
	private int numberOfThrows;
	
	public Player(String name) {
		this.name = name;
		this.score = 0;
		this.numberOfThrows = 0;
		this.id = COUNTER;
		COUNTER++;
	}
	
	public void addScore(int score) {
		this.score += score;
	}
	
	public int getId() {
		return this.id;
	}
	
	public String getName() {
		return this.name;
	}
	
	public void incrementNumberOfThrows() {
		numberOfThrows++;
	}
	
	public int getNumberOfThrows() {
		return this.numberOfThrows;
	}
	
	public void setNumberOfThrows(int num) {
		this.numberOfThrows = num;
	}
	
	public int getScore() {
		return this.score;
	}
	
	@Override
	public String toString() {
		return this.name;
	}
}
