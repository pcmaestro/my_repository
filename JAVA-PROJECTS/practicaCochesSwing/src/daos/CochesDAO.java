package daos;

import java.util.ArrayList;

import modelo.Coche;

public interface CochesDAO {

	public void registrarCoche(Coche c);

	public ArrayList<Coche> listarCoches();

	public void borrarCoche(int index);

	public Coche obtenerCoche(int index);

	public void actualizarCoche(
			String marca, String modelo, String color, String motor, String cilindrada, String precio, int index
			);
}//end interfaz