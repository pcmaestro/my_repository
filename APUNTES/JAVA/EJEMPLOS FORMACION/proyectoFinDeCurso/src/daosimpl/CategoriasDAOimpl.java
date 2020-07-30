package daosimpl;

import java.sql.ResultSet; 
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import daos.CategoriasDAO;
import model.Categoria;

public class CategoriasDAOimpl extends MasterDAO implements CategoriasDAO{

	@Override
	public List<Categoria> obtenerCategorias() {
		List<Categoria> categorias = new ArrayList<Categoria>();
		String sql = "select * from tabla_categorias_coches order by id asc";
		conectar();
		try {
			Statement st =conexion.createStatement();
			ResultSet rs = st.executeQuery(sql);
			while(rs.next()) {
				Categoria c = new Categoria();
				c.setId(rs.getInt(1));
				c.setCategoria(rs.getString(2));
				c.setDescripcion(rs.getString(3));
				categorias.add(c);
			}
		} catch (SQLException e) {
			System.out.println("Error en obtenerCategorias, revisar CategoriasDAOimpl-obtenerCategorias()");
			e.printStackTrace();
		}
		desconectar();
		return categorias;
	}//end obtenerCategorias

}//end class