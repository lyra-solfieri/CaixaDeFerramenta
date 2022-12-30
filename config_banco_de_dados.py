import sqlite3


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
	id integer PRIMARY KEY,
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


def salvar_link(args):
    pass
