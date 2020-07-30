package servletsAdmin;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.LibrosDAO;
import daos.LibrosDAOImpl;


@WebServlet("/admin/ServletBorrarLibro")
public class ServletBorrarLibro extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		int idAborrar = Integer.parseInt(id);
		LibrosDAO librosDAO = new LibrosDAOImpl();
		librosDAO.borrarLibro(idAborrar);
		response.sendRedirect("ServletListarAnuncios");
	}
}
