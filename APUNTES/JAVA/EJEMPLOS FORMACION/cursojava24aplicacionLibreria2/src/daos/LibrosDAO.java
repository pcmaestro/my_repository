package daos;

import java.util.ArrayList;

import modelo.Libro;

public interface LibrosDAO {

	public void registrarLibro(Libro l);
	public ArrayList<Libro> obtenerLibros();
	public void borrarLibro(int indice);
	public Libro obtenerLibroPorIndice(int indice);
	public void actualizarLibroPorIndice(
			String autor, String titulo, double precio, int paginas, int indice);
	
}
