package modelo;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="tabla_anuncios")
public class Anuncio {

	private String titulo;
	private double precio;
	private String texto;
	
	@Id
	@GeneratedValue
	private int id;
	
	public Anuncio() {
	}

	public Anuncio(String titulo, double precio, String texto) {
		super();
		this.titulo = titulo;
		this.precio = precio;
		this.texto = texto;
	}

	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	public String getTexto() {
		return texto;
	}

	public void setTexto(String texto) {
		this.texto = texto;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
	
}
