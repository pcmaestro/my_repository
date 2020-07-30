package daos;

import java.util.List;

import modelo.Libro;

public interface LibrosDAO {
	
	public void registrarLibro(Libro l);
	public List<Libro> obtenerLibros();
	
}
