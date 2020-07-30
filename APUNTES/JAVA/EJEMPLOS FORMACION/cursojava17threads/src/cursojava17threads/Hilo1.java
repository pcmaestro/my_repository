package cursojava17threads;

//las clases del paquete java.lang no hace falta importarlas
//ya estan incluidas por defecto
public class Hilo1 extends Thread {

	private boolean hiloActivo = true;

	public void pararHilo() {
		this.hiloActivo = false;
	}

	@Override
	public void run() {
		// todo el codigo que tenga dentro de este run
		// lo puedo ejecutar de forma paralela a la aplicacion principal
		while (this.hiloActivo == true) {
			System.out.println("se ejecuta hilo1");
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				System.out.println("se interrumpio la espera");
			}
		} // end while
	}// End run

}
