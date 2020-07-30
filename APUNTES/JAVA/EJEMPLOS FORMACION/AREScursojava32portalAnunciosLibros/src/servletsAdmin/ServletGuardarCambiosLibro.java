package servletsAdmin;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.LibrosDAO;
import daos.LibrosDAOImpl;
import modelo.Libro;

@WebServlet("/admin/ServletGuardarCambiosLibro")
public class ServletGuardarCambiosLibro extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String titulo = request.getParameter("titulo");
		String autor = request.getParameter("autor");
		String paginas = request.getParameter("paginas");
		String precio = request.getParameter("precio");
		String id = request.getParameter("id");
		//parte de validacion
		//...
		int paginasInt = Integer.parseInt(paginas);
		int idInt = Integer.parseInt(id);
		double precioDouble = Double.parseDouble(precio);
		//fin parte de validacion
		
		Libro l = new Libro(titulo, autor, paginasInt, precioDouble);
		l.setId(idInt);
		LibrosDAO librosDAO = new LibrosDAOImpl();
		librosDAO.guardarCambiosLibro(l);
		response.sendRedirect("ServletListarAnuncios");		
	}//end doPost

}
