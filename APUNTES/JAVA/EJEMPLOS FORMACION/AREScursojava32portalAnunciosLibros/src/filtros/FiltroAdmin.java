package filtros;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class FiltroAdmin implements Filter{

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		//si en sesion no esta metido un adminOk
		//redirijo a loginAdmin.jsp
		
		//el request de este filter no es el mismo que el que estamos 
		//usando en los servlet, para tener el mismo request
		//que en los servlet, tengo que hacer un casting
		//ahora mismo req es el mismo request que en los servlet
		HttpServletRequest req = (HttpServletRequest)request;
		if( req.getSession().getAttribute("adminOk") != null ) {
			//si todo esta bien, que el filtro no haga nada
			//y permita que la peticion siga adelante
			chain.doFilter(request, response);
		}else {
			HttpServletResponse res = (HttpServletResponse)response;
			//lo siguiente es una redireccion forzada, lo que hace es:
			//forzar al navegador del cliente a pedir la ruta indicada
			res.sendRedirect("loginAdmin.jsp");
		}
		
		
		
	}//end doFilter

}
