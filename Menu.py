from tkinter import *

import random
import os

#глобальные перменные
WIDTH = 500 #ширина окна
HEIGHT = 500 #высота окна
    
#------------------------------------------------------------------------------------
#основная функция Menu
def main():
  #основные поля меню
  c.create_text(WIDTH/2, 40,
                      text="MENU",
                      font="Colibri 30",
                      fill="green")

  c.create_text(WIDTH/2, 150,
                      text="[S] tart game",
                      font="Colibri 20",
                      fill="white")

  c.create_text(WIDTH/2, 200,
                      text="[R] ecords",
                      font="Colibri 20",
                      fill="white")

  c.create_text(WIDTH/2, 250,
                      text="[H] elp",
                      font="Colibri 20",
                      fill="white")

  c.create_text(WIDTH/2, 300,
                      text="[E] xit",
                      font="Colibri 20",
                      fill="white")

  c.create_text(WIDTH/2, 450,
                      text="Choose and Press [KEY]",
                      font="Colibri 10",
                      fill="blue")
     
def start(event):
  #запуск окна игры
  root.destroy()

def records(event):
  #запуск окна "рекорды"
  root.destroy()

def helps(event):
  #запуск окна "помощь"
  root.destroy()
    
def _exit(event):
  root.destroy()
            
#------------------------------------------------------------------------------------
#создание окна
root = Tk()
#название окна
root.title("Игра Snake")
 
#создание экземпляра класса Canvas библиотеки tkinter
#используем парметры глобальных переменных (высота, ширина), цвет фона - черный
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
#помещаем его в "таблицу ячеек" с помощью упаковщика grid 
c.grid()
#наведение фокуса на Canvas для определения нажатия на кнопку
c.focus_set()

root.bind('s', start)
root.bind('r', records)
root.bind('h', helps)
root.bind('e', _exit)

main()

#------------------------------------------------------------------------
#запуск окна
root.mainloop()
