from tkinter import *

import random

import os

#глобальные перменные
WIDTH = 500 #ширина окна
HEIGHT = 500 #высота окна
PART_SIZE = 25 #размер части змейки и яблока
FL_GM = True #флаг состаяния игры
record = 0
rec = 0

#------------------------------------------------------------------------------------
#создание "яблока"
def create_block():
    global BLOCK
    posx = PART_SIZE * random.randint(1, (WIDTH-PART_SIZE) / PART_SIZE)
    posy = PART_SIZE * random.randint(1, (HEIGHT-PART_SIZE) / PART_SIZE)
     
    # блок это яблоко красного цвета
    BLOCK = cs.create_oval(posx, posy, posx + PART_SIZE, posy + PART_SIZE,
                          fill="red")
#------------------------------------------------------------------------------------
#основная функция управления игры
def main():
    global FL_GM
    global rec
    global record
    #проверка состояния игры
    if FL_GM:
        s.move()
        #определение начала змейки
        head = cs.coords(s.parts[-1].instance)
        x1, y1, x2, y2 = head
        
        #проверка на столкновение змейки со стеной
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            FL_GM = False
 
        # Поедание яблок 
        if head == cs.coords(BLOCK):
            rec=int(rec+1)
            s.add_segment()
            cs.delete(BLOCK)
            create_block()
 
        # Самоедство
        else:
            # Проходим по всем сегментам змеи
            for index in range(len(s.parts)-1):
                if cs.coords(s.parts[index].instance) == head:
                    FL_GM = False
            
        consol.after(100, main)
    #сообщение об окончании игры
    else:
        cs.create_text(WIDTH/2, HEIGHT/3,
                      text="GAME OVER !",
                      font="Colibri 50",
                      fill="red")

        cs.create_text(WIDTH/2, HEIGHT/2+50,
                      text="Score %s" % (rec),
                      font="Colibri 20",
                      fill="yellow")

        #f = open('records.txt','w')
        #f.write(str(0))
        #f.close()

        f = open('records.txt','r')
        line = f.readline()
        record = int(line)
        f.close()

        f = open('records.txt','w')
        if rec > record:
            f.write(str(rec))
        else:
            f.write(str(record))
        f.close()


        cs.create_text(WIDTH/5, HEIGHT-50,
                      text="[B] ack to Menu",
                      font="Colibri 15",
                      fill="blue")

        cs.create_text(WIDTH/1.2, HEIGHT-50,
                      text="[P] lay again",
                      font="Colibri 15",
                      fill="blue")
    

def back_to_menu(event):
    #вернуться в меню
    os.startfile('C:/Users/Alter/Desktop/v2/Menu.pyw')
    consol.destroy()

def restart(event):
    #запуск игры заново
    os.startfile('C:/Users/Alter/Desktop/v2/snake.pyw')
    consol.destroy()
#------------------------------------------------------------------------------------
#класс части змейки
class Part(object):
    #метод создания части змейки заданного размера (PART_SIZE), белого цвета
    def __init__(a, x, y):
        a.instance = cs.create_rectangle(x, y, x+PART_SIZE, y+PART_SIZE, fill="white")
#------------------------------------------------------------------------------------
#класс змейки
class Snake(object):
    #метод создания змейки
    def __init__(a, parts):
        a.parts = parts

        #доступные змейке направления
        a.mapping = {"Right": (1, 0), "Left": (-1, 0),"Down": (0, 1), "Up": (0, -1)}
        #первоначальное напрвление змейки - вправо
        a.vector = a.mapping["Right"]

    #управление змейкой
    #---------------------------------------------------------------------------
    #движение змейки
    def move(a):   
         #рассмотрим все части змейки, за исключением первой
         for index in range(len(a.parts)-1):
              part = a.parts[index].instance
              x1, y1, x2, y2 = cs.coords(a.parts[index+1].instance)
              # задаем каждому сегменту позицию сегмента стоящего после него
              cs.coords(part, x1, y1, x2, y2)
          
         # получаем координаты сегмента перед "головой"
         x1, y1, x2, y2 = cs.coords(a.parts[-2].instance)
          
         # помещаем "голову" в направлении указанном в векторе движения
         cs.coords(a.parts[-1].instance, x1 + a.vector[0]*PART_SIZE,
                   y1 + a.vector[1]*PART_SIZE, x2 + a.vector[0]*PART_SIZE,
                   y2 + a.vector[1]*PART_SIZE)

    #изменение направления
    def change_direction(a, event):
    #event - событие, обозначающее нажатие на кнопку
    #проверка кнопки на обозначение направления
        if event.keysym in a.mapping:
            a.vector = a.mapping[event.keysym] #меняем направление

    #увеличение длины змейки
    def add_segment(a):
        last_seg = cs.coords(a.parts[0].instance)
        x = last_seg[2] - PART_SIZE
        y = last_seg[3] - PART_SIZE
        a.parts.insert(0, Part(x, y))
        
 
#------------------------------------------------------------------------------------
#создание окна
consol = Tk()
#название окна
consol.title("Игра Snake")

#создание экземпляра класса Canvas библиотеки tkinter
#используем парметры глобальных переменных (высота, ширина), цвет фона - черный
cs = Canvas(consol, width=WIDTH, height=HEIGHT, bg="black")
#помещаем его в "таблицу ячеек" с помощью упаковщика grid 
cs.grid()
#наведение фокуса на Canvas для определения нажатия на кнопку
cs.focus_set()

#создание 3 частей змейки (ориентация змейки - горизонтальная)
parts = [Part(PART_SIZE, PART_SIZE), Part(PART_SIZE*2, PART_SIZE),
         Part(PART_SIZE*3, PART_SIZE)]

#создание "змейки" с помощью созданных выше ее частей
s = Snake(parts)
rec = 0

#реакция на нажатие кнопки
cs.bind("<KeyPress>", s.change_direction)

consol.bind('b', back_to_menu)
consol.bind('p', restart)
    
#создать "яблоко"
create_block()

#выполнить основную функцию игры
main()
#------------------------------------------------------------------------
#запуск окна
consol.mainloop()
