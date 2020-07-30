package daos;

import java.util.ArrayList;

import modelo.Libro;

public class LibrosDAOimplArrayList implements LibrosDAO{

	private ArrayList<Libro> libros = new ArrayList<Libro>();
	
	public void ordenarLibros() {
		
	}
	
	@Override
	public void registrarLibro(Libro l) {
		libros.add(l);
	}

	@Override
	public ArrayList<Libro> obtenerLibros() {
		return libros;
	}

	@Override
	public void borrarLibro(int indice) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public Libro obtenerLibroPorIndice(int indice) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void actualizarLibroPorIndice(String autor, String titulo, double precio, int paginas, int indice) {
		// TODO Auto-generated method stub
		
	}
	

}
