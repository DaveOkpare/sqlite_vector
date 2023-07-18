import sqlite3
from typing import List, Tuple, Any


class VectorDB:
    def __init__(self, database: str = ":memory:"):
        self.conn = sqlite3.connect(database)
        self.cur = self.conn.cursor()

    def create_table(self, table_name: str, columns: List[Tuple[str, str]]):
        """
        Create a table with the given name and columns

        Columns should be a list of tuples (name, type)

        For example, [("id", "INTEGER PRIMARY KEY"), ("name", "TEXT")]
        """
        sql = f"CREATE TABLE {table_name} ("
        for column in columns:
            sql += f"{column[0]} {column[1]}, "
        sql = sql[:-2] + ")"  # Removes the last comma and add a closing parenthesis

        self.cur.execute(sql)
        self.conn.commit()

    def insert_data(self, table_name: str, data: List[Tuple[Any]]):
        """
        Insert data into the table

        Data should be a list of tuples with values for each column

        For example, [(1, "Alice"), (2, "Bob")]
        """
        placeholders = ", ".join(["?"] * len(data[0]))  # Create placeholders for each value
        sql = f"INSERT INTO {table_name} VALUES {placeholders}"
        self.cur.executemany(sql, data)
        self.conn.commit()

    def query_data(self, table_name: str, condition: str = None) -> List[Tuple]:
        """
        Query data from the table

        Condition is an optional string to filter the results

        For example, "name = 'Alice'"
        """
        sql = f"SELECT * FROM {table_name}"
        if condition:
            sql += f" WHERE {condition}"
        self.cur.execute(sql)
        return self.cur.fetchall()  # Return a list of tuples with the query results

    def close(self):
        """
        Create placeholders for each value
        """
        self.conn.close()
