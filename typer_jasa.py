import tkinter
from tkinter import W

import pyautogui
# import time

# is an app to help user to input/entry master setting of "JASA"


main_window = tkinter.Tk()
main_window.geometry("900x200")

tkinter.Label(main_window, text="start date:")\
    .grid(row=0, column=0, sticky=W, pady=2)  # Start Year Period
tkinter.Label(main_window, text="*01/01/2022 or 01012022")\
    .grid(row=0, column=2, sticky=W, pady=2)  # year_example
tkinter.Label(main_window, text="end date:")\
    .grid(row=1, column=0, sticky=W, pady=2)  # End Year Period
tkinter.Label(main_window, text="*01/01/2022 or 01012022")\
    .grid(row=1, column=2, sticky=W, pady=2)  # year_example
tkinter.Label(main_window, text="% non penindak langsung")\
    .grid(row=2, column=0, sticky=W, pady=2)  # percentage of penindak langsung
tkinter.Label(main_window, text="% penindak langsung")\
    .grid(row=3, column=0, sticky=W, pady=2)  # percentage of non penindak langsung
tkinter.Label(main_window, text="% D operator")\
    .grid(row=4, column=0, sticky=W, pady=2)  # percentage of dokter operator share
tkinter.Label(main_window, text="% perawat")\
    .grid(row=5, column=0, sticky=W, pady=2)  # percentage of perawat share
tkinter.Label(main_window, text="% radiografer")\
    .grid(row=6, column=0, sticky=W, pady=2)  # percentage of radiografer share


# FIELD TEXT_BOX
startDate = tkinter.Entry(main_window)
endDate = tkinter.Entry(main_window)
nonLangsung = tkinter.Entry(main_window)
langsung = tkinter.Entry(main_window)
dOperator = tkinter.Entry(main_window)
perawat = tkinter.Entry(main_window)
radiografer = tkinter.Entry(main_window)

# TEXT_BOX POSITIONING
startDate.grid(row=0, column=1)
endDate.grid(row=1, column=1)
nonLangsung.grid(row=2, column=1)
langsung.grid(row=3, column=1)
dOperator.grid(row=4, column=1)
perawat.grid(row=5, column=1)
radiografer.grid(row=6, column=1)


def tunai():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')  # <==alt tab

    pyautogui.press('f5')  # Setting Group
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(startDate.get()))
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
    pyautogui.write(str(endDate.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('kelo')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(nonLangsung.get()))
    pyautogui.hotkey('alt', 't')
    pyautogui.write('kelom')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(langsung.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('up')
    pyautogui.press('f5')
    pyautogui.write('non')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('f5')
    pyautogui.write('dd')
    pyautogui.press('tab')
    pyautogui.write(str(dOperator.get()))
    pyautogui.hotkey('alt', 't')
    pyautogui.write('rr')
    pyautogui.press('tab')
    pyautogui.write(str(radiografer.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked


def jaminan():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')  # <==alt tab

    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write(str(startDate.get()))
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'shiftleft', 'shiftright', 'right')
    pyautogui.write(str(endDate.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('f5')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('in')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write('12')
    pyautogui.hotkey('alt', 't')
    pyautogui.write('ke')
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('tab')
    pyautogui.write('88')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('f5')
    pyautogui.write('kelo')
    pyautogui.press('tab')
    pyautogui.write(str(nonLangsung.get()))
    pyautogui.hotkey('alt', 't')
    pyautogui.write('kelom')
    pyautogui.press('tab')
    pyautogui.write(str(langsung.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('up')
    pyautogui.press('f5')
    pyautogui.write('non')
    pyautogui.press('tab')
    pyautogui.write('100')
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked

    pyautogui.press('pagedown')
    pyautogui.press('f5')
    pyautogui.write('dd')
    pyautogui.press('tab')
    pyautogui.write(str(dOperator.get()))
    pyautogui.hotkey('alt', 't')
    pyautogui.write('rr')
    pyautogui.press('tab')
    pyautogui.write(str(radiografer.get()))
    pyautogui.hotkey('alt', 's')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'k')  # checked


def repeating():
    pyautogui.press('tab')
    pyautogui.press('tab')


tombolJaminan = tkinter.Button(main_window, text="JAMINAN", command=jaminan)
tombolJaminan.grid(row=7, column=0)


tombolTunai = tkinter.Button(main_window, text="TUNAI", command=tunai)
tombolTunai.grid(row=7, column=3)

if __name__ == "__main__":
    main_window.mainloop()
