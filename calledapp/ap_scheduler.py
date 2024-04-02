from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
import pyautogui


def periodic_execution():
    pyautogui.hotkey('ctrl', 'r')
    
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(periodic_execution, 'interval', minutes=1)# 1分おきに実行
    scheduler.star