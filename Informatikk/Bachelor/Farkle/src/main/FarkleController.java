package main;

import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class FarkleController {
	
	@FXML
	TextArea scoreArea;
	
	@FXML
	TextField player1, player2;
	
	Player p1;
	Player p2;
	
	Game g;
	
	public void setPlayerScore() {
		scoreArea.setText("Score:\n\n" + p1 + ": " + p1.getScore() + "\n\n" + p2 + ": " + p2.getScore());
	}
	
	public void newGame() {
		p1 = new Player(player1.getText());
		p2 = new Player(player2.getText());
		
		g = new Game(p1, p2);
		g.init();
		setPlayerScore();
	}
	
}
