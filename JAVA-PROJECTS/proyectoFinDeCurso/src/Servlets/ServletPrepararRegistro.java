package Servlets;

import java.io.IOException;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.CategoriasDAO;
import daosimpl.CategoriasDAOimpl;
import model.Categoria;

@WebServlet("/ServletPrepararRegistro")
public class ServletPrepararRegistro extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		CategoriasDAO categoriasDAO = new CategoriasDAOimpl();
		List<Categoria> categorias = categoriasDAO.obtenerCategorias();
		request.setAttribute("categorias", categorias);
		RequestDispatcher dispatcher = getServletContext().getRequestDispatcher("/registrarCoche.jsp");
		dispatcher.forward(request, response);
		
	}//end doGet	

}//end Servlet
