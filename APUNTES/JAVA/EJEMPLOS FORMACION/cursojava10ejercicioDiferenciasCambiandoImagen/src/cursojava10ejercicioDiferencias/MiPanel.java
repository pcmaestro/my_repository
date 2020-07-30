package cursojava10ejercicioDiferencias;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class MiPanel extends JPanel implements MouseListener{
	
	private Image primeraImagen = null;
	private JFrame ventana;
	
	public MiPanel(JFrame ventana) {
		this.ventana = ventana;
		//cargar la imagen:
		File archivoImagen = new File("imagen.jpg");
		try {
			primeraImagen = ImageIO.read(archivoImagen);
		} catch (IOException e) {
			System.out.println("no pude leer del archivo");
		}
		//vamos a decirle al panel que el solito es el qeu va a 
		//atender los clicks de raton sobre el mismo
		this.addMouseListener(this);
		
	}

	public void paint(Graphics g) {
		//todo el codigo que dice como se muestra el panel
		g.drawImage(primeraImagen, 0,0, 800, 400, this);
	}



	@Override
	public void mousePressed(MouseEvent e) {
		int x = e.getX();
		int y = e.getY();
		
		System.out.println("has hecho click en x: " + x + " y: " + y);
		
		if ( x >= 537 && x <= 643 && y >= 130 && y <= 186 ) {
			JOptionPane.showMessageDialog(this, 
					"Felicidades la has adivinado");
			File archivoImagen = new File("imagenFinal.jpg");
			this.ventana.setSize(900, 300);
			try {
				primeraImagen = ImageIO.read(archivoImagen);
			} catch (IOException e2) {
				System.out.println("no pude leer del archivo");
			}
			this.repaint();
			
		} else {
			JOptionPane.showMessageDialog(this, 
					"Fallaste, intentalo de nuevo");
		}
		
	}
	//resto de metodos del interfaz que no vamos a usar, 
	//pero tienen que estar. Ya que cuando implementamos un interfaz
	//debemos tener en la clase todos los metodos que 
	//nos indique el interfaz
	@Override
	public void mouseClicked(MouseEvent e) {
	}

	@Override
	public void mouseReleased(MouseEvent e) {
	}

	@Override
	public void mouseEntered(MouseEvent e) {
	}

	@Override
	public void mouseExited(MouseEvent e) {
	}
		
}
