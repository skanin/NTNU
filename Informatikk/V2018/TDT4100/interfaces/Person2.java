package interfaces;

public class Person2 implements Named {
	
	String fullName;
	
	public Person2(String fullName) {
		this.fullName = fullName;
		
	}
	@Override
	public void setGivenName(String name) {
		this.fullName = name + " " + this.fullName.substring(fullName.indexOf(" ") + 1, fullName.length());
	}

	@Override
	public String getGivenName() {
		String parts[] = this.fullName.split(" ");
		return parts[0];
	}

	@Override
	public void setFamilyName(String name) {
		this.fullName = this.fullName.substring(0, fullName.indexOf(" ")) + " " + name;
	}

	@Override
	public String getFamilyName() {
		String parts[] = this.fullName.split(" ");
		return parts[1];
	}

	@Override
	public void setFullName(String name) {
		this.fullName = name;
	}

	@Override
	public String getFullName() {
		return this.fullName;
	}
}
