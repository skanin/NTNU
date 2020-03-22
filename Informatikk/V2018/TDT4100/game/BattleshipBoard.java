package game;

public class BattleshipBoard {
	private Cell[][] board;
	private int currentPlayer; 
	
	public BattleshipBoard(/*String hangar, String slag, String ubaat, String fergatt, String patrulje*/) {
		board = new Cell[10][10];
		initBoard();
		currentPlayer = 1;
	}
	
	public void createBåt(int x,int y, int width, int height) {
		for(int lx = x; lx < x+width; lx ++)
			for(int ly = y; ly < y+height; ly ++) {
				if(board[lx][ly].isABoat()) {
					throw new IllegalArgumentException("THERE IS ALREADY A BOAT THERE MOTHERFUCKING IDIIIOTOTTT: " + lx + " " + ly);
				}
				board[lx][ly].setToBoat();
			}
	}
	
	public void addHangarskip(int x, int y, boolean h) {
		if(h) {
			createBåt(x,y,3,2);
		}
		else {
			createBåt(x,y,2,3);
		}
	}
	
	public void addSlagskip(int x, int y, boolean h) {
		if(h) {
			createBåt(x,y,4,1);
		}
		else {
			createBåt(x,y,1,4);
		}
	}
	
	public void addUbåt(int x, int y, boolean h) {
		if(h) {
			createBåt(x,y,3,1);
		}
		else {
			createBåt(x,y,1,3);
		}				
	}
	public void addFergatt(int x, int y, boolean h) {
		if(h) {
			createBåt(x,y,3,1);
		}
		else {
			createBåt(x,y,1,3);
		}
	}
	public void addPatruljebåt(int x, int y, boolean h) {
		if(h) {
			createBåt(x,y,2,1);
		}
		else {
			createBåt(x,y,1,2);
		}
	}
	
	public void initBoard() {
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				board[i][j] = new Cell();
			}
		}
	}
	
	public void printBoard() {
		System.out.println(" ---------------------------------------------------");
		for (int i = 0; i < 10; i++) {
			System.out.print("| ");
			for(int j = 0; j < 10; j++) {
				System.out.print("  " + board[i][j].toString() + "  ");
			}
			System.out.print("|");
			System.out.println();
		}
		System.out.println(" ---------------------------------------------------");
		System.out.println();
	}
	
	public void tryToHit(int x,int y) {
		board[x][y].hit();
		if(board[x][y].isHit()) {
			System.out.println("That's a hit!");
		}else {
			System.out.println("That's a miss...");
		}
		changePlayer();
	}
	
	private void changePlayer() {
		if(currentPlayer == 1) {
			currentPlayer = 2;
		}else {
			currentPlayer = 1;
		}
		//System.out.println("Player " + currentPlayer + "'s turn");
	}
	
	public void getInput(String in) {
		
	}
	
	public String toString() {
		String dots = " ---------------------------------------";
		String boardString = "";
		for (int i = 0; i < 10; i++) {
			boardString += "| ";
			for(int j = 0; j < 10; j++) {
				boardString += "  " + board[i][j].toString() + "  ";
			}
			boardString += "|\n";
		}
		return("Player " + currentPlayer + "'s turn\n" + dots + "\n" + boardString + dots);
	}
	
	public static void main(String[] args) {
		BattleshipBoard b = new BattleshipBoard();
		b.addSlagskip(2, 1, true);
		b.addHangarskip(2, 2, true);
		b.addFergatt(7, 3, true);
		b.addUbåt(5, 2, true);
		b.addPatruljebåt(3, 7, true);
		
		BattleshipBoard b2 = new BattleshipBoard();
		b2.addSlagskip(2, 1, true);
		b2.addHangarskip(2, 2, true);
		b2.addFergatt(7, 3, true);
		b2.addUbåt(5, 2, true);
		b2.addPatruljebåt(3, 7, true);
		
		b2.printBoard();
		b.tryToHit(2, 1);	
		
		
		b.printBoard();
		b2.tryToHit(2, 1);
	}
}
