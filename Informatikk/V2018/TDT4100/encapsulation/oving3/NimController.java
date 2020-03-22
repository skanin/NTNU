package encapsulation;

import javafx.fxml.FXML;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.TextField;
import javafx.scene.paint.Color;
import javafx.scene.text.Text;


public class NimController {
	
	private Nim nim; //Klassen min brukes her
	
	@FXML private Text pile1;
	@FXML private Text pile2;
	@FXML private Text pile3;
	@FXML private Text gameState;
	
	@FXML private TextField pileSizeField;
	@FXML private TextField numberField;
	
	@FXML private Text feedbackText;
	@FXML private ChoiceBox<String> targetPileChoice; 
	
	@FXML
	public void initialize() {
		nim = new Nim(); //Lages en ny instans av klassen min
		update();
	}
	
	@FXML
	public void newGame() {
		if (pileSizeField.getText() != null && (! pileSizeField.getText().trim().isEmpty())) {
			int pileSize = Integer.valueOf(pileSizeField.getText());
			nim = new Nim(pileSize); //Lager nytt spill med bestemt pile size
		}
		else {
			nim = new Nim(); //Lager nytt spill med ubestemt pile size (10)
		}
		update();
	}
	
	@FXML
	public void removePieces(){
		if (numberField.getText() == null || numberField.getText().isEmpty()) {
			return;
		}
		int number = Integer.valueOf(numberField.getText());
		int targetPile = Integer.valueOf(targetPileChoice.getValue()) - 1;
		
		// Her brukes klassen til å sjekke om et trekk er lovlig og deretter utføre det
		if (nim.isValidMove(number, targetPile)) {
			nim.removePieces(number, targetPile);
			feedbackText.setText(String.format("Removed %d pieces.", number));
			update();
		} else {
			feedbackText.setText("Illegal move!");
		}
	}
	
	@FXML
	private void update() {
		// Her brukes den til å sette teksten til antall brikker som er igjen i pilsene.
		pile1.setText(Integer.toString(nim.getPile(0)));
		pile2.setText(Integer.toString(nim.getPile(1)));
		pile3.setText(Integer.toString(nim.getPile(2)));
		
		gameState.setText("Game " + (nim.isGameOver() ? "over!" : "active"));
		gameState.setFill(nim.isGameOver() ? Color.RED : Color.WHITE);
	}
	
	
}
