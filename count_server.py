import pandas as pd
import openpyxl
from itertools import islice


def count_medicine(filename):
    wb_obj = openpyxl.load_workbook(filename, read_only=True)
    result = {}
    for wb in wb_obj.worksheets:
        res = process_one_wb(wb)
        result[wb.title] = pd.DataFrame([[key, res[key]] for key in res.keys()], columns=['name', 'sold'])
    name = filename.split('.')[0]
    result_file_name = f'{name}_result.xlsx'
    with pd.ExcelWriter(result_file_name) as writer:
        for key in result.keys():
            result[key].to_excel(writer, sheet_name=key, index=False)
    return result_file_name


def process_one_wb(wb):
    values = {}
    for row in islice(wb.rows, 3, None):
        if isinstance(row[2].value, str):
            vals = [str(cell.value) for cell in row if cell.value is not None]
            key_v = vals[0]
            data = ' '.join(vals[2:])
            del vals
            data = data.replace('x', '')
            data = data.replace(' ', '')
            c_sold = data.count('JL')
            if key_v in values.keys():
                values[key_v] = values[key_v] + c_sold
            else:
                values[key_v] = c_sold
    return {k: v for k, v in sorted(values.items(), key=lambda item: item[1])}
