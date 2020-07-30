package daosimpl;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import daos.CochesDAO;
import model.Categoria;
import model.Coche;

public class CochesDAOimpl extends MasterDAO implements CochesDAO {

	@Override
	public int registrarCoche(Coche coche) {

		String sql = "insert into tabla_coches (marca, modelo, color, motor, cilindrada, precio, telefono, email, id_categoria)"
				+ "values (? ,? ,? ,? ,? ,? ,? ,?, ?)";

		conectar();
		System.out.println("registrarCoche() conecta con la BBDD");
		int idGenerado = -1;
		
		try {
			PreparedStatement ps = conexion.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);			
			ps.setString(1, coche.getMarca());
			ps.setString(2, coche.getModelo());
			ps.setString(3, coche.getColor());
			ps.setString(4, coche.getMotor());
			ps.setInt(5, coche.getCilindrada());
			ps.setInt(6, coche.getPrecio());
			ps.setInt(7, coche.getTelefono());
			ps.setString(8, coche.getEmail());
			ps.setInt(9, coche.getId_categoria());			
			ps.executeUpdate();
			
			ResultSet rs = ps.getGeneratedKeys();
			if (rs.next()) {
				idGenerado = rs.getInt(1);
			}//end if
			
		} catch (SQLException e) {
			System.out.println("Fallo en insert SQL, revisar clase CochesDAOimpl-registrarCoche()");
			e.printStackTrace();
		}//end insert SQL
		
		desconectar();
		
		return idGenerado;

	}// end registrarCoche
	
	@Override
	public List<Coche> obtenerCoches(String marca, String modelo, String color, int comienzo, int cuantos) {
		List<Coche> coches = new ArrayList<Coche>();
		conectar();	
		System.out.println("obtenerCoches() conecta con la BBDD");
		try {
			String sql = "SELECT tc.id , tc.marca, tc.modelo, tc.color, tc.motor, tc.cilindrada, tc.precio, "+
					"tc.telefono, tc.email, cat.categoria from tabla_coches as tc, tabla_categorias_coches as cat "+
					"where tc.id_categoria = cat.id and tc.marca like ? and tc.modelo like ? and tc.color like ? "+
					"order by tc.id desc limit ?, ?;";
			
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setString(1, "%" + marca + "%");
			ps.setString(2, "%" + modelo + "%");
			ps.setString(3, "%" + color + "%");
			ps.setInt(4, comienzo);
			ps.setInt(5, cuantos);
			ResultSet rs = ps.executeQuery();
			System.out.println("select ejecutada correctamente");
			System.out.println(ps);
			while (rs.next()) {
				Coche coche = new Coche();
				coche.setId(rs.getInt(1));
				coche.setMarca(rs.getString(2));
				coche.setModelo(rs.getString(3));
				coche.setColor(rs.getString(4));
				coche.setMotor(rs.getString(5));
				coche.setCilindrada(rs.getInt(6));
				coche.setPrecio(rs.getInt(7));
				coche.setTelefono(rs.getInt(8));
				coche.setEmail(rs.getString(9));
				
				Categoria c = new Categoria();
				c.setCategoria(rs.getString(10));
				coche.setCategoria(c);
				
				coches.add(coche);
				
			}//end while
			
		} catch (SQLException e) {
			System.out.println("No han podido obtenerse los anuncios, revisar clase CochesDAOimpl-obtenerCoches()");
			e.printStackTrace();
		}//end select SQL

		desconectar();
		
		return coches;
		
	}//end obtenerCoches

	
	public void borrarCoche(int id) {
		conectar();
		String sql = "delete from tabla_coches where id = ?;";
		try {
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setInt(1, id);
			ps.executeUpdate();
		} catch (SQLException e) {
			System.out.println("No se ha podido borrar el anuncio, revisar clase CochesDAO-borrarCoche()");
			e.printStackTrace();
		}

		desconectar();
	}// end borrarCoche

	@Override
	public Coche obtenerCochePorId(int id) {
		Coche coche = new Coche();
		conectar();
		String sql = "select * from tabla_coches where id = ?;";
		try {
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setInt(1, id);
			ResultSet rs = ps.executeQuery();
			if (rs.next()) {
				coche.setId(rs.getInt(1));
				coche.setMarca(rs.getString(2));
				coche.setModelo(rs.getString(3));
				coche.setColor(rs.getString(4));
				coche.setMotor(rs.getString(5));
				coche.setCilindrada(rs.getInt(6));
				coche.setPrecio(rs.getInt(7));
				coche.setTelefono(rs.getInt(8));
				coche.setEmail(rs.getString(9));
				coche.setId_categoria(rs.getInt(10));
			}
		} catch (SQLException e) {
			System.out.println("Error al obtener coche por Id, revisar clase CochesDAOimpl-obtenerCochePorId()");
			e.printStackTrace();
		}

		desconectar();

		return coche;
	}//end obtenerCochePorId

	@Override
	public void guardarCambiosCoche (Coche coche){

		conectar();

		String sql = "update tabla_coches set marca = ? , modelo = ? , color = ? , motor = ?, "+
				"cilindrada = ?, precio = ?, telefono = ?, email = ?, id_categoria = ? where id = ?;";
		
		try {
			System.out.println("Ejecutando el update SQL");
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setString(1, coche.getMarca());
			ps.setString(2, coche.getModelo());
			ps.setString(3, coche.getColor());
			ps.setString(4, coche.getMotor());
			ps.setInt(5, coche.getCilindrada());
			ps.setInt(6, coche.getPrecio());
			ps.setInt(7, coche.getTelefono());
			ps.setString(8, coche.getEmail());
			ps.setInt(9, coche.getId_categoria());
			ps.setInt(10, coche.getId());
			ps.executeUpdate();
			System.out.println("update SQL ejecutada");
		} catch (SQLException e) {
			System.out.println("No se ha podido modificar el anuncio, revisar clase CochesDAOimpl-guardarCambiosCoche()");
			e.printStackTrace();
		}

		desconectar();

	}// end guardarCambiosCoche
	
	
	//Método que devuelve el total de anuncios con la marca, modelo y color
	//seleccionados, devuelve -1 si no puede hacerlo
	@Override
	public int totalCoches(String marca, String modelo, String color) {
		int total = -1;
		
		conectar();
		
		String sql = "select count(id) from tabla_coches where marca like ? and modelo like ? "+
					"and color like ?;";

		try {
			PreparedStatement ps = conexion.prepareStatement(sql);
			ps.setString(1, "%"+ marca +"%");
			ps.setString(2, "%"+ modelo +"%");
			ps.setString(3, "%"+ color +"%");
			ResultSet rs = ps.executeQuery();
			if(rs.next()) {
				total = rs.getInt(1);
			}
		} catch (SQLException e) {
			System.out.println("Error al obtener el total de anuncios, revisar clase CochesDAOimpl-totalCoches()");
			e.printStackTrace();
		}
		
		desconectar();
		
		return total;
	}//end totalCoches


}// end class
