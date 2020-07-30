package daosimpl;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import daos.CocheDAO;
import daos.MasterDAO;
import model.Coche;
import sql.Query;

public class CocheDAOimpl extends MasterDAO implements CocheDAO{

	@Override
	public ArrayList<Coche> obtenerCoches() {
		
		conectar();
		
		ArrayList<Coche> coches = new ArrayList<Coche>();
		
		String sql = Query.getSelect();
		
		try {
			Statement st = conexion.createStatement();
			ResultSet rs =  st.executeQuery(sql);
			while(rs.next()) {
				Coche c = new Coche();
				c.setId(rs.getInt(1));
				c.setMarca(rs.getString(2));
				c.setModelo(rs.getString(3));
				c.setColor(rs.getString(4));
				c.setMotor(rs.getString(5));
				c.setCilindrada(rs.getInt(6));
				c.setPrecio(rs.getInt(7));
				c.setTelefono(rs.getInt(8));
				c.setEmail(rs.getString(9));
				c.setId_categoria(rs.getInt(10));	
				coches.add(c);
			}
		} catch (SQLException e) {
			System.out.println("Fallo al ejecutar select");
			e.printStackTrace();
		}
		
		
		desconectar();
		
		return coches;
	}//end obtenerCoches


		@Override
		public Coche obtenerCochePorId(int id) {

			conectar();
			
			Coche coche = new Coche();
			
			String sql = Query.getSelectbyid();
			
			try {
				PreparedStatement ps = conexion.prepareStatement(sql);
				ps.setInt(1, id);
				ResultSet rs = ps.executeQuery();				
				while(rs.next()) {
					if(rs.getRow() != 0) {
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
					}//end if
				}//end while
			} catch (SQLException e) {
				System.out.println("Fallo en select by id");
				e.printStackTrace();
			}			
			
			desconectar();
			
			return coche;
		}//end obtenerCochePorId	


		@Override
		public void borrarCoche(int id) {
			
			conectar();
			
			String sql = Query.getDelete();
			
			try {
				PreparedStatement ps = conexion.prepareStatement(sql);
				ps.setString(1, Integer.toString(id));
				ps.executeUpdate();
			} catch (SQLException e) {
				System.out.println("Fallo al ejecutar DELETE");
				e.printStackTrace();
			}
			
			desconectar();
			
		}//end borrarCoche


		@Override
		public int registrarCoche(Coche coche) {
			
			conectar();			
			
			String sql = Query.getInsert();
			
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
				
				while(rs.next()) {
					idGenerado = rs.getInt(1);
					coche.setId(idGenerado);
				}
				
				
			} catch (SQLException e) {
				System.out.println("Fallo al ejecutar INSERT");				
				e.printStackTrace();
			}

			desconectar();
			
			return idGenerado;
			
		}//end registrarCoche


		@Override
		public int modificarCoche(int id, Coche cocheNew) {
			
			conectar();
			
			int modificacionOK = 0;
			
			CocheDAO c = new CocheDAOimpl();	

			Coche coche = c.obtenerCochePorId(id);
			
			//Antes de ejecutar la modificación, comprobamos si el id existe
			if(c.obtenerCochePorId(id).getId() > 0) {
				
				if(!coche.getMarca().equals(cocheNew.getMarca())) {
					coche.setMarca(cocheNew.getMarca());				
				}
				
				if(!coche.getModelo().equals(cocheNew.getModelo())) {
					coche.setModelo(cocheNew.getModelo());				
				}
				
				if(!coche.getColor().equals(cocheNew.getColor())) {
					coche.setColor(cocheNew.getColor());				
				}
				
				if(!coche.getMotor().equals(cocheNew.getMotor())) {
					coche.setMotor(cocheNew.getMotor());				
				}
				
				if(coche.getCilindrada() != cocheNew.getCilindrada()) {
					coche.setCilindrada(cocheNew.getCilindrada());
				}
				
				if(coche.getPrecio() != cocheNew.getPrecio()) {
					coche.setPrecio(cocheNew.getPrecio());
				}
				
				if(coche.getTelefono() != cocheNew.getTelefono()) {
					coche.setTelefono(cocheNew.getTelefono());
				}
				
				if(!coche.getEmail().equals(cocheNew.getEmail())) {
					coche.setEmail(cocheNew.getEmail());				
				}
				
				if(coche.getId_categoria() != cocheNew.getId_categoria()) {
					coche.setId_categoria(cocheNew.getId_categoria());
				}	
					
				String sql = Query.getUpdate();
				
				try {
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
					ps.setInt(10, id);
					ps.executeUpdate();
					modificacionOK = 1;
					
				} catch (SQLException e) {
					System.out.println("Fallo en ejecución de UPDATE");
					e.printStackTrace();
				}//end try-catch
				
			}//end if comprobacion si existe id
			
			desconectar();
			
			return modificacionOK;
			
		}//end modificarCoche
	

}//end class
