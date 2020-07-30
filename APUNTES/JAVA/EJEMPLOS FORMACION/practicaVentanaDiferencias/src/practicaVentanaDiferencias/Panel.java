package practicaVentanaDiferencias;

import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.File;
import java.io.IOException;
import java.util.Date;

import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class Panel extends JPanel implements MouseListener {

	private Image imagenA = null;
	private Image imagenB = null;

	private boolean acierto1 = false;
	private boolean acierto2 = false;
	private boolean acierto3 = false;
	private boolean acierto4 = false;

	Date start = new Date();
	Date stop = new Date();
	
	double inicio = start.getTime();
	double fin = 0;

	public Panel(JFrame ventana) {
		File imagen1 = new File(
				"C:\\Users\\localuser\\eclipse-workspace\\practicaVentanaDiferencias\\src\\practicaVentanaDiferencias\\paisaje1.jpg");
		File imagen2 = new File(
				"C:\\Users\\localuser\\eclipse-workspace\\practicaVentanaDiferencias\\src\\practicaVentanaDiferencias\\paisaje2.jpg");
		try {
			imagenA = ImageIO.read(imagen1);
			imagenB = ImageIO.read(imagen2);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			System.out.println("No se localiza la imagen");
		}
		this.addMouseListener(this);
		
	}

	public void paint(Graphics g) {
		g.drawImage(imagenA, 0, 0, 450, 350, this);
		g.drawImage(imagenB, 450, 0, 450, 350, this);

	}

	@Override
	public void mousePressed(MouseEvent e) {
		int x = e.getX();
		int y = e.getY();

		if (x < 531 && x > 486 && y < 40 && y > 9) {
			JOptionPane.showMessageDialog(this, "Acertaste !!");
			acierto1 = true;

		} else if (x < 599 && x > 549 && y < 55 && y > 27) {
			JOptionPane.showMessageDialog(this, "Acertaste !!");
			acierto2 = true;

		} else if (x < 645 && x > 610 && y < 289 && y > 264) {
			JOptionPane.showMessageDialog(this, "Acertaste !!");
			acierto3 = true;

		} else {
			JOptionPane.showMessageDialog(this, "OOOH, fallaste !!");

		} // end if

		if ((acierto1 && acierto2 && acierto3) || (acierto1 && acierto2 && acierto3 && acierto4)) {
			JOptionPane.showMessageDialog(this, "Enhorabuena, acertaste todas las diferencias !!");
			File nuevaImagen = new File(
					"C:\\Users\\localuser\\eclipse-workspace\\practicaVentanaDiferencias\\src\\practicaVentanaDiferencias\\paisaje3.jpg");
			try {
				imagenB = ImageIO.read(nuevaImagen);
			} catch (IOException e1) {				
				e1.printStackTrace();
			}
			this.repaint();
			JOptionPane.showMessageDialog(this, "Prueba suerte con una nueva diferencia adicional");

			if(x < 871 && x > 802 && y < 131 && y > 118) {
				acierto4 = true;		
				double fin = stop.getTime();
			}
			
		} //end if

	}// end MousePressed
	
	public void mostrar_registro() {
		
	}

	@Override
	public void mouseClicked(MouseEvent arg0) {

	}

	@Override
	public void mouseEntered(MouseEvent e) {

	}

	@Override
	public void mouseExited(MouseEvent e) {

	}

	@Override
	public void mouseReleased(MouseEvent e) {

	}

}
