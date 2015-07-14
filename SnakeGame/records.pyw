from tkinter import *
import os

#глобальные перменные
WIDTH = 500 #ширина окна
HEIGHT = 500 #высота окна

#----------------------------------------------------------
def main():
  #основные поля меню
  c.create_text(WIDTH/2, 30,
                      text="Records",
                      font="Colibri 30",
                      fill="green")

  c.create_text(WIDTH/1.1, HEIGHT - 30,
                      text="[O] k",
                      font="Colibri 20",
                      fill="white")

  f = open ('records.txt','r')
  line = f.readline()
  f.close()
  
  c.create_text(WIDTH/2, HEIGHT - 350,
                      text="Absolute Record",
                      font="Colibri 40",
                      fill="red")
  
  c.create_text(WIDTH/2, HEIGHT - 250,
                      text=line,
                      font="Colibri 30",
                      fill="yellow")
  
def menu(event):
  #переход обратно в меню
  os.startfile('C:/Users/Alter/Desktop/v2/Menu.pyw')
  consol.destroy() 

#------------------------------------------------------------------------------------
#создание окна
consol = Tk()
#название окна
consol.title("Игра Snake")

#создание экземпляра класса Canvas библиотеки tkinter
#используем парметры глобальных переменных (высота, ширина), цвет фона - черный
c = Canvas(consol, width=WIDTH, height=HEIGHT, bg="black")
#помещаем его в "таблицу ячеек" с помощью упаковщика grid 
c.grid()
#наведение фокуса на Canvas для определения нажатия на кнопку
c.focus_set()

consol.bind('o', menu)

#выполнить основную функцию игры
main()
#------------------------------------------------------------------------
#запуск окна
consol.mainloop()
