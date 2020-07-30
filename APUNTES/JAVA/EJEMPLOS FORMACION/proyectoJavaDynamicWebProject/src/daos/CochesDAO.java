package daos;

import java.util.List;

import model.Coche;

public interface CochesDAO {

	public int registrarCoche(Coche c);

	public List<Coche> obtenerCoches(String marca, String modelo, String color, int comienzo, int cuantos);
	
	public void borrarCoche(int id);

	public Coche obtenerCochePorId(int id);

	public void guardarCambiosCoche(Coche c);
	
	public int totalCoches(String marca, String modelo, String color);
}// end interfaz