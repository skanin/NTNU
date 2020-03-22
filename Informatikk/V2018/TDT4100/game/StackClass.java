package game;

import java.util.*;

public class StackClass {
	private Stack<TicTacToe> undo;
	private Stack<TicTacToe> redo;
	TicTacToe game;
	
	public StackClass(TicTacToe game) {
		this.game = game;
		this.undo = new Stack<TicTacToe>();
		undo.push(this.game);
		this.redo = new Stack<TicTacToe>();
	}
	
	public void move(TicTacToe board) {
		undo.push(this.game);
		redo.clear();
		game = board;
	}
	
	public TicTacToe undo() {
		redo.push(game);
		game = undo.pop();
		return game;
	}
	
	public TicTacToe redo() {
		undo.push(game);
		game = redo.pop();
		return game;
	}
	
	public static void main(String[] args) {
		TicTacToe t = new TicTacToe();
		StackClass s = new StackClass(t);
		t.printBoard();
		t.play(0, 0);
		s.move(t);
		t.play(0, 1);
		s.move(t);
		t.play(0, 2);
		s.move(t);
		s.undo();
		System.out.println(s.game);
	}
}
