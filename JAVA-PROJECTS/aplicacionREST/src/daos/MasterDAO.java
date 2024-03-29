package daos;

import java.sql.Connection; 
import java.sql.DriverManager;
import java.sql.SQLException;

public class MasterDAO {	
	
	private String URL = "jdbc:mysql://localhost:3306/bd_coches?serverTimezone=UTC";
	private String USER = "mysqluser";
	private String PASS = "1234";		
	protected Connection conexion;
	
	public void conectar() {
		
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");			
			conexion = DriverManager.getConnection(URL, USER, PASS);
			System.out.println("Conexion con BBDD establecida");				
			} catch (ClassNotFoundException e) {
				System.out.println("Error al cargar el driver de la BBDD");
				e.printStackTrace();
			} catch (SQLException e) {
				System.out.println("Error al conectar con la BBDD");
				e.printStackTrace();
			}
			
	}//end conectar
	
	public void desconectar() {
		
		try {
			conexion.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
}//end class
