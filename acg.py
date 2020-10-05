import time
import pyautogui as pg

url = "https://www.meteosuisse.admin.ch/home/valeurs-mesurees.html?param=messnetz-webcams&station=DOL"

def _delayedCall(f):
    def outwrapper(delay):
        def wrapper(*args, **kwargs):
            time.sleep(delay)
            return f(*args, **kwargs)
        return wrapper
    return outwrapper

@_delayedCall(8)
def scrollDown(clicks=24):
    pg.scroll(-clicks)


@_delayedCall(8)
def scrollTop():
    pg.scroll(9999)

def select_first_date():
    pg.moveTo(1217, 330, 1)
    pg.leftClick()
    pg.press("Home")
    pg.press("Enter")

def next_date():
    pg.moveTo(1217, 330, 1)
    pg.leftClick()
    pg.press("Down")
    pg.press("Enter")

def select_first_time():
    pg.moveTo(1352, 330, 1)
    pg.leftClick()
    pg.press("Home")
    pg.press("Enter")

def next_time():
    pg.moveTo(1352, 330, 1)
    pg.leftClick()
    pg.press("Down")
    pg.press("Enter")


