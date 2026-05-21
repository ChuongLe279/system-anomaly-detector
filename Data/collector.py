import sqlite3
import psutil
import time


def collect_row():
    net  = psutil.net_io_counters()
    disk = psutil.disk_io_counters()
    return (
        time.time(),
        psutil.cpu_percent(),
        psutil.virtual_memory().percent,
        net.bytes_sent,
        net.bytes_recv,
        disk.read_bytes, # type: ignore
        disk.write_bytes, # type: ignore
        len(psutil.pids()),
    )


def add_data(N, interval=5):
    sql = '''
        INSERT INTO train
            (timestamp, cpu_percent, mem_percent,
             bytes_sent, bytes_recv, disk_read, disk_write, process_count)
        VALUES (?,?,?,?,?,?,?,?)
    '''
    try:
        with sqlite3.connect('Database/metrics.db') as conn:
            psutil.cpu_percent()  
            time.sleep(0.5)

            for i in range(N):
                row = collect_row()
                conn.execute(sql, row)
                # commit every 100 rows
                if i % 100 == 0:  
                    conn.commit()
                    print(f'[{i}/{N}] rows collected')

                time.sleep(interval)
            # final commit for remaining rows
            conn.commit()  
            return conn.execute('SELECT last_insert_rowid()').fetchone()[0]

    except sqlite3.Error as e:
        print(f'DB error: {e}')
    except KeyboardInterrupt:
        print('\nStopped by user — data saved up to last commit')


def main():
    last_id = add_data(N=10, interval=5)
    print(f'Done! Last row id = {last_id}')


if __name__ == '__main__':
    main()
