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
import javax.swing.SwingUtilities;

public class MiPanel extends JPanel implements MouseListener{
	
	private Image primeraImagen = null;
	private JFrame ventana;
	
	private boolean diferencia1 = false;
	private boolean diferencia2 = false;
	private boolean diferencia3 = false;
	
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
					"adivinaste la primera");
			this.diferencia1 = true;
		}else if(x >= 567 && x <= 604 && y >= 31 && y <= 54) {
			JOptionPane.showMessageDialog(this, 
					"adivinaste la segunda");
			this.diferencia2 = true;
		}else if(x >= 628 && x <= 705 && y >= 308 && y <= 337) {
			JOptionPane.showMessageDialog(this, 
					"adivinaste la tercera");
			this.diferencia3 = true;
		} else {
			JOptionPane.showMessageDialog(this, 
					"Fallaste, intentalo de nuevo");
		}
		
		if ( this.diferencia1 == true && this.diferencia2 == true 
				&& this.diferencia3== true) {
			JOptionPane.showMessageDialog(this, 
					"Felicidades la has adivinado");
			
			this.ventana.setContentPane(new PanelFinal());
			SwingUtilities.updateComponentTreeUI(this.ventana);
		}//en if diferencias true
		
	}//end evento del mouse
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
