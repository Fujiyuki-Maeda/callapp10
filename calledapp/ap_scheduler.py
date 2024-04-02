from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import pyautogui
import webbrowser


def periodic_execution():
    pyautogui.hotkey('ctrl', 'r')
    print("更新")
    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution, 'interval', minutes=1)# 1分おきに実行
    scheduler.star
    
    webbrowser.open("https://fujiyukimaeda.pythonanywhere.com/index/")