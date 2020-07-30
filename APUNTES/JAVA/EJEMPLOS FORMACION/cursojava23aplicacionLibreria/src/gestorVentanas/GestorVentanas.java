package gestorVentanas;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

import daos.LibrosDAO;
import daos.LibrosDAOimplArrayList;
import modelo.Libro;
import vista.PanelInsertarLibro;
import vista.PanelListarLibros;
import vista.VentanaPrincipal;

public class GestorVentanas implements ActionListener{

	//voy a decir que DAO voy a usar aqui para guardar los libros
	LibrosDAO librosDAO = new LibrosDAOimplArrayList();
	
	private VentanaPrincipal ventanaPrincipal = 
			new VentanaPrincipal();
	private PanelInsertarLibro panelInsertarLibro = 
			new PanelInsertarLibro();
	private PanelListarLibros panelListarLibros = 
			new PanelListarLibros();
	
	public GestorVentanas() {
		
		//digo donde se atiende las opciones de menu
		ventanaPrincipal.getMenuRegistrarLibro().addActionListener(this);
		ventanaPrincipal.getMenuListarLibros().addActionListener(this);
		
		//digo donde se atienden los botones
		panelInsertarLibro.getBotonRegistrarLibro().addActionListener(this);
		
		//de primeras que la ventana muestre el panel de insercion
		ventanaPrincipal.setContentPane(panelInsertarLibro);
		ventanaPrincipal.setVisible(true);
	}
	
	
	
	@Override
	public void actionPerformed(ActionEvent e) {
		Object elementoPulsado = e.getSource();
		if (elementoPulsado == ventanaPrincipal.getMenuRegistrarLibro()) {
			ventanaPrincipal.setContentPane(panelInsertarLibro);
		}else if(elementoPulsado == ventanaPrincipal.getMenuListarLibros()) {
			ventanaPrincipal.setContentPane(panelListarLibros);
			ArrayList<Libro> libros = librosDAO.obtenerLibros();
			String texto = "";
			for(Libro l : libros) {
				texto += l.toString() + "\n";
			}
			panelListarLibros.getListadoLibros().setText(texto);
			
		}else if(elementoPulsado == panelInsertarLibro.getBotonRegistrarLibro()) {
			Libro nuevoLibro = new Libro();
			nuevoLibro.setTitulo(panelInsertarLibro.getEntradaTitulo().getText());
			nuevoLibro.setAutor(panelInsertarLibro.getEntradaAutor().getText());
			nuevoLibro.setNumeroPaginas(
				Integer.parseInt(panelInsertarLibro.getEntradaPaginas().getText())
				);
			nuevoLibro.setPrecio(
				Double.parseDouble(panelInsertarLibro.getEntradaPrecio().getText())	
				);
			librosDAO.registrarLibro(nuevoLibro);
			JOptionPane.showMessageDialog(null,
					"Libros registrado OK");
		}
		SwingUtilities.updateComponentTreeUI(ventanaPrincipal);
	}//end actionPerformed

}













