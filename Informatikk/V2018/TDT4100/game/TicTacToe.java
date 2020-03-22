package game;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.Reader;
import java.util.EmptyStackException;
import java.util.Scanner;
import java.util.Stack;
import java.lang.*;

public class TicTacToe implements SaveLoad{
	
	private char[][] board;
	private char currentPlayerMark;
	private Stack<char[][]> redo;
	private	Stack<char[][]> undo;
	
	public TicTacToe() {
		board = new char[3][3];
		initBoard();
		currentPlayerMark = 'x';
		this.redo = new Stack<char[][]>();
		this.undo = new Stack<char[][]>();
	}
	
	public void addToUndo() {
		char[][] tempBoard = new char[3][3];
		for(int i = 0; i < tempBoard.length; i++) {
			for(int j = 0; j < tempBoard.length; j++) {
				tempBoard[i][j] = this.board[i][j];
			}
		}
		this.undo.push(tempBoard);
	}
	
	public void addToRedo() {
		char[][] tempBoard = new char[3][3];
		for(int i = 0; i < tempBoard.length; i++) {
			for(int j = 0; j < tempBoard.length; j++) {
				tempBoard[i][j] = this.board[i][j];
			}
		}
		this.redo.push(tempBoard);
	}
	
	public void redo() {
		try {
			if(redo.size() > 0 && this.board != redo.peek()) {
				addToUndo();
				this.board = redo.pop();
				changePlayer();
			}else {
				System.out.println("Can't redo");
			}
			
		}catch(EmptyStackException e) {
			System.out.println("Redo stack empty!");
		}
	}
	
	public void undo() {
		try {
			if(undo.size() > 0) {
				addToRedo();
				this.board = undo.pop();
				changePlayer();
			}
		}catch(EmptyStackException e) {
			System.out.println("Undo stack empty!");
		}
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
					boardString += board[i][j] + " | \n";
				}else {
					boardString += board[i][j] + " | ";
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
					this.board[x][y] = c;
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
		addToUndo();
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
	
	public void save(String fileName) throws FileNotFoundException {
		 try
	        {
	            PrintWriter file = new PrintWriter(fileName + "txt");
	            file.println(this.toString());
	            file.close();
	        }
	        catch (FileNotFoundException e)
	        {
	            System.err.println("Error: file could not be opened for writing.");
	            System.exit(1);
	        }
	         
	    }
	
	public void load(String fileName) throws FileNotFoundException {
		 Scanner in;
	        try
	        {
	            in = new Scanner(new FileReader(fileName + "txt"));
	            String emptyString = ""; 
	            while(in.hasNext()){
	                String line = in.nextLine();
	                if(line.contains("|")) {
	                		emptyString += line;
	                }
	                
	                System.out.println(line);
	            }
	            String emptyString2 = "";
	            for(int i = 0; i < emptyString.length(); i++) {
	            		char result = emptyString.charAt(i);
	            		if(result == ' ') {
	            			continue;
	            		}else {
	            			emptyString2 += result;
	            		}
	            }
	            String test3 = emptyString2.replaceAll("\\|", "").replaceAll("\\|", "");
	            int countX = emptyString2.length() - emptyString2.replace("x", "").length();
	            int countO = emptyString2.length() - emptyString2.replace("o", "").length();
	            if((countO > countX) && (currentPlayerMark == 'o')) {
	            		changePlayer();
	            }else if((countX > countO) && (currentPlayerMark == 'x')) {
	            		changePlayer();
	            }
	            char[] u = new char[9];
	            for(int i = 0; i < test3.length(); i++) {
	            		u[i] = test3.charAt(i);
	            }
	            char[][] y = new char[3][3];
	            
	            int row=3;
	            int col=3;
	            int i = 0;
	            for(int r=0; r<row; r++){
	            		for( int c=0; c<col; c++){
	                       y[r][c]=u[i++];
	              }
	            }
	            
	            for(int w = 0; w < board.length; w++) {
	            		for(int g = 0; g < board.length; g++) {
	            	   		board[w][g] = y[w][g];
	            	   	}
	            }
	            in.close();
	        }
	        catch (IOException e)
	        {
	            System.err.println("Error: file 'test.txt' could not be opened. Does it exist?");
	            System.exit(1);
	        }
	}
	
	public static void main(String[] args) {
		TicTacToe tic = new TicTacToe();
		tic.printBoard();
		tic.play(0, 0);
		tic.play(0, 1);
		tic.play(0, 2);
		tic.play(1, 1);
		tic.redo();
	}
}
