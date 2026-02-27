import duckdb

conn = duckdb.connect(database='my_database.db')

conn.sql("SELECT * FROM my_table").limit(5).show()

