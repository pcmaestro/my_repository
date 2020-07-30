package cursojava17threads;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		System.out.println("se ejecuta el hilo principal");
		Hilo1 h1 = new Hilo1();
		Thread.sleep(1000);
		System.out.println("vamos a lanzar el hilo uno");
		h1.start();//start lanza el run del hilo de forma paralela
		
		System.out.println("esperamos desde el hilo principal 1 seg");
		Thread.sleep(1000);
		
		System.out.println("esperamos desde el princial otro segundo");
		Thread.sleep(1000);
		
		System.out.println(
				"esperamos un segundo MAS desde el hilo principal");
		Thread.sleep(1000);
		h1.pararHilo();
		Thread.sleep(1000);
		System.out.println("ahora el hilo principal seguiría");
		System.out.println("resto de codigo");
		
	}

}
