from frcteam195.database import connect


def get(cmd):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(cmd)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return results
