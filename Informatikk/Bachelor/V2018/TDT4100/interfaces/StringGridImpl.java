package interfaces;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class StringGridImpl implements StringGrid {
	
	private int rows, columnCount;
	//public List<List<String>> grid = new ArrayList<>();
	public ArrayList<ArrayList<String>> grid = new ArrayList<>();
	
	public StringGridImpl(int rows, int columnCount) {
		this.rows = rows;
		this.columnCount = columnCount;
		for(int i = 0; i < rows; i++) {
			grid.add(new ArrayList<>());
			for(int j = 0; j < columnCount; j++) {
				grid.get(i).add(null);
			}
		}
	}
	@Override
	public int getRowCount() {
		return rows;
	}

	@Override
	public int getColumnCount() {
		return columnCount;
	}

	@Override
	public String getElement(int row, int column) {
		if(row > this.rows || row < 0 || column > this.columnCount || column < 0) {
			throw new IllegalArgumentException("Row or column out of range");
		}
		return grid.get(row).get(column);
	}

	@Override
	public void setElement(int row, int column, String element) {
		if(row > this.rows || row < 0 || column > this.columnCount || column < 0) {
			throw new IllegalArgumentException("Row or column out of range");
		}
		grid.get(row).set(column, element);
	}
	public static void main(String[] args) {
		StringGridImpl s = new StringGridImpl(10, 10);
		s.setElement(1, 1, "Yo");
	}
	
	@Override
	public Iterator<String> iterator() {
		// TODO Auto-generated method stub
		return null;
	}
}
