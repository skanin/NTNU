package interfaces;

public class Person1 implements Named {
	
	String givenName;
	String familyName;
	
	public Person1 (String givenName, String familyName) {
		setGivenName(givenName);
		setFamilyName(familyName);
	}
	@Override
	public void setGivenName(String name) {
		this.givenName = name;
	}

	@Override
	public String getGivenName() {
		return givenName;
	}

	@Override
	public void setFamilyName(String name) {
		this.familyName = name;
	}

	@Override
	public String getFamilyName() {
		return familyName;
	}

	@Override
	public void setFullName(String name) {
		String parts[] = name.split(" ");
		this.givenName = parts[0];
		this.familyName = parts[1];
	}
	@Override
	public String getFullName() {
		return givenName + " " + familyName;
	}
	
}
