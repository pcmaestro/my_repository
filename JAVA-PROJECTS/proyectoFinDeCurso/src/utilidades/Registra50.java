package utilidades;

import daos.CochesDAO; 
import daosimpl.CochesDAOimpl;
import model.Coche;

public class Registra50 {
	public static void main(String[] args) {
		
		CochesDAO cochesDAO = new CochesDAOimpl();	
		Coche coche = new Coche();
		for (int i = 0; i < 50; i++) {
			coche.setMarca("Marca" + i);
			coche.setModelo("Modelo" + i);
			coche.setColor("color" + i );
			coche.setMotor("motor" + i);
			coche.setCilindrada(2000);
			coche.setPrecio(100000);
			coche.setTelefono(910000000);
			coche.setEmail("email"+i+"gmail.com");
			coche.setId_categoria(3);
			
			cochesDAO.registrarCoche(coche);
			System.out.println("registrando coche: " + i);
		}
	}
}
