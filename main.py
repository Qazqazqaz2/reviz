from pyexcel import *

import json
import glob
import warnings

def main(filename):
    warnings.simplefilter(action='ignore', category=UserWarning)
    folders = glob.glob('*/')
    d_l = 1000
    reester = []
    try:
        while d_l==1000:
            d_l = 0
            datas = get_sheet(file_name=filename, start_row=1, row_limit=1000, column_limit=1)
            reester.extend(datas)
            for data in datas:
                if data != ['']:
                    for folder in folders:
                        fold = folder.replace(' ', '')
                        print(data[0])
                        if str(data[0]).replace(' ', '') in fold:
                            d_l += 1
                            print(data[0])
                            reester.remove(data)
                            break
            break
    except:
        print(1111)
    return reester
