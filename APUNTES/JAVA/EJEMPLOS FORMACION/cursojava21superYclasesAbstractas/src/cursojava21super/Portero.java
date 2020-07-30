package cursojava21super;

public class Portero extends Jugador{

	public Portero() {
		super(30,400);
		System.out.println("se ejecuta el constructor de Portero");
	}

	@Override
	public void correr() {
		super.correr();
		System.out.println("limitar que portero no salga de zona");
	}
	
	public void correr(int velocidad) {
		this.correr();
		System.out.println("portero corre a velocidad: " + velocidad);
	}

	@Override
	public void expulsar() {
		System.out.println("expulsando portero...");
	}
	
	//lo siguiente solo esta permitido en clases abstractas
	//public abstract void cobrar();
	
}
