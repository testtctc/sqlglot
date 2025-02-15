
from sqlglot import parse_one
import sqlglot.expressions as exps
from typing import List

"""为列添加别名"""

def parse_columns(sql:str) -> List[str]:
    abs:exps.Select = parse_one(sql,dialect='hive',into=exps.Select)
    return abs.named_selects


def add_table_alias(sql,table_alias ='t1'):
    columns = parse_columns(sql)
    out = ['{}.{}'.format(table_alias,c) for c in columns]
    return ',\n'.join(out)

if __name__ == '__main__':
    sql = 'select abs as a, bcd as b, cdb as d from tbl'
    result = add_table_alias(sql)
    print(result)