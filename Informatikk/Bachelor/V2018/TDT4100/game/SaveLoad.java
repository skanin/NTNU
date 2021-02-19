package game;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;

public interface SaveLoad {
	public void save(String filename) throws FileNotFoundException;
	public void load(String filename) throws FileNotFoundException;
}
