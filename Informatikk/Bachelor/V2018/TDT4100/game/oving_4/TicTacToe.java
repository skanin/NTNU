package game;

public class TicTacToe {
	
	private char[][] board;
	private char currentPlayerMark;
	
	public TicTacToe() {
		board = new char[3][3];
		initBoard();
		currentPlayerMark = 'x';
		
	}
	
	
	public void initBoard() {
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				board[i][j] = '-';
			}
		}
	}
	
	public void printBoard() {
		System.out.println("-------------");
		for(int i = 0; i < 3; i++) {
			System.out.print("| ");
			for(int j = 0; j < 3; j++) {
					System.out.print(board[i][j] + " | ");
			}
			System.out.println();
			System.out.println("-------------");
		}
		System.out.println();
	}
	
	public String toString() {
		String dots = "-------------";
		String boardString = "";
		for(int i = 0; i < 3; i++) {
			boardString += "| ";
			for(int j = 0; j < 3; j++) {
				if(j == 2) {
					boardString += board[i][j] + "  |  \n";
				}else {
					boardString += board[i][j] + "  |  ";
				}
			}
		}
		return (dots + "\n" + boardString + dots);
	}

	public boolean isBoardFull() {
		boolean isFull = true;
		
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				if(board[i][j] == '-') {
					isFull = false;
				}
			}
		}
		return isFull;
	}
	
	public void changePlayer() {
		if(currentPlayerMark == 'x') {
			currentPlayerMark = 'o';
		}else {
			currentPlayerMark = 'x';
		}
	}
	

	
	public char getCell(int x, int y) {
		return board[x][y];
	}
	
	public boolean setCell(char c, int x, int y) {
		if(hasWinner()) {
			System.out.println("Game is already over!");
			return false;
		}
		if(x >= 0 && y < 3) {
			if(y >= 0 && x <= 3) {
				if(!isOccupied(x, y)) {
					board[x][y] = c;
					printBoard();
					if(hasWinner()) {
						System.out.println("We have a winner!");
						return false;
					}else if(isBoardFull()) {
						System.out.println("Game Over!");
						return false;
					}
					changePlayer();
					return true;
				}
			}
		}
		System.out.println("You can't place here (" + String.valueOf(x) + ", " + String.valueOf(y) + ")");
		return false;
	}
	
	public boolean isOccupied(int x, int y) {
		if(!(board[x][y] == '-')) {
			return true;
		}
		return false;
	}
	
	public char getCurrentPlayer() {
		return currentPlayerMark;
	}
	
	
	
	public void play(int x, int y) {
		setCell(getCurrentPlayer(), x, y);
	}
	
	private boolean checkRowAndCol(char c1, char c2, char c3) {
		return((c1 != '-') && (c1 == c2) && (c1 == c3));
	}
	
	private boolean checkRowWin() {
		for(int i = 0; i < 3; i++) {
			if(checkRowAndCol(board[i][0], board[i][1], board[i][2]) == true) {
				return true;
			}
		}
		return false;
	}
	
	private boolean checkColWin() {
		for(int i = 0; i < 3; i++) {
			if(checkRowAndCol(board[0][i], board[1][i], board[2][i]) == true) {
				return true;
			}
		}
		return false;
	}
	
	private boolean checkDiagonalForWin() {
		return ((checkRowAndCol(board[0][0], board[1][1], board[2][2]) || checkRowAndCol(board[0][2], board[1][1], board[2][0]))
				== true);
	}
	
	public boolean isWinner(char c) {
		for(int i = 0; i < 3; i ++) {
			if(checkRowWin() && (board[i][0] == c)) {
				return true;
			}else if(checkColWin() && (board[0][i] == c)) {
				System.out.println(c);
				System.out.println(board[i][0]);
				return true;
			}else if(checkDiagonalForWin() && (board[1][1] == c)) {
				return true;
			}
		}
		return false;
	}
	
	public boolean hasWinner() {
		if(isWinner('x') || isWinner('o')) {
			return true;
		}
		return false;
	}
	
	public boolean isFinished() {
		if(isBoardFull() || hasWinner()) {
			return true;
		}
		return false;
	}
	
	public void getInput(String in) {
		String xVal = in.substring(0,1);
		String yVal = in.substring(1,2);
		
		Integer x = Integer.valueOf(xVal);
		Integer y = Integer.valueOf(yVal);
		
		
		play(x, y);
	}
	
	public static void main(String[] args) {
		TicTacToe tic = new TicTacToe();
		tic.printBoard();
		tic.play(0, 0);
		tic.play(0, 1);
		tic.play(1, 0);
		tic.play(0, 2);
		tic.play(2, 0);
		System.out.println(tic.isWinner('x'));
		System.out.println(tic.toString());
		String f = "12";
		String e = f.substring(0,1);
		String g = f.substring(1,2);
		System.out.println(e);
		System.out.println(g);
	}
}
