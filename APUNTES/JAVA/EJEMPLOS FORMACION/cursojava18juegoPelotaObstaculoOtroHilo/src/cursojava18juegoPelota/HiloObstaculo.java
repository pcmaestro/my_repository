package cursojava18juegoPelota;

public class HiloObstaculo extends Thread {
	// coordenas obstaculo
	private int xObstaculo = 200;
	private int yObstaculo = 200;
	private boolean hiloActivo = true;

	@Override
	public void run() {
		while (hiloActivo) {
			yObstaculo--;
			try {
				Thread.sleep(5);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} // end while
	}// end run

	public int getxObstaculo() {
		return xObstaculo;
	}

	public void setxObstaculo(int xObstaculo) {
		this.xObstaculo = xObstaculo;
	}

	public int getyObstaculo() {
		return yObstaculo;
	}

	public void setyObstaculo(int yObstaculo) {
		this.yObstaculo = yObstaculo;
	}

	public boolean isHiloActivo() {
		return hiloActivo;
	}

	public void setHiloActivo(boolean hiloActivo) {
		this.hiloActivo = hiloActivo;
	}

}
