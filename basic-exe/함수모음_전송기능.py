# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 23:14:23 2025

@author: rogio-new
"""

import time, win32con, win32api, win32gui,ctypes,clipboard
import pyautogui
import 함수모음_기초기능 as 기초기능




# # 채팅방 열기 (완전 일치하지 않으면 열리지 않음)
def open_chatroom(chatroom_name):
    '''
    chatroom_name = '테스트방'
    '''
    # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
        
    hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit1, hwndkakao_edit2, "EVA_Window", None)
    hwndkakao_edit4 = win32gui.FindWindowEx(hwndkakao_edit3, None, "Edit", None)

    # win32gui.SetForegroundWindow(hwndkakao)  # 창을 최전면으로 가져옴
    # win32gui.SetActiveWindow(hwndkakao)  # 창을 활성화 (일부 경우 필요)
    
    
    win32api.SendMessage(hwndkakao_edit4, win32con.WM_SETTEXT, 0, "")
    win32api.SendMessage(hwndkakao_edit4, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(0.5)
    기초기능.SendReturn(hwndkakao_edit4)
    win32api.SendMessage(hwndkakao_edit4, win32con.WM_SETTEXT, 0, "")
    time.sleep(1)
    
    
    hwndMain = win32gui.FindWindow( None, chatroom_name) #채팅방 검색
    
    타이틀 = 기초기능.get_active_window_title()

    if hwndMain == 0:
        print(f'오픈에 실패하였습니다. : {chatroom_name}')
        print(f'{타이틀}')
        
    return hwndMain


# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    '''
    chatroom_name = '테스트방'
    text = '내용'
    '''
    hwndMain = win32gui.FindWindow( None, chatroom_name) #채팅방 검색
    
    
    if hwndMain ==0:
        채팅방 = chatroom_name
        print('채팅방(''%s'')을 오픈합니다.'%채팅방)
        open_chatroom(채팅방)
        hwndMain = win32gui.FindWindow( None, chatroom_name)
            
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)
    
    
    win32api.SendMessage(hwndEdit, win32con.EM_REPLACESEL, 1, text)
    time.sleep(0.3)
    win32api.PostMessage(hwndEdit, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwndEdit, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    
    
for i in range(0,10):
        
        
    kakao_sendtext('테스트방',f'내용{i}')
    print(f'내용{i}')


#%%
def sendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)



def sendText(room, text):
    hwndMain = win32gui.FindWindow(None, room)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RichEdit50W", None)
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    sendReturn(hwndEdit)


