package servletsAdmin;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/admin/ServletLogOutAdmin")
public class ServletLogOutAdmin extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//este metodo se ejecuta ante get y post
		request.getSession().invalidate();
		response.sendRedirect("../loginAdmin.jsp");
	}

}
