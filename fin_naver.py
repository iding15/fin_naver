from Chrome import sel
from quant import CheckBox, remove_sheet, save_sheet
import time
import pandas as pd
import openpyxl
import datetime

l_idName=["option1","option15","option21","option18","option24","option27"]
get_url=sel("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0")
for i in l_idName:
    get_url.ClickTool("id",i)

get_url.ClickTool("xpath","//img[@alt='적용하기']")
time.sleep(1.5)

table_head = "//table[@class='type_2']/thead"
table_body = "//table[@class='type_2']/tbody"
data = get_url.table(table_head, table_body)
write_wb = openpyxl.Workbook()
write_ws = write_wb.active
for d in data:
    write_ws.append(d)

c_ = 2
while True:
    try:
        ref = "//a[@href="+\
        "'/sise/sise_market_sum.nhn?sosok=0&page="+str(c_)+"']"
        get_url.ClickTool("xpath", ref)
        ndata = get_url.table(table_head, table_body, header=False)
        for n in ndata:
            write_ws.append(n)
        c_ = c_+1
    except:
        break
get_url.driverClose()

now = datetime.datetime.now()
nowDate = now.strftime('%y%m%d')
address = './DATA/'+nowDate+'.xlsx'

write_wb.save(address)

pd_data = CheckBox(nowDate)
save_sheet(nowDate, pd_data.delNan(), 'Data')
remove_sheet(nowDate, 'Sheet')
