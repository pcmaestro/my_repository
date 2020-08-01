package modelo;

import java.io.Serializable;

public class Coche implements Serializable	{
	private String marca;
	private String modelo;
	private String color;
	private String motor;
	private String cilindrada;
	private String precio;	
	private int id;
	private static int proximoId = 0;
	
	public Coche() {
		this.id = proximoId;
		proximoId++;
	}

	public Coche(String marca, String modelo, String color, String motor, String cilindrada, String precio) {

		this.marca = marca;
		this.modelo = modelo;
		this.color = color;
		this.motor = motor;
		this.cilindrada = cilindrada;
		this.precio = precio;
		this.id = proximoId++;

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

	public String getCilindrada() {
		return cilindrada;
	}

	public void setCilindrada(String cilindrada) {
		this.cilindrada = cilindrada;
	}

	public String  getPrecio() {
		return precio;
	}

	public void setPrecio(String precio) {
		this.precio = precio;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
	
	@Override
	public String toString() {
		return "Coche [marca=" + marca + ", modelo=" + modelo + ", color=" + color + ", motor=" + motor
				+ ", cilindrada=" + cilindrada + ", precio=" + precio + ", id=" + id + "]";
	}
}// end class