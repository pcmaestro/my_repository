package model;


public class Coche {
	private int id;
	private String marca;
	private String modelo;
	private String color;
	private String motor;
	private int cilindrada;
	private int precio;
	private int telefono;
	private String email;
	
	//Variables de categoria, campo Foreign Key de la tabla_coches y objeto
	//de la clase que representa a la tabla_categorias_coches
	private int id_categoria;
	private Categoria categoria;	


	public Coche() {
		
	}//end constructor

	public Coche(String marca, String modelo, String color, String motor, int cilindrada, int precio,
			int telefono, String email, int id_categoria) {

		this.marca = marca;
		this.modelo = modelo;
		this.color = color;
		this.motor = motor;
		this.cilindrada = cilindrada;
		this.precio = precio;
		this.telefono = telefono;
		this.email = email;
		this.id_categoria = id_categoria;

	}//end constructor
	
	public int getId() {
		return id;
	}
	
	public void setId(int id) {
		this.id = id;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getMotor() {
		return motor;
	}

	public void setMotor(String motor) {
		this.motor = motor;
	}

	public int getCilindrada() {
		return cilindrada;
	}

	public void setCilindrada(int cilindrada) {
		this.cilindrada = cilindrada;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	public int getTelefono() {
		return telefono;
	}

	public void setTelefono(int telefono) {
		this.telefono = telefono;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}
	
	public int getId_categoria() {
		return id_categoria;
	}

	public void setId_categoria(int id_categoria) {
		this.id_categoria = id_categoria;
	}
	
	public Categoria getCategoria() {
		return categoria;
	}

	public void setCategoria(Categoria categoria) {
		this.categoria = categoria;
	}

	@Override
	public String toString() {
		return "Coche [id=" + id + ", marca=" + marca + ", modelo=" + modelo + ", color=" + color + ", motor=" + motor
				+ ", cilindrada=" + cilindrada + ", precio=" + precio + ", telefono=" + telefono + ", email=" + email
				+ ", id_categoria=" + id_categoria + ", categoria=" + categoria + "]";
	}

	
	
}// end class
