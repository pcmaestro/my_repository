package cursojava30jdbcIncluyendoLibreria;

import java.io.Serializable;

public class Libro implements Serializable{

	private static final long serialVersionUID = 3L;
	
	private String titulo;
	private String autor;
	private int numeroPaginas;
	private double precio;
	private String tipo;
	private boolean enStock;
	private int id;
	private boolean tapaDura;
	public boolean isTapaDura() {
		return tapaDura;
	}

	public void setTapaDura(boolean tapaDura) {
		this.tapaDura = tapaDura;
	}

	private static int proximoId = 1;

	public Libro() {
		this.id = proximoId;
		proximoId++;
	}

	public Libro(String titulo, String autor, int numeroPaginas, double precio) {
		this.titulo = titulo;
		this.autor = autor;
		this.numeroPaginas = numeroPaginas;
		this.precio = precio;
		this.id = proximoId++;// esto signa y luego incrementa
	}

	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public String getAutor() {
		return autor;
	}

	public void setAutor(String autor) {
		this.autor = autor;
	}

	public int getNumeroPaginas() {
		return numeroPaginas;
	}

	public void setNumeroPaginas(int numeroPaginas) {
		this.numeroPaginas = numeroPaginas;
	}

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
	
	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public boolean isEnStock() {
		return enStock;
	}

	public void setEnStock(boolean enStock) {
		this.enStock = enStock;
	}

	@Override
	public String toString() {
		return "Libro [titulo=" + titulo + ", autor=" + autor + ", numeroPaginas=" + numeroPaginas + ", precio="
				+ precio + ", id=" + id + "]";
	}

}//end class









