from pyexcel import *

import json
import glob
import warnings

def main(filename):
    warnings.simplefilter(action='ignore', category=UserWarning)
    folders = glob.glob('*/')
    d_l = 100
    reester = []
    while d_l==100:
        d_l = 0
        datas = get_sheet(file_name=filename, start_row=1, row_limit=1000, column_limit=1)
        reester.extend(datas)
        for data in datas:
            if data != ['']:
                for folder in folders:
                    fold = folder.replace(' ', '')
                    if data[0].replace(' ', '') in fold:
                        d_l += 1
                        print(data[0])
                        reester.remove(data)
                        break
        
        break
    return reester
