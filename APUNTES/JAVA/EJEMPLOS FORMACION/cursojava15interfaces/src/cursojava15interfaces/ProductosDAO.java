package cursojava15interfaces;

//en un interfaz se ponen los metodos que tiene que tener otra clase
//por eso, dichos metodos aqui no tienen codigo.
public interface ProductosDAO {
			
	void registrarProducto(String nombre, int codigo);
	void borrarProducto(long id);
	int obtenerTotalProductos();
	
}
