package servlets;

import java.io.IOException;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.LibrosDAO;
import daos.LibrosDAOImpl;
import modelo.Libro;


@WebServlet("/inicio")
public class ServletInicio extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//obtener los anuncios y listarlos en inicio.jsp
		LibrosDAO librosDAO = new LibrosDAOImpl();
		List<Libro> libros = librosDAO.obtenerLibros();
		request.setAttribute("libros", libros);
		RequestDispatcher dispatcher = 
				getServletContext().getRequestDispatcher("/inicio.jsp");
		dispatcher.forward(request, response);
	}


}
