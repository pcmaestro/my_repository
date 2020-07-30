package servlets;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/ServletIdentificarAdmin")
public class ServletIdentificarAdmin extends HttpServlet {
	private static final long serialVersionUID = 1L;
   
	private final static String PASS_ADMIN = "123";

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		if(request.getParameter("pass").equals(PASS_ADMIN)) {
			//para que el filtro no intercepte mas:
			request.getSession().setAttribute("adminOk", "ok");
			//refresco el navegador de usuario con la siguiente ruta:
			response.sendRedirect("loginAdminOk.jsp");
		}else {
			response.sendRedirect("loginAdmin.jsp");			
		}
	}

}
