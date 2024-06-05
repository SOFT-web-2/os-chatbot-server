import sqlite3
from typing import Any, List


class Database:
    def __init__(self):
        self.__connection: sqlite3.Connection = sqlite3.connect(
            database="data/db.sqlite",
        )
        self.__cursor: sqlite3.Cursor = self.__connection.cursor()

    def query(self, sql: str, *args: Any) -> List[Any]:
        self.__cursor.execute(sql, args)
        return self.__cursor.fetchall()

    def close(self) -> None:
        self.__connection.close()
