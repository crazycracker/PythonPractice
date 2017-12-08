import mysql.connector
from mysql.connector import errorcode


config = {
  'user': 'root',
  'password': 'MyNewPass',
  'host': '127.0.0.1',
  'database': 'testdb',
  'raise_on_warnings': True,
  'use_pure': False,
}
cnx = mysql.connector.connect(**config)
print(cnx.server_port)
cnx.close()