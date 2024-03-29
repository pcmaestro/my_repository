package daos;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import modelo.Coche;

public class CochesDAOimplArchivo implements CochesDAO {

	private static final String ARCHIVO = "datos.dat";
	ArrayList<Coche> coches = new ArrayList<Coche>();

	public CochesDAOimplArchivo() {

		this.cargarArchivo();

	}// end CochesDAOimplArchivo

	private void cargarArchivo() {

		File f = new File(ARCHIVO);

		if (f.exists()) {
			try {
				FileInputStream fis = new FileInputStream(f);
				ObjectInputStream ois = new ObjectInputStream(fis);
				coches = (ArrayList<Coche>) ois.readObject();
				ois.close();
				fis.close();
				System.out.println("lectura del archivo correcta");
			} catch (IOException e) {
				System.out.println("no se pudo leer el archivo");
			} catch (ClassNotFoundException e) {
				System.out.println("no se encuentra la clase del objeto");
			}

		} // end if

	}// end cargarArchivo

	private void escribirArchivo() {
		File f = new File(ARCHIVO);
		try {
			FileOutputStream fos = new FileOutputStream(f);
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			oos.writeObject(coches);
			oos.close();
			fos.close();
			System.out.println("escritura del archivo correcta");
		} catch (IOException e) {
			System.out.println("no pude escribir el archivo");
		}
	}

	@Override
	public void registrarCoche(Coche c) {

		coches.add(c);
		this.escribirArchivo();

	}// end registrarCoche

	@Override
	public ArrayList<Coche> listarCoches() {

		return coches;

	}// end listarCoches

	@Override
	public void borrarCoche(int indice) {

		coches.remove(indice);
		this.escribirArchivo();

	}// end borrarCoche

	@Override
	public Coche obtenerCoche(int indice) {
		
		return coches.get(indice);

	}// end ObtenerCoche

	@Override
	public void actualizarCoche(String marca, String modelo, String color, String motor, String cilindrada, String precio,
			int indice) {
		
		Coche c = coches.get(indice);
		
		c.setMarca(marca);
		c.setModelo(modelo);
		c.setColor(color);
		c.setMotor(motor);
		c.setCilindrada(cilindrada);
		c.setPrecio(precio);
		this.escribirArchivo();

	}// end actualizarCoche

}// end class
