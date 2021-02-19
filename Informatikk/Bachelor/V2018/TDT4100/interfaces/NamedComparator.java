package interfaces;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class NamedComparator implements Comparator<Named> {

	@Override
	public int compare(Named named1, Named named2) {
		if(named1.getFamilyName().compareTo(named2.getFamilyName()) == 0) {
			return named1.getGivenName().compareTo(named2.getGivenName());
		}else {
			return named1.getFamilyName().compareTo(named2.getFamilyName());
		}
	}
	public static void main(String[] args) {
		List<Named> liste = new ArrayList<Named>();
		Person1 p1 = new Person1("Sander", "Lindberg");
		Person2 p2 = new Person2("Marcus Henriksbø");
		
		System.out.println("P1: " + p1 + " " + p1.getGivenName());
		System.out.println("P2: " + p2 + " " + p2.getGivenName());
		liste.add(p1);
		liste.add(p2);
		
		System.out.println("Original: " + liste);
		Collections.sort(liste, new NamedComparator());
		System.out.println("Collections: " + liste);
	}
}
