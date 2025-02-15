from sqlglot import parse_one
import sqlglot.expressions as exps


def modify_sql()->str:
    sql = 'select a from table'
    ast = parse_one(sql)
    new_ast = ast.transform(change_column_name)
    return  new_ast.sql()


def change_column_name(node: exps.Expression) -> exps.Expression:
    if isinstance(node, exps.Column) and node.name == 'a':
        return parse_one("date(a)")
    return node


if __name__ == '__main__':
    sql = modify_sql()
    print(sql)