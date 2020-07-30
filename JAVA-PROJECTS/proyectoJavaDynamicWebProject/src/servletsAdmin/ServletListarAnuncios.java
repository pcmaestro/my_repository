package servletsAdmin;

import java.io.IOException; 


import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.util.List;

import daos.CochesDAO;
import daosimpl.CochesDAOimpl;
import model.Coche;

/**
 * Servlet implementation class ServletListarAnuncios
 */
@WebServlet("/admin/ServletListarAnuncios")
public class ServletListarAnuncios extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		CochesDAO cochesDAO = new CochesDAOimpl();
		//Sin buscador ni paginación
		List<Coche> coches = cochesDAO.obtenerCoches("", "", "", 0, 500);
		request.setAttribute("coches", coches);
		RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/admin/gestionCoches.jsp");
		dispatcher.forward(request, response);

	}//end doGet


}//end servlet
