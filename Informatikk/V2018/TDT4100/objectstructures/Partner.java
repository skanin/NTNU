package objectstructures;

public class Partner {
	String name;
	Partner partner;
	
	public Partner(String name) {
		this.name = name;
	}
	
	public String getName() {
		if(this.partner == null) return null;
		return this.name;
	}
	
	Partner p = this.partner;
	/*public void setPartner(Partner partner) {
		if(this == partner) {
			throw new IllegalArgumentException("Partner can't be yourself");
		}else if(partner == null) {
			this.partner.partner = null;
			this.partner = null;
		}else if((this.partner != partner) && this.partner != null) {
			this.partner.partner = null;
			this.partner = partner;
			partner.partner = this;
		}
		else {
			if(!(this.partner == partner)) {
				this.partner = partner;
				partner.setPartner(this);
			}
			
		}
	}*/
	public void setPartner(Partner p) {
		if(this == p) {
			throw new IllegalArgumentException("Partner can't be yourself");
		}else if(this.partner == null) {
			this.partner = p;
			p.partner = this;
		}else if(this.partner != p && this.partner != null) {
			this.partner.partner = null;
			this.partner = p;
			p.partner = this;
		}
	}
	
	public Partner getPartner() {
		return partner;
	}
	
	public static void main(String[] args) {
		/*Partner p1 = new Partner("Sander");
		Partner p2 = new Partner("Marcus");
		Partner p3 = new Partner("Filip");
		
		p1.setPartner(p2);
		p1.setPartner(null);
		//p1.setPartner(p3);
		System.out.println("Name: " + p1.getName() + "\nPartner: " + p1.getPartner());*/
		Partner p1 = new Partner("Sander");
		Partner p2 = new Partner("Marcus");
		Partner p4 = new Partner("Filip");
		p1.setPartner(p2);
		System.out.println("P1: " + p1.partner.getName());
		System.out.println("P2: " + p2.partner.getName());
		p1.setPartner(null);
		System.out.println("P1: " + p1.partner.getName());
		p1.setPartner(p4);
		System.out.println("P1: " + p1.partner.getName());
		System.out.println("P2: " + p2.partner.getName());
		System.out.println("P4: " + p4.partner.getName());
	}
}
