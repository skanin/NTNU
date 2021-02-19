package encapsulation;

public class Nim {
	
	int pileSize, pileOne, pileTwo, pileThree;
	
	public Nim() {
		this.pileSize = 10;
		pileOne = pileTwo = pileThree = this.pileSize;
		
	}
	
	public Nim(int pileSize) {
		if(pileSize > 0){
			this.pileSize = pileSize;
			pileOne = pileTwo = pileThree = this.pileSize;
		}
	}
	
	public void removePieces(int number, int targetPile) {
		System.out.println("Remove Number: " + number);
		System.out.println("Remove Target Pile: " + targetPile);
		if(isGameOver()) {
			throw new IllegalStateException("Game is already over");
		}
		
		if(isValidMove(number, targetPile)) {
			switch(targetPile) {
			case 0:
				if(number <= pileOne) {
					pileOne -= number;
				}else {
					throw new IllegalArgumentException("Number is invalid");
				}
				
				break;
			case 1:
				if(number <= pileTwo) {
					pileTwo -= number;
				}else {
					throw new IllegalArgumentException("Number is invalid");
				}
				break;
			case 2:
				if(number <= pileThree) {
					pileThree -= number;
				}else {
					throw new IllegalArgumentException("Number is invalid");
				}
				break;
			default:
				throw new IllegalArgumentException("Target pile is invalid");
			}
		}else {
			throw new IllegalArgumentException("Number is invalid");
		}
	}
	
	protected boolean isValidMove(int number, int targetPile) {
		if(number >= 1 && !isGameOver()) {
			if(targetPile == 0) {
				if(number <= pileOne) {
					return true;
				}else {
					return false;
				}
			}else if (targetPile == 1) {
				if(number <= pileTwo) {
					return true;
				}else {
					return false;
				}
			}else if (targetPile == 2) {
				if(number <= pileThree) {
					return true;
				}else {
					return false;
				}
			}
			return false;
		}
		return false;
	}
	
	public boolean isGameOver() {
		if(pileOne == 0 || pileTwo == 0 || pileThree == 0) {
			return true;
		}
		return false;
	}
	
	public int getPile(int targetPile) {
		switch(targetPile) {
		case 0:
			return pileOne;
		case 1:
			return pileTwo;
		case 2:
			return pileThree;
		default:
			throw new IllegalArgumentException("Target pile is invalid");
		}
	}
	public static void main(String[] args) {
		Nim o = new Nim();
		o.removePieces(5, 0);
		System.out.println(o.isValidMove(2, 10));
	}
}
