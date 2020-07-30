package daosimpl;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public abstract class MasterDAO {
	
	private static final String URL = "jdbc:mysql://localhost:3306/bd_coches";

	private static final String USER = "root";

	private static final String PASSWORD = "";
	
	protected Connection conexion = null;
	
	public MasterDAO() {
		System.out.println("se ejecuta el constructor de MasterDAO");
		//Cargando el driver de MySQL
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			System.out.println("No se ha podido cargar el driver de la BBDD - revisar clase MasterDAO");
			e.printStackTrace();
		}//end carga Driver
	}//end constructor
	
	protected void conectar(){
		try {
			conexion = DriverManager.getConnection(URL, USER, PASSWORD);
			System.out.println("Conexion con la BBDD correcta");
		} catch (SQLException e) {
			System.out.println("No se ha podido conectar con la BBDD, revisar clase MasterDAO-conectar()");
			e.printStackTrace();
		}
	}//end conectar
	
	protected void desconectar() {
		try {
			conexion.close();
		} catch (SQLException e) {
			System.out.println("No se ha podido desconectar la BBDD, revisar clase MasterDAO-desconectar()");
			e.printStackTrace();
		}
		
	}//end desconectar

}//end class
