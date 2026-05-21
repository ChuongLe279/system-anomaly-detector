import sqlite3

database = 'Database/metrics.db'
create_table_train = """
    CREATE TABLE IF NOT EXISTS train (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp REAL NOT NULL,
        cpu_percent REAL NOT NULL,
        mem_percent REAL NOT NULL,
        bytes_sent INTEGER NOT NULL,
        bytes_recv INTEGER NOT NULL,
        disk_read INTEGER NOT NULL,
        disk_write INTEGER NOT NULL,
        process_count INTEGER NOT NULL
    );
"""
create_table_test = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp REAL NOT NULL,
        cpu_percent REAL NOT NULL,
        mem_percent REAL NOT NULL,
        bytes_sent INTEGER NOT NULL,
        bytes_recv INTEGER NOT NULL,
        disk_read INTEGER NOT NULL,
        disk_write INTEGER NOT NULL,
        process_count INTEGER NOT NULL
    );
"""
try:
    with sqlite3.connect(database) as conn:
        cursor  = conn.cursor()
        cursor.execute(create_table_train)
        conn.commit()
        cursor.execute(create_table_test)
        conn.commit()
except sqlite3.OperationalError as e:
    print(e)

