package game;

public class Cell {
	private boolean isABoat = false;
	private boolean isHit = false;
	public Cell(){
		
	}
	
	public void hit() {
		isHit = true;
	}
	
	public boolean isHit() {
		return isHit;
	}
	
	public void setToBoat() {
		isABoat = true;
	}
	public boolean isABoat() {
		return isABoat;
	}
	public String toString() {
		if(isHit == false)
		{
			return "~";
		}
		else {
			if(isABoat) {
				
				return "X";
			}
			else {
				System.out.println("That's a miss...");
				return ".";
			}
		}
	}
	

}
