package modelo;

import java.util.List;

import org.hibernate.Criteria;
import org.hibernate.SessionFactory;
import org.hibernate.criterion.Criterion;
import org.hibernate.criterion.Restrictions;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class ServicioAnunciosHiberImpl implements ServicioAnuncios{

	@Autowired
	private SessionFactory sessionFactory;
	
	@Override
	public void registrarAnuncio(Anuncio anuncio) {
		sessionFactory.getCurrentSession().save(anuncio);
	}

	@Override
	public List<Anuncio> obtenerAnuncios() {
		Criteria criteria = 
				sessionFactory.getCurrentSession().
					createCriteria(Anuncio.class);
//		criteria.add(Restrictions.isEmpty("precio"));	
		return criteria.list();
	}
	

	
}




