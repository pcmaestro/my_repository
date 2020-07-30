package sql;

public class Query {
	
	private static final String select = "select * from tabla_coches order by id desc;";
	private static final String selectById = "select * from tabla_coches where id = ?;";
	private static final String insert = "insert into tabla_coches (marca, modelo, color, motor, cilindrada, precio, telefono, email, id_categoria) "+
										 "values (?,?,?,?,?,?,?,?,?);";
	private static final String delete = "delete from tabla_coches where id = ?;"; 
	private static final String update = "update tabla_coches set marca = ?, modelo = ?, color = ?, motor = ?,"+
										 "cilindrada = ?, precio = ?, telefono = ?, email = ?, id_categoria = ? where id = ?;";
	

	public static String getSelect() {
		return select;
	}

	public static String getInsert() {
		return insert;
	}

	public static String getSelectbyid() {
		return selectById;
	}

	public static String getDelete() {
		return delete;
	}

	public static String getUpdate() {
		return update;
	}
	
	
	
	
}
