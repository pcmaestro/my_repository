package daos;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.TimeZone;

import modelo.Libro;

public class LibrosDAOImpl implements LibrosDAO {
	
	private final static String url = 
			"jdbc:mysql://localhost:3306/bd_java_libros";
	private final static String urlAres = //solo para el profe
			"jdbc:mysql://localhost:3306/bd_java_libros"+
			"?serverTimezone=" + TimeZone.getDefault().getID();
	private final static String user = "root";
	private final static String pass = "root1234";
	
	
	private Connection conexion = null;
	
	public LibrosDAOImpl() {
		//cargo el driver de mysql
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			System.out.println("no pude cargar el driver");
		}
	}
	
	
	private void conectar() {
		try {
			conexion = DriverManager.getConnection(urlAres, user, pass);
		} catch (SQLException e) {
			System.out.println("no pude conectar con la base de datos");
			e.printStackTrace();
		}
	}

	private void desconectar() {
		try {
			conexion.close();
		} catch (SQLException e) {
			System.out.println("no pude desconectar");
		}
	}

	@Override
	public void registrarLibro(Libro l) {
		String sql = "insert into tabla_libros(autor,titulo,paginas,precio) " + " values (?,?,?,?)";
		PreparedStatement ps;
		conectar();
		try {
			ps = conexion.prepareStatement(sql);
			ps.setString(1, l.getAutor());
			ps.setString(2, l.getTitulo());
			ps.setInt(3, l.getNumeroPaginas());
			ps.setDouble(4, l.getPrecio());
			ps.executeUpdate();
		} catch (SQLException e) {
			System.out.println("excepcion tipo sql");
			e.printStackTrace();
		}
		desconectar();
	}

	@Override
	public List<Libro> obtenerLibros() {
		List<Libro> libros = new ArrayList<Libro>();
		Statement st;
		conectar();
		try {
			st = conexion.createStatement();
			String sql = "SELECT * FROM tabla_libros";
			ResultSet rs = st.executeQuery(sql);
			while (rs.next()) {
				Libro l = new Libro();
				l.setId(rs.getInt(1));
				l.setAutor(rs.getString(2));
				l.setTitulo(rs.getString(3));
				l.setNumeroPaginas(rs.getInt(4));
				l.setPrecio(rs.getInt(5));
				libros.add(l);
			}//end while
		} catch (SQLException e) {
			System.out.println("error al sacar listado de libros de BD");
		}		
		desconectar();
		return libros;
	}


	@Override
	public void borrarLibro(int id) {
		conectar();
		String sql = "DELETE FROM tabla_libros where id = ? ;";
		try {
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setInt(1, id);
			ps.executeUpdate();
		} catch (SQLException e) {
			System.out.println("error al borrar libro");
			e.printStackTrace();
		}
		desconectar();
	}


	@Override
	public Libro obtenerLibroPorId(int id) {
		Libro l = new Libro();
		conectar();
		String sql = "SELECT * FROM tabla_libros WHERE id = ? ";
		try {
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setInt(1, id);
			ResultSet rs = ps.executeQuery();
			if (rs.next()) {
				l.setId(rs.getInt(1));
				l.setAutor(rs.getString(2));
				l.setTitulo(rs.getString(3));
				l.setNumeroPaginas(rs.getInt(4));
				l.setPrecio(rs.getInt(5));
			}
		} catch (SQLException e) {
			System.out.println("error al obtenerLibroPorId");
			e.printStackTrace();
		}
		desconectar();
		return l;
	}


	@Override
	public void guardarCambiosLibro(Libro l) {
		conectar();
		String sql = "UPDATE tabla_libros set titulo = ? , autor = ? , "
				+ "paginas = ? , precio = ? WHERE id = ? ;";
		try {
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setString(1, l.getTitulo());
			ps.setString(2, l.getAutor());
			ps.setInt(3, l.getNumeroPaginas());
			ps.setDouble(4, l.getPrecio());
			ps.setInt(5, l.getId());
			ps.executeUpdate();
		} catch (SQLException e) {
			System.out.println("error en guardarCambiosLibro ");
			e.printStackTrace();
		}
		desconectar();		
	}//end guardarCambiosLibro

}
