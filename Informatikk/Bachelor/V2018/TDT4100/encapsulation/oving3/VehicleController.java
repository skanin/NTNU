package encapsulation;

import javafx.fxml.FXML;

import javafx.scene.control.TextField;

import javafx.scene.text.Text;
import java.awt.Button;

import encapsulation.Vehicle;

public class VehicleController {
	Vehicle v;
	
	@FXML Text typeText;
	@FXML Text fuelText;
	@FXML Text regText;
	@FXML TextField typeInp;
	@FXML TextField fuelInp;
	@FXML TextField regInp;
	@FXML Button regBtn;
	
	@FXML
	public void handleClick() {
		String type = typeInp.getText();
		String fuel = fuelInp.getText();
		String reg = regInp.getText();
		
		char charType = type.charAt(0);
		char charFuel = fuel.charAt(0);
		
		
		
		v = new Vehicle(charType, charFuel, reg);
				
		typeText.setText(String.valueOf(type));
		fuelText.setText(String.valueOf(fuel));
		regText.setText(reg);
		typeText.setVisible(true);
		fuelText.setVisible(true);
		regText.setVisible(true);		
	}
}
