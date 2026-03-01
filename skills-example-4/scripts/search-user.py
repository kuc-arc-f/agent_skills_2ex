import duckdb
import sys

conn = duckdb.connect(database='my_database.db')
#
#
#
def search_user(id):
    #print(f"id= {id}")
    select_sql = """SELECT 
    ID, 
    Name, 
    Age
    FROM my_table WHERE ID = ?
    """

    resp = conn.execute(select_sql, [id]).fetchall()
    #print(resp)
    ouStr = "" 
    for row in resp:
        #print(row[0])
        ouStr += f"ID: {row[0]} \n"
        ouStr += f"Name: {row[1]} \n"
        ouStr += f"Age: {row[2]} \n\n"

    print(ouStr) 
#
#
#
if __name__ == "__main__":
    args = sys.argv
    #print(f"実行ファイル名: {args[0]}")
    if len(args) > 1:
        #print(f"最初の引数: {args[1]}")
        #print(f"引数 2: {args[2]}")
        id = args[2]
        search_user(str(id))
    else:
        print("error, nothing args")
