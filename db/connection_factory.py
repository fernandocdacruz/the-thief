import mysql.connector
from mysql.connector import Error
from db.config import DB_CONFIG

class DB:
    _connection = None

    @classmethod
    def get_connection(cls):
        if cls._connection is None or not cls._connection.is_connected():
            try:
               cls._connection = mysql.connector.connect(**DB_CONFIG)
            except Error as e:
                raise RuntimeError(f"Erro de conexão com o banco de dados: {e}")
        return cls._connection

    @classmethod
    def close_connection(cls):
        if cls._connection and cls._connection.is_connected():
            cls._connection.close()
            cls._connection = None
