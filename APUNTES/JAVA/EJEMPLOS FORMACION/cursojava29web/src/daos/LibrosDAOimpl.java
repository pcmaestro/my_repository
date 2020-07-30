package daos;

import java.util.List;

import model.Libro;

public class LibrosDAOimpl implements LibrosDAO {

	private final static String url = 
			"jdbc:mysql://localhost:3306/bd_java_libros";
	private final static String user = "root";
	private final static String pass = "root1234";
	
	public LibrosDAOImpl() {
		//cargo el driver de mysql
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			System.out.println("no pude cargar el driver");
		}
	}

	private void conectar() {
		
	}
	
	private void desconectar() {
		
	}

	@Override
	public void registrarLibro(Libro l) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public List<Libro> obtenerLibros() {
		// TODO Auto-generated method stub
		return null;
	}

}
