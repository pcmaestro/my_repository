package cursojava18juegoPelota;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JOptionPane;
import javax.swing.JPanel;

//parecido a cuando usabamos Thread para trabajar con hilos
//también podemos trabajar con hilo con el interfaz Runnable
public class MiPanel extends JPanel implements Runnable, KeyListener {

	// variable que indica la direccion de la pelota
	Direcciones direccion = Direcciones.DERECHA;

	// coordenadas de la pelota
	int xbola = 50;
	int ybola = 50;

	// coordenadas de la zona de meta
	int xMeta = 700;
	int yMeta = 300;
	int anchoMeta = 100;
	int altoMeta = 200;

	// variable que gestiona si el hilo esta activo
	private boolean hiloActivo = true;

	public MiPanel() {
		this.setFocusable(true);// es para permitir que el panel tenga foco
		this.addKeyListener(this);
		this.setBackground(new Color(100, 200, 100));
		// creo el hilo y lo lanzo, por trabajar con Runnable
		// se hace asi:
		Thread hilo = new Thread(this);
		hilo.start();
	}

	@Override
	public void paint(Graphics g) {
		super.paint(g);
		g.setColor(Color.WHITE);
		g.fillOval(xbola, ybola, 70, 70);
		g.setColor(Color.YELLOW);
		g.fillRect(xMeta, yMeta, anchoMeta, altoMeta);

	}

	@Override
	public void run() {
		while (hiloActivo) {
			try {
				Thread.sleep(10);

				switch (direccion) {
				case DERECHA:
					xbola++;
					break;
				case ABAJO:
					ybola++;
					break;
				default:
					break;
				}
				

				if (xbola >= xMeta && xbola <= (xMeta + anchoMeta) && 
					ybola >= yMeta && ybola <= (yMeta + altoMeta) ) {
					
					JOptionPane.showMessageDialog(this, 
							"Felicidades, llevaste la bola a la meta");
					this.hiloActivo = false;
					
				}else if( xbola >= 800 || ybola >= 600) {
					
					JOptionPane.showMessageDialog(this,
							"Lo siento, has perdido");
					this.hiloActivo = false;
				}
				repaint();
			} catch (InterruptedException e) {
				System.out.println("se interrumpio el hilo");
			}
		} // end while
	}// end run

	@Override
	public void keyPressed(KeyEvent e) {
		int tecla = e.getKeyCode();
		System.out.println("pulsado: " + tecla);
		switch (tecla) {
		case 39:
			direccion = Direcciones.DERECHA;
			break;
		case 40:
			direccion = Direcciones.ABAJO;
			break;
		default:
			break;
		}
		
	}

	@Override
	public void keyTyped(KeyEvent e) {
	}

	@Override
	public void keyReleased(KeyEvent e) {
	}

}// end class
