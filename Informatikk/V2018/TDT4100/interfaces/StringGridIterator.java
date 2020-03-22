package interfaces;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class StringGridIterator implements Iterator<String> {
	
	private StringGrid strGrid;
	private boolean rowMajor;
	private int currentRow;
	private int currentColumn;
	
	public StringGridIterator(StringGrid strGrid, boolean rowMajor) {
		this.strGrid = strGrid;
		this.rowMajor = rowMajor;
		this.currentColumn = 0;
		this.currentRow = 0;
	}
	
	@Override
	public boolean hasNext() {
		return currentColumn < strGrid.getColumnCount() && currentRow < strGrid.getRowCount();
	}
	
	@Override
	public String next() {
		if(! hasNext()) throw new NoSuchElementException();
		
		String result = strGrid.getElement(currentRow, currentColumn);
		
		if(rowMajor) {
			currentColumn++;
			if(currentColumn >= strGrid.getColumnCount()) {
				currentColumn = 0;
				currentRow++;
			}
		}else {
			currentRow++;
			if(currentRow >= strGrid.getRowCount()) {
				currentRow = 0;
				currentColumn++;
			}
		
		}
		return result;
	}
}
