package servletsAdmin;

import java.io.IOException; 

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import daos.CochesDAO;
import daosimpl.CochesDAOimpl;
import model.Coche;


@WebServlet("/admin/ServletEditarCoche")
public class ServletEditarCoche extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id = request.getParameter("id");
		int idEditar = Integer.parseInt(id);
		CochesDAO cochesDAO = new CochesDAOimpl();
		Coche coche = cochesDAO.obtenerCochePorId(idEditar);
		request.setAttribute("coche", coche);
		if (coche.getId_categoria() == 1) {
			request.setAttribute("nuevo", "selected");
		}else if(coche.getId_categoria() == 2) {
			request.setAttribute("seminuevo", "selected");
		}else if(coche.getId_categoria() == 3) {
			request.setAttribute("viejo", "selected");
		}//end if		
		
		RequestDispatcher dispatcher = 
				getServletContext().getRequestDispatcher("/admin/editarCoche.jsp");
		dispatcher.forward(request, response);

	}//end doGet

}//end Servlet
	