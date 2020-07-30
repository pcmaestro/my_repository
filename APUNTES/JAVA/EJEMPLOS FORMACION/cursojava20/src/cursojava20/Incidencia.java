package cursojava20;

public class Incidencia {
	private String nombre;
	private int pedido;
	private EstadoIncidencia estado;
	
	public Incidencia() {
		this.estado = EstadoIncidencia.ABIERTA;
	}
}
