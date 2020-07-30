package Servlets;

import java.io.File;
import java.io.IOException;  

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import daos.CochesDAO;
import daosimpl.CochesDAOimpl;
import model.Coche;
import validadores.Validador;


@WebServlet("/guardarNuevoCoche")
@MultipartConfig
public class ServletGuardarCoche extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	//Variables de validacion
	private Validador validador = new Validador();
	private boolean marcav;
	private boolean modelov;
	private boolean colorv;
	private boolean motorv;
	private boolean cilindradav;
	private boolean preciov;
	private boolean telefonov;
	private boolean emailv;
	private boolean validarFormularios;
	
	//Objeto de coche
	private Coche coche = new Coche();
	
	//Variables para recoger la información de los formularios
	String marca;
	String modelo;
	String color;
	String motor;
	String cilindrada;
	String precio;
	String telefono;
	String email;
	String id_categoria;
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException{
		
		//Recogemos los datos de los formularios y validamos que no haya campos
		//en blanco
		marca = request.getParameter("marca").trim();
		modelo = request.getParameter("modelo").trim();
		color = request.getParameter("color").trim();
		motor = request.getParameter("motor").trim();
		cilindrada = request.getParameter("cilindrada").replace(".","").replace(",","").trim();
		precio = request.getParameter("precio").replace(".","").replace(",","").trim();
		telefono = request.getParameter("telefono").replace(".","").replace(",","").trim();
		email = request.getParameter("email").trim();
		id_categoria = request.getParameter("id_categoria");		
		
		if(validador.validarTexto(marca)) {
			marcav = true;
			coche.setMarca(marca);
		}//end validador marca
		
		if(validador.validarTexto(modelo)) {
			modelov = true;
			coche.setModelo(modelo);
		}//end validador modelo
		
		if(validador.validarTexto(color)) {
			colorv = true;
			coche.setColor(color);
		}//end validador color
		
		if(validador.validarTexto(motor)) {
			motorv = true;
			coche.setMotor(motor);
		}//end validador motor
		
		if(validador.validarCilindrada(cilindrada)){
			cilindradav = true;
			coche.setCilindrada(Integer.parseInt(cilindrada));
		}//end validador cilindrada
		
		if(validador.validarPrecio(precio)) {
			preciov = true;
			coche.setPrecio(Integer.parseInt(precio));
		}//end validador precio
		
		if(validador.validarTf(telefono)) {
			telefonov = true;
			coche.setTelefono(Integer.parseInt(telefono));
		}//end validador telefono
		
		if(validador.validarEmail(email)) {
			emailv = true;
			coche.setEmail(email);
		}//end validador email		
		
		coche.setId_categoria(Integer.parseInt(id_categoria));
		
		if(marcav && modelov && colorv && motorv && cilindradav && preciov && telefonov && emailv) {
			validarFormularios = true;
			CochesDAO cochesDAO = new CochesDAOimpl();
			int idGenerado = cochesDAO.registrarCoche(coche);
			
			//Registro de la imagen del anuncio
			Part archivo =  request.getPart("imagen");
			
			//Ruta en la aplicación de despliegue
			String rutaAplicacion = getServletContext().getRealPath("");
			
			//Creamos nueva carpeta en la ruta de despliegue
			String rutaImagenes = rutaAplicacion + File.separator + "imagenes";
			
			//Creamos el objeto para gestionar archivos en la ruta
			File f = new File(rutaImagenes);
			if (!f.exists()) {
				f.mkdirs();
			}
			
			//Creamos la ruta completa incluyendo el nombre de imagen y la guardamos
			String rutaArchivo = rutaImagenes + File.separator  + idGenerado + ".jpg";			
			archivo.write(rutaArchivo);		
			System.out.println("Imagen guardada en la ruta : " + rutaArchivo);
			
			RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/registroCocheOK.jsp");
			dispatcher.forward(request, response);
			
			System.out.println(rutaImagenes);
			
			//Reseteamos el objeto y lo dejamos vacio para evitar duplicidad de registros
			coche.setMarca(null);
			coche.setModelo(null);
			coche.setColor(null);
			coche.setMotor(null);
			coche.setCilindrada(-1);
			coche.setPrecio(-1);
			coche.setTelefono(-1);
			coche.setEmail(null);
			coche.setId_categoria(-1);
			
			
		}else {
			validarFormularios = false;
			RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/registroCocheKO.jsp");
			dispatcher.forward(request, response);
		}
		

	}// end doPost
	
}// end class

