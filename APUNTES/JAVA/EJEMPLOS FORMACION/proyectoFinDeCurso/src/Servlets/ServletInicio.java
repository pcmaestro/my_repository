
package Servlets;

import java.io.IOException; 
import java.util.ArrayList;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.CochesDAO;
import daosimpl.CochesDAOimpl;
import model.Coche;

@WebServlet("/inicio")
public class ServletInicio extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		System.out.println("llego a ServletInicio-doGet");
		
		//Variables para el buscador
		String marcaAbuscar = "";
		String modeloAbuscar = "";
		String colorAbuscar = "";	
		
		request.setAttribute("marcaAbuscar", "");
		request.setAttribute("modeloAbuscar", "");
		request.setAttribute("colorAbuscar", "");
	

		if (request.getParameter("marca") != null ) {
			marcaAbuscar = request.getParameter("marca");
			System.out.println("validando marca");
			
		}else if (request.getParameter("modelo") != null) {
			modeloAbuscar = request.getParameter("modelo");
			System.out.println("validando modelo");
			
		}else if (request.getParameter("color") != null) {
			colorAbuscar = request.getParameter("color");
			System.out.println("validando color");			
		
		}//end if			

		//Variables de paginación
		int comienzo = 0;
		int resultadosPorPagina = 20;
		int siguiente = -1;
		int anterior = -1;

		if (request.getParameter("comienzo") != null) {
			comienzo = Integer.parseInt(request.getParameter("comienzo"));
		}
		siguiente = comienzo + resultadosPorPagina;
		anterior = comienzo - resultadosPorPagina;
		
		//Obtención y listado de anuncios al principio
		CochesDAO cochesDAO = new CochesDAOimpl();
		List<Coche> coches = cochesDAO.obtenerCoches(marcaAbuscar, modeloAbuscar, colorAbuscar, comienzo, resultadosPorPagina);
		request.setAttribute("coches", coches);
		request.setAttribute("marcaAbuscar", marcaAbuscar);
		request.setAttribute("modeloAbuscar", modeloAbuscar);
		request.setAttribute("colorAbuscar", colorAbuscar);
		request.setAttribute("siguiente", siguiente);
		request.setAttribute("anterior", anterior);
		
				
		//Obtenemos el total de libros para mostrarlos en la página
		int total = cochesDAO.totalCoches(marcaAbuscar, modeloAbuscar, colorAbuscar);
		request.setAttribute("total", total);
		System.out.println("Buscando anuncios, caso de error, revisar ServletInicio");
		
		RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/inicio.jsp");
		dispatcher.forward(request, response);
		
			
	}//end doGet

}//end servlet
