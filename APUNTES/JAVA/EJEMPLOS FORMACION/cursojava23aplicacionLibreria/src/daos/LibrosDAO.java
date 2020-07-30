package daos;

import java.util.ArrayList;

import modelo.Libro;

public interface LibrosDAO {

	public void registrarLibro(Libro l);
	public ArrayList<Libro> obtenerLibros();
	
}
