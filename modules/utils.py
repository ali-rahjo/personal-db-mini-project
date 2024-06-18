from prettytable import PrettyTable

def print_table(headers, rows):
    table = PrettyTable(headers)
    for row in rows:
        table.add_row(row)
    print(table)
