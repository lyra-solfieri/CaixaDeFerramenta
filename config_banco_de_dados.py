import sqlite3


db_file = 'links_salvos.db'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def main():

    db_file = 'links_salvos.db'

    sql = """CREATE TABLE IF NOT EXISTS link_titulo (
	id integer PRIMARY KEY AUTOINCREMENT,
	link text NOT NULL,
	titulo text  NOT NULL,
	date text
    );"""

    # criando a conexão
    conn = create_connection(db_file)

    # criando tabela
    if conn is not None:

        create_table(conn, sql)

    else:
        print("Error! cannot create the database connection.")


"""executar o main para criar a tabela se não existir
if __name__ == '__main__':
    main()"""


def salvar_link(link, titulo, date):
    sql_insert = """INSERT INTO link_titulo(link,titulo,date) VALUES(?,?,?)"""

    try:
        conn = create_connection(db_file=db_file)
        c = conn.cursor()
        c.execute(sql_insert, (link, titulo, date))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


"""TODO: adicionar função para acessar dados salvos no banco de dados 
def links_salvos():
    sql_select = "SELECT * FROM link_titulo LIMIT 0, 11"
    try:
        conn = create_connection(db_file=db_file)
        c = conn.cursor()
        c.execute(sql_select)
        i = 0
        print(c)
        
       for links in c:
            for j in range(len(links)):
                e = Entry(width=10, fg='blue')
                e.pack(fill=BOTH, expand=True)
                e.insert(links[j])
            i = i+1
        
    except sqlite3.Error as e:
        print(e)
    """
