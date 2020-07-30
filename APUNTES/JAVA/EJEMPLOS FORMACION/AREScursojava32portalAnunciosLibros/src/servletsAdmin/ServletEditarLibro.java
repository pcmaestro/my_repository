package servletsAdmin;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.LibrosDAO;
import daos.LibrosDAOImpl;
import modelo.Libro;


@WebServlet("/admin/ServletEditarLibro")
public class ServletEditarLibro extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		int idEditar = Integer.parseInt(id);
		LibrosDAO librosDAO = new LibrosDAOImpl();
		Libro l = librosDAO.obtenerLibroPorId(idEditar);
		request.setAttribute("libro", l);
		RequestDispatcher dispatcher = 
				getServletContext().getRequestDispatcher("/admin/editarLibro.jsp");
		dispatcher.forward(request, response);
	}

}
