package stateandbehavior;

import javafx.fxml.FXML;
import javafx.scene.control.TextField;
import stateandbehavior.UpOrDownCounter;

public class UpOrDownCounterController {
	UpOrDownCounter cd;
	
	@FXML TextField startValue;
	@FXML TextField stopValue;
	@FXML TextField counterOutput;
	
	@FXML
	void handleClick() {
		String startString = startValue.getText();
		int start = Integer.valueOf(startString);
		String stopString = stopValue.getText();
		int stop = Integer.valueOf(stopString);
		
		cd = new UpOrDownCounter(start, stop);
		
		while(cd.count()) {
			try {
				System.out.println("Counter: " + String.valueOf(cd.getCounter()));
				counterOutput.setText(String.valueOf(cd.getCounter()));
				System.out.println(String.valueOf(cd.getCounter()));
				Thread.sleep(1000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}

