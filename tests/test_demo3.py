from sqlalchemy.dialects.mssql.pymssql import dialect

from sqlglot import parse_one, parse
import sqlglot.expressions as exps
from sqlglot import transpile
from typing import List
import re
import logging
"""format sql with comment"""

sql ="""
select
    a,
    b,
    c
from
    abc_${YYYYmmdd} t1;
    
select
    a,
    b,
    c
from
    abc_${YYYYmmdd} t1;
"""

PATTERN1 = re.compile(r"\$\{[a-zA-Z0-9.]+\}")

def process_sql(sql:str)->str:
    i = 0
    d = {}
    ps= set(PATTERN1.findall(sql))
    for p in ps:
        # print(p)
        mark = 'xxppppp{}pppppxx'.format(str(i))
        d[mark]=p
        sql=sql.replace(p,mark)
        i+=1
    # print(sql)
    out=[]
    result_sqls = transpile(sql,read='hive',write="hive", identify=True, pretty=True)
    for result_sql in result_sqls:
        for k in d:
            result_sql = result_sql.replace(k,d[k])
        out.append(result_sql)
    return ';\n'.join(out)

if __name__ == '__main__':
    result = process_sql(sql)
    print(result)