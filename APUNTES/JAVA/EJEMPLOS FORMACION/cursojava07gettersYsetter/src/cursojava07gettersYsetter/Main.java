package cursojava07gettersYsetter;

public class Main {

	public static void main(String[] args) {
		
		Producto p1 = new Producto();
		p1.setNombre("Vestido");
		p1.setPrecio(19.99);
		
		Producto p2 = new Producto("zapatos" , 3.99);
		
		System.out.println("productos disponibles:");
		System.out.println( p1.getNombre() );
		System.out.println( p2.getNombre() );
		
	}

}
