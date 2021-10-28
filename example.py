import csv
import sys

import psycopg
from psycopg.rows import dict_row

CONN_STRING = "postgresql://sonar:sonar@localhost:5432/sonar"

ISSUE_QUERY = """
    SELECT * FROM issues
"""

with psycopg.connect(CONN_STRING) as con, con.cursor(row_factory=dict_row) as cur:
    cur.execute(ISSUE_QUERY)
    rows = list(cur)
    writer = csv.DictWriter(sys.stdout, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
