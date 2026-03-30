#!/bin/bash

export DATABASE_URL=/home/naka/work/rust/sqlite-vec-3/db.sqlite

/home/naka/work/rust/sqlite-vec-3/target/debug/sqlite-vec-3 search $1
