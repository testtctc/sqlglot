
from sqlglot import parse_one
from typing import List
from sqlglot.expressions import Select,Table,Column
from sqlglot.optimizer.qualify_columns import qualify_columns
from collections import defaultdict

def extract_all_columns(schema:str,table:str):
    """extract all the columns in a table"""
    result=defaultdict(set)
    tree =parse_one(sql)
    print(tree)
    tree:Select=qualify_columns(tree,schema={})
    print(tree)
    table_names = get_all_alias(tree)
    # get projects
    all_columns:List[Column]=list(tree.find_all(Column))
    for column in all_columns:
        table_name =column.table
        column_name = column.name
        if table_name  in table_names:
            table_name = table_names[table_name]
            result[table_name].add(column_name)
    result={key:list(result[key]) for key in result}
    return result

def get_all_alias(tree:Select):
    result ={}
    tables:List[Table] = list(tree.find_all(Table))
    for table in tables:
        table_name = table.name
        alias_name =table.alias_or_name
        result[alias_name]=table_name
    return result


if __name__ == '__main__':
    sql = """
    select
        t1.a,
        t1.b,
        t1.c
    from tbl1 t1
    join tb2 t2
    on t1.id = t2.id
    join tbl3
    on t1.id = tbl3.id
    where t1.name is not null
    """
    result = extract_all_columns(sql,'tbl1')
    print(result)
