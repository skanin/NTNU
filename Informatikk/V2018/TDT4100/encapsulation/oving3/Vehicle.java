package encapsulation;

import org.apache.commons.lang3.StringUtils;

public class Vehicle {
	
	
	private char type, fuel;
	private String registration;
	
	public Vehicle(char type, char fuel, String registration) {
		/*Is type correct?*/
		if(!(type == 'C' || type == 'M')) {
			throw new IllegalArgumentException("Incorrect type");
		}else {
			this.type = type;
		}
		
		/*Is fuel correct?*/
		if(!(fuel == 'H' || fuel == 'E' || fuel == 'G' || fuel == 'D')){
			throw new IllegalArgumentException("Incorrect fuel");
		}else{
			if(type == 'M' && fuel == 'H') {
				throw new IllegalArgumentException("Motorcycle can't run on Hydrogen");
			}else {
				this.fuel = fuel;
			}
		}
		
		/*Is reg correct?*/
		if((type == 'C' && !(registration.length() == 7)) || (type == 'M' && !(registration.length() == 6))) {
			throw new IllegalArgumentException("Wrong length");
		}
		String regChar = registration.substring(0,2);
		
		if(StringUtils.isNumeric(regChar.substring(0,1)) || StringUtils.isNumeric(regChar.substring(1,2))) {
			throw new IllegalArgumentException("First to items must be letters");
		}
		
		if(regChar != regChar.toUpperCase()) {
			throw new IllegalArgumentException("Must be uppercase");
		}
			
		String regNumb;
		
		if(this.type == 'C') {
			regNumb = registration.substring(2, 7);
			if(!StringUtils.isNumeric(regNumb)) {
				throw new IllegalArgumentException("last 5 must be numeric");
			}
		}else {
			regNumb = registration.substring(2, 6);
			if(!StringUtils.isNumeric(regNumb)) {
				throw new IllegalArgumentException("last 4 must be numeric");
			}
		}
		
		switch(fuel) {
		case 'H':
			if(!regChar.equals("HY")) {
				throw new IllegalArgumentException("With H as fuel, reg must start with HY");
			}else {
				this.registration = registration;
			}
			break;
		case 'E':
			if(!(regChar.equals("EK") || regChar.equals("EL"))) {
				throw new IllegalArgumentException("With E as fuel, reg must start with EK or EL");
			}else {
				this.registration = registration;
			}
			break;
		case 'D':
		case 'G':
			if(regChar.equals("HY") || regChar.equals("EK") || regChar.equals("EL") || regChar.matches(".*[A-Z]Æ") ||
			regChar.matches(".*[A-Z]Ø") || regChar.matches(".*[A-Z]Å")) {
				throw new IllegalArgumentException("With D or G as fuel, reg can't start with HY, EL, EK or contain Æ, Ø, Å");
			}else {
				this.registration = registration;
			}
			break;
		default:
			throw new IllegalArgumentException("Incorrect fuel");
		}
	}
	
	public void setRegistrationNumber(String reg) {
		/*Is reg correct?*/
		if((type == 'C' && !(reg.length() == 7)) || (type == 'M' && !(reg.length() == 6))) {
			throw new IllegalArgumentException("Wrong length");
		}
		String regChar = reg.substring(0,2);
		
		if(StringUtils.isNumeric(regChar.substring(0,1)) || StringUtils.isNumeric(regChar.substring(1,2))) {
			throw new IllegalArgumentException("First to items must be letters");
		}
		
		if(regChar != regChar.toUpperCase()) {
			throw new IllegalArgumentException("Must be uppercase");
		}
			
		String regNumb;
		
		if(type == 'C') {
			regNumb = reg.substring(2, 7);
			if(!StringUtils.isNumeric(regNumb)) {
				throw new IllegalArgumentException("last 5 must be numeric");
			}
		}else {
			regNumb = reg.substring(2, 6);
			if(!StringUtils.isNumeric(regNumb)) {
				throw new IllegalArgumentException("last 4 must be numeric");
			}
		}
		
		switch(fuel) {
		case 'H':
			if(!regChar.equals("HY")) {
				throw new IllegalArgumentException("With H as fuel, reg must start with HY");
			}else {
				registration = reg;
			}
			break;
		case 'E':
			if(!(regChar.equals("EK") || regChar.equals("EL"))) {
				throw new IllegalArgumentException("With E as fuel, reg must start with EK or EL");
			}else {
				registration = reg;
			}
			break;
		case 'D':
		case 'G':
			if(regChar.equals("HY") || regChar.equals("EK") || regChar.equals("EL") || regChar.matches(".*[A-Z]Æ") ||
			regChar.matches(".*[A-Z]Ø") || regChar.matches(".*[A-Z]Å")) {
				throw new IllegalArgumentException("With D or G as fuel, reg can't start with HY, EL, EK or contain Æ, Ø, Å");
			}else {
				registration = reg;
			}
			break;
		default:
			throw new IllegalArgumentException("Incorrect fuel");
		}
	}

	public String getRegistrationNumber() {
		return registration;
	}
	
	public char getFuelType() {
		return fuel;
	}
	
	public char getVehicleType() {
		return type;
	}
	
}
