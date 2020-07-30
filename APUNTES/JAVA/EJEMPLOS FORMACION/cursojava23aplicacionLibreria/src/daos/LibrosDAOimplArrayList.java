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
	

}
