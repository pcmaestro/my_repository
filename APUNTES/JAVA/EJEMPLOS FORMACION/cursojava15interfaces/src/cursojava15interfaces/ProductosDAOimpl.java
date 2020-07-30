package cursojava15interfaces;

public class ProductosDAOimpl implements ProductosDAO{

	@Override
	public void registrarProducto(String nombre, int codigo) {
		System.out.println("registrando producto...");
	}

	@Override
	public void borrarProducto(long id) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public int obtenerTotalProductos() {
		// TODO Auto-generated method stub
		return 0;
	}

}
