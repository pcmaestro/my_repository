package cursojava30jdbcIncluyendoLibreria;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.TimeZone;

public class Main {

	public static void main(String[] args) {
		// ejemplo de conexion con base de datos

		// para cargar la libreria:
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			System.out.println("paso 1 ok");
			// establecer conexion con la base de datos

			String url = "jdbc:mysql://localhost:3306/bd_java_libros";
			// la siguiente linea solo para para la libreria version 8:
			url += "?serverTimezone=" + TimeZone.getDefault().getID();
			String usuario = "root";
			String pass = "root1234";
			Connection conexion = DriverManager.getConnection(url, usuario, pass);
			System.out.println("tenemos conexion con la bd");
			// ahora segun el tipo de sql que quiera lanzar tengo que hacer una cosa u otra

			// para insertar informacion:
			Libro l = new Libro("El Quijote", "Cervantes", 477, 12.5);
			// la no que no deberia usar:
//			Statement st = conexion.createStatement();
//			String sql = "insert into tabla_libros(autor,titulo,paginas,precio) " +
//			"values('"+l.getAutor()+"','"+l.getTitulo()+"','"+l.getNumeroPaginas()+
//			"','"+l.getPrecio()+"')";
//			System.out.println("voy a lanzar la sql: " + sql);
//			st.executeUpdate(sql);
//			System.out.println("sql de insercion lanzada");

			// lo siguiente es mucho mas seguro y menos lioso:
			String sql = "insert into tabla_libros(autor,titulo,paginas,precio) " + " values (?,?,?,?)";
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setString(1, l.getAutor());
			ps.setString(2, l.getTitulo());
			ps.setInt(3, l.getNumeroPaginas());
			ps.setDouble(4, l.getPrecio());
			ps.executeUpdate();
			System.out.println("registro ok");

			// para sacar informacion, si
			// la sql no tiene partes dependientes del usuario
			Statement st = conexion.createStatement();
			sql = "SELECT * FROM tabla_libros";
			ResultSet rs = st.executeQuery(sql);
			while (rs.next()) {
				System.out.println("id: " + rs.getInt("id") + " autor:  " + 
						rs.getString(2) + " titulo: " + rs.getString(3));
			}

			conexion.close();

		} catch (ClassNotFoundException e) {
			System.out.println("no pude cargar el driver de mysql");
		} catch (SQLException e) {
			System.out.println("error al conectar o al lanzar SQL");
			e.printStackTrace();// da mas informacion del error
		}

	}// end main

}// end class
