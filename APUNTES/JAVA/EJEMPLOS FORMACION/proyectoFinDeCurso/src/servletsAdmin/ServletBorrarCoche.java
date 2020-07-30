package servletsAdmin;

import java.io.IOException; 
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.CochesDAO;
import daosimpl.CochesDAOimpl;


@WebServlet("/admin/ServletBorrarCoche")
public class ServletBorrarCoche extends HttpServlet {
	private static final long serialVersionUID = 1L;
       

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		int idBorrar = Integer.parseInt(id);
		CochesDAO cochesDAO = new CochesDAOimpl();
		cochesDAO.borrarCoche(idBorrar);
		response.sendRedirect("ServletListarAnuncios");
	}

	
}
