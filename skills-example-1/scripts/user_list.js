const duckdb = require("duckdb");

// DB作成（ファイル or メモリ）
const db = new duckdb.Database("my_database.db");

// 接続
const conn = db.connect();


// 一覧取得
conn.all("SELECT * FROM my_table", (err, rows) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(rows); // ← 一覧表示
});