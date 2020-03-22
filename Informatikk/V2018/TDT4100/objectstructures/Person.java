package objectstructures;

import java.util.ArrayList;
import java.util.List;

public class Person {
	
	String name;
	char gender;
	Person mother, father, child;
	List<Person> childs = new ArrayList<Person>();
	
	public Person(String name, char gender) {
		if(gender == 'F' || gender == 'M') {
			this.gender = gender;
		}else {
			throw new IllegalArgumentException("Gender must be M or F");
		}
		this.name = name;
	}
	
	public String getName() {
		return name;
	}
	
	public char getGender() {
		return gender;
	}
	
	public Person getMother() {
		if(this.mother == null) return null;
		return mother;
	}
	
	public Person getFather() {
		if(this.father == null) return null;
		return father;
	}
	
	public int getChildCount() {
		return childs.size();
	}
	
	public Person getChild(int n) {
		if(n < 0 || n > childs.size()) 
			throw new IllegalArgumentException("N is too high or too low");
		return childs.get(n);
	}
	
	public void addChild(Person child) {
		if(child.getMother() == null && this.gender == 'F') {
			child.mother = this;
			this.childs.add(child);
		}else if(child.getFather() == null && this.gender == 'M') {
			child.father = this;
			this.childs.add(child);
			
		}else if(child.getFather() != null && this.gender == 'M') {
			child.getFather().removeChild(child);
			child.father = this;
			this.childs.add(child);
		}else if(child.getMother() != null && this.gender == 'F') {
			child.getMother().removeChild(child);
			child.mother = this;
			this.childs.add(child);
		}
	}
	
	public void removeChild(Person child) {
		if(this.gender == 'F') {
			child.mother = null;
			for(int i = 0; i < childs.size(); i++) {
				if(childs.get(i) == child) {
					childs.remove(i);
				}
			}
		}else {
			child.father = null;
			for(int i = 0; i < childs.size(); i++) {
				if(childs.get(i) == child) {
					childs.remove(i);
				}
			}
		}
	}
	
	public void setMother(Person mother) {
		if(mother == this) {
			throw new IllegalArgumentException("You cannot be your own mother");
		}else if(mother.getGender() != 'F') {
			throw new IllegalArgumentException("Mother must be female");
		}
		else if(this.mother == null) {
			this.mother = mother;
			mother.addChild(this);
		}else if (this.mother != mother) {
			this.mother.removeChild(this);
			this.mother = mother;
			mother.addChild(this);
		}
		
	}
	
	public void setFather(Person father) {
		if(father == this) {
			throw new IllegalArgumentException("You cannot be your own father");
		}else if(father.getGender() == 'F') {
			throw new IllegalArgumentException("Father must be male");
		}else if(this.father == null) {
			this.father = father;
			father.addChild(this);
		}else if(this.father != father) {
			this.father.removeChild(this);
			this.father = father;
			father.addChild(this);
		}
	}
}
