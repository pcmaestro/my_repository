package practicaJuegoPelota;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;

import javax.swing.JOptionPane;
import javax.swing.JPanel;

//parecido a cuando usabamos Thread para trabajar con hilos
//también podemos trabajar con hilo con el interfaz Runnable
public class MiPanel extends JPanel implements Runnable, KeyListener {

	private static final int DERECHA = 1;
	private static final int ABAJO = 2;
	private static final int ATRAS = 3;
	private static final int ARRIBA = 4;

	// variable que indica la direccion de la pelota
	int direccion = DERECHA;
	int velocidad = 1;	

	// coordenadas de la pelota
	Random r = new Random();
	
	int numeroInt = 100 + r.nextInt(400);
	
	
	int xbola = 50;
	int ybola = numeroInt;


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
	} //end constructor

	@Override
	public void paint(Graphics g) {
		super.paint(g);
		g.setColor(Color.WHITE);
		g.fillOval(xbola, ybola, 70, 70);		
		g.setColor(Color.YELLOW);
		g.fillRect(xMeta, yMeta, anchoMeta, altoMeta);

	}//end paint

	@Override
	public void run() {
		while (hiloActivo) {
			try {
				Thread.sleep(10);

				if (direccion == DERECHA) {
					xbola += velocidad;
				}
				if (direccion == ABAJO) {
					ybola += velocidad;
				}
				if (direccion == ATRAS) {
					xbola -= velocidad;
				}
				if (direccion == ARRIBA) {
					ybola -= velocidad;
				}

				if (xbola >= xMeta && xbola <= (xMeta + anchoMeta) && ybola >= yMeta && ybola <= (yMeta + altoMeta)) {

					JOptionPane.showMessageDialog(this, "Felicidades, llevaste la bola a la meta");
					JOptionPane.showMessageDialog(this, "jugamos otra vez");
					xbola = 50;
					ybola = (int)numeroInt;
					velocidad++;

				} else if (xbola >= 800 || ybola >= 600 || xbola < -140 || ybola < -140) {

					JOptionPane.showMessageDialog(this, "Lo siento, has perdido");
					this.hiloActivo = false;
				}//end if
				
				repaint();
				
			} catch (InterruptedException e) {
				System.out.println("se interrumpio el hilo");
			}//end try-catch
		} // end while
	}// end run

	@Override
	public void keyPressed(KeyEvent e) {
		int tecla = e.getKeyCode();
		System.out.println("pulsado: " + tecla);

		switch (tecla) {
			case 39:
				direccion = DERECHA;
				break;
	
			case 40:
				direccion = ABAJO;
				break;
	
			case 37:
				direccion = ATRAS;
				break;
	
			case 38:
				direccion = ARRIBA;
				break;
		} //end switch
	}// end keypressed

	@Override
	public void keyTyped(KeyEvent e) {
	}

	@Override
	public void keyReleased(KeyEvent e) {
	}

}// end class
