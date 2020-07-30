package utilidades;

public class Registra50 {
	public static void main(String[] args) {
		LibrosDAO librosDAO = new LibrosDAOImpl();
		Libro l = new Libro("", "", 150, 9.5);
		for (int i = 0; i < 50; i++) {
			l.setTitulo("titulo" + i);
			l.setAutor("titulo" + i);
			librosDAO.registrarLibro(l);
			System.out.println("registrando libro: " + i);
		}
	}
}


