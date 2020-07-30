package daos;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import modelo.Libro;

public class LibrosDAOimplArchivo implements LibrosDAO {

	private static final String ARCHIVO = "datos.dat";
	ArrayList<Libro> libros = new ArrayList<Libro>();

	public LibrosDAOimplArchivo() {
		this.cargarArchivo();
	}

	private void cargarArchivo() {
		File f = new File(ARCHIVO);
		if (f.exists()) {
			try {
				FileInputStream fis = new FileInputStream(f);
				ObjectInputStream ois = new ObjectInputStream(fis);
				libros = (ArrayList<Libro>)ois.readObject();
				ois.close();
				fis.close();
				System.out.println("lectura del archivo correcta");
			} catch (IOException e) {
				System.out.println("no se pudo leer el archivo");
			} catch (ClassNotFoundException e) {
				System.out.println("no se encuentra la clase del objeto");
			}
		}// if (f.exists())
	}//end cargarArchivo
	
	
	private void escribirArchivo() {
		File f = new File(ARCHIVO);
		try {
			FileOutputStream fos = new FileOutputStream(f);
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			oos.writeObject(libros);
			oos.close();
			fos.close();
			System.out.println("escritura del archivo correcta");
		} catch (IOException e) {
			System.out.println("no pude escribir el archivo");
		}
	}

	@Override
	public void registrarLibro(Libro l) {
		libros.add(l);
		escribirArchivo();
	}

	@Override
	public ArrayList<Libro> obtenerLibros() {
		return libros;
	}

	@Override
	public void borrarLibro(int indice) {
		libros.remove(indice);
		escribirArchivo();
	}

	@Override
	public Libro obtenerLibroPorIndice(int indice) {
		return libros.get(indice);
	}

	@Override
	public void actualizarLibroPorIndice(String autor, String titulo, 
			double precio, int paginas, int indice) {
		Libro l = libros.get(indice);
		l.setAutor(autor);
		l.setTitulo(titulo);
		l.setPrecio(precio);
		l.setNumeroPaginas(paginas);
		escribirArchivo();
	}

}



















