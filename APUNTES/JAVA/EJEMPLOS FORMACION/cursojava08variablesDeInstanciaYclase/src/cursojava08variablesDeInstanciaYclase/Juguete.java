package cursojava08variablesDeInstanciaYclase;

public class Juguete {

	private String nombre;
	private String color;
	private double precio;
	
	public int altura;
	public static String numeroSerie = "cod0001";
	

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

}
