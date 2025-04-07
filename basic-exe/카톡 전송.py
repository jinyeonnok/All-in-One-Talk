# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:08:10 2023

@author: Rogio
"""

import time, win32con, win32api, win32gui
import pandas as pd


# # 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = '진연녹'


# 카톡메시지 = pd.read_excel(r'C:\Users\dudtl\Desktop/카톡 테스트.xlsx')
카톡메시지 = pd.DataFrame({1,2,3})
#%%

for i in range(0,len(카톡메시지)):
    
    대상 = 카톡메시지.iloc[i,0]
    text = 카톡메시지.iloc[i,1]
    print(대상)
    
    hwndMain = win32gui.FindWindow( None, 대상)
    
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RICHEDIT50W", None)
    
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    
    win32api.PostMessage(hwndEdit, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwndEdit, win32con.WM_KEYUP, win32con.VK_RETURN, 0)