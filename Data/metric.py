import sqlite3

database = 'Database/metrics.db'
create_table = """
    CREATE TABLE IF NOT EXISTS metrics (
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
        cursor.execute(create_table)
        conn.commit()
except sqlite3.OperationalError as e:
    print(e)

