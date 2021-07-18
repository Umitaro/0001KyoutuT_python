# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox
#重複したデータだけ出力
import pandas as pd
import numpy as np

data = pd.read_csv('C:/Users/kaika/OneDrive/デスクトップ/-Git/01TestDataCheck/file3.csv',dtype=str,encoding="cp932")
studentinfo = pd.read_csv('C:/Users/kaika/OneDrive/デスクトップ/-Git/01TestDataCheck/studentinfo.csv',dtype=str,encoding="cp932")


cdata = pd.merge(data, studentinfo, on='受験番号', how='left')
cdata.to_csv('C:/Users/kaika/OneDrive/デスクトップ/-Git/01TestDataCheck/file4.csv',index=False,mode = 'w',encoding="cp932")


cdata['在卒高校コード'] = cdata['在卒高校コード'].fillna(cdata['学校コード']).astype(str)
cdata['高校名'] = cdata['高校名'].fillna(cdata['学校名']).astype(str)
print(cdata.columns.get_loc('在卒高校コード'))
print(cdata.columns.get_loc('学校コード'))
print(cdata.columns.get_loc('高校名'))
print(cdata.columns.get_loc('学校名'))
cdata.to_csv('C:/Users/kaika/OneDrive/デスクトップ/-Git/01TestDataCheck/file5.csv',index=False,mode = 'w',encoding="cp932")



