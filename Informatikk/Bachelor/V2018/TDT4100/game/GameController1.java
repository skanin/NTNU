	package game;


import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;

public class GameController1 {


	@FXML
	TextArea console ;

	@FXML
	TextField inputField ;

	//Her maa du deklarerere spillet ditt dersom det heter noe annet enn TicTacToe
	BattleshipBoard b1;
	BattleshipBoard b2;

	public void initialize(){
		//Her maa du opprette et objekt av spillet ditt med de argumentene som behoves for det - resten av koden vil gaa ut ifra at du har kalt den game
		b1 = new BattleshipBoard();
		b2 = new BattleshipBoard();
		console.setText(b2.toString());
	}


	@FXML
	public void sendInput(){
		String in = inputField.getText();
		System.out.println(in);
		//Denne metoden kan hete hva som helst, men husk aa endre det her
		b1.getInput(in);
		console.setText(b1.toString());

	}
}
