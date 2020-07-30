package cursojava21super;

public abstract class Jugador {
	
	private int x;
	private int y;
	
	public Jugador() {
		System.out.println("creando jugador");
	}
	
	public Jugador(int x, int y) {
		this.x = x;
		this.y = y;
		System.out.println("creando jugador con posiciones x e y "
				+ "indicadas");
	}

	public void correr() {
		System.out.println("jugador corre");
	}
	
	public abstract void expulsar();
	
}
