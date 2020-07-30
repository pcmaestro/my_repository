package gestorVentanas;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.DefaultListModel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

import daos.LibrosDAO;
import daos.LibrosDAOimplArchivo;
import daos.LibrosDAOimplArrayList;
import modelo.Libro;
import vista.PanelEditarLibro;
import vista.PanelInsertarLibro;
import vista.PanelListarLibros;
import vista.VentanaPrincipal;

public class GestorVentanas implements ActionListener {

	// voy a decir que DAO voy a usar aqui para guardar los libros
	LibrosDAO librosDAO = new LibrosDAOimplArchivo();

	private VentanaPrincipal ventanaPrincipal = new VentanaPrincipal();
	private PanelInsertarLibro panelInsertarLibro = new PanelInsertarLibro();
	private PanelListarLibros panelListarLibros = new PanelListarLibros();
	private PanelEditarLibro panelEditarLibro = new PanelEditarLibro();

	//defino una variable para guardar el indice seleccionado
	int indiceLibroSeleccionado = -1;
	
	public GestorVentanas() {

		// digo donde se atiende las opciones de menu
		ventanaPrincipal.getMenuRegistrarLibro().addActionListener(this);
		ventanaPrincipal.getMenuListarLibros().addActionListener(this);

		// digo donde se atienden los botones
		panelInsertarLibro.getBotonRegistrarLibro().addActionListener(this);
		//botones editar y borrar libro
		panelListarLibros.getBotonBorrar().addActionListener(this);
		panelListarLibros.getBotonEditar().addActionListener(this);
		//boton guardar cambios
		panelEditarLibro.getBotonGuardarCambiosLibro().addActionListener(this);
		
		// de primeras que la ventana muestre el panel de insercion
		ventanaPrincipal.setContentPane(panelInsertarLibro);
		ventanaPrincipal.setVisible(true);
	}

	
	private void cargarPanelListadoLibros() {
		ventanaPrincipal.setContentPane(panelListarLibros);
		ArrayList<Libro> libros = librosDAO.obtenerLibros();
		DefaultListModel<String> listModel = 
					new DefaultListModel<String>();
		for(Libro l : libros) {
			listModel.addElement(l.toString());
		}
		panelListarLibros.getJListLibros().setModel(listModel);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		Object elementoPulsado = e.getSource();
		if (elementoPulsado == ventanaPrincipal.getMenuRegistrarLibro()) {
			ventanaPrincipal.setContentPane(panelInsertarLibro);
		} else if (elementoPulsado == ventanaPrincipal.getMenuListarLibros()) {			
			cargarPanelListadoLibros();
		} else if (elementoPulsado == panelInsertarLibro.getBotonRegistrarLibro()) {
			Libro nuevoLibro = new Libro();
			nuevoLibro.setTitulo(panelInsertarLibro.getEntradaTitulo().getText());
			nuevoLibro.setAutor(panelInsertarLibro.getEntradaAutor().getText());
			nuevoLibro.setNumeroPaginas(Integer.parseInt(panelInsertarLibro.getEntradaPaginas().getText()));
			nuevoLibro.setPrecio(Double.parseDouble(panelInsertarLibro.getEntradaPrecio().getText()));
			librosDAO.registrarLibro(nuevoLibro);
			JOptionPane.showMessageDialog(null, "Libro registrado OK");
			panelInsertarLibro.getEntradaAutor().setText("");
			panelInsertarLibro.getEntradaTitulo().setText("");
			panelInsertarLibro.getEntradaPrecio().setText("");
			panelInsertarLibro.getEntradaPaginas().setText("");
			
		} else if(elementoPulsado == panelListarLibros.getBotonBorrar()) {
			System.out.println("se quiere borrar un registro");
			int indice = 
					panelListarLibros.getJListLibros().getSelectedIndex();
			System.out.println("borrar el indice: " + indice);
			librosDAO.borrarLibro(indice);
			cargarPanelListadoLibros();			
		}else if(elementoPulsado == panelListarLibros.getBotonEditar()) {
			indiceLibroSeleccionado = 
					panelListarLibros.getJListLibros().getSelectedIndex();
			Libro l = librosDAO.obtenerLibroPorIndice(indiceLibroSeleccionado);
			panelEditarLibro.getEntradaTitulo().setText(l.getTitulo());
			panelEditarLibro.getEntradaAutor().setText(l.getAutor());
			panelEditarLibro.getEntradaPrecio().
				setText(Double.toString(l.getPrecio()));
			panelEditarLibro.getEntradaPaginas().setText(
					Integer.toString(l.getNumeroPaginas())
					);
			ventanaPrincipal.setContentPane(panelEditarLibro);
		}else if(elementoPulsado == panelEditarLibro.getBotonGuardarCambiosLibro()) {
			String titulo = panelEditarLibro.getEntradaTitulo().getText();
			String autor = panelEditarLibro.getEntradaAutor().getText();
			double precio = Double.parseDouble(
					panelEditarLibro.getEntradaPrecio().getText());
			int paginas = Integer.parseInt(
					panelEditarLibro.getEntradaPaginas().getText());
			librosDAO.actualizarLibroPorIndice(autor, titulo, precio, 
					paginas, indiceLibroSeleccionado);
			cargarPanelListadoLibros();
		}
			
			
		SwingUtilities.updateComponentTreeUI(ventanaPrincipal);
	}// end actionPerformed

}







