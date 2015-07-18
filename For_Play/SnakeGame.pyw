from tkinter import *

import random
import os

#глобальные перменные
WIDTH = 500 #ширина окна
HEIGHT = 500 #высота окна
PART_SIZE = 25 #размер части змейки и яблока
record = 0#рекорд из текстового файла
rec = 0#количество очков текущей игры
    
#------------------------------------------------------------------------------------
#основная функция Menu
def main_menu():
  #наименование окна меню
  c.create_text(WIDTH/2, 40,
                      text="MENU",
                      font="Colibri 30",
                      fill="green")
  #основные поля меню
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
#----------------------------------------------------------------------------
#функция для Records
def main_records():
  #наименование поля рекорда
  c.create_text(WIDTH/2, 30,
                      text="Records",
                      font="Colibri 30",
                      fill="green")
  #указатель на клавишу для перехода в меню
  c.create_text(WIDTH/1.1, HEIGHT - 30,
                      text="[O] k",
                      font="Colibri 20",
                      fill="white")

  #подзаголовок поля рекорда "Абсолютный рекорд"
  c.create_text(WIDTH/2, HEIGHT - 350,
                      text="Absolute Record",
                      font="Colibri 40",
                      fill="red")

  #проверка на наличие файла с рекордом
  try:
      #открываем файл, содержащий абсолютный рекорд игры
      f = open('records.txt','r')
  except IOError as e:
          #вывод количества заработанных очков за текущую игру
          c.create_text(WIDTH/2, HEIGHT - 250,
          text=str(0),
          font="Colibri 30",
          fill="yellow") 
  else:
      with f:
            #считывания числа, являющегося абсолютным рекордом игры
            line = f.readline()
            #закрытие файла
            f.close()
            #вывод количества заработанных очков за текущую игру
            c.create_text(WIDTH/2, HEIGHT - 250,
                      text=line,
                      font="Colibri 30",
                      fill="yellow")
#----------------------------------------------------------------------------
#функция для Help
def main_helps():
  #наименование поля помощи
  c.create_text(WIDTH/2, 30,
                      text="Help",
                      font="Colibri 30",
                      fill="green")
  ##указатель на клавишу для перехода в меню
  c.create_text(WIDTH/1.1, HEIGHT - 30,
                      text="[O] k",
                      font="Colibri 20",
                      fill="white")

  #основное описание управления игрой
  c.create_text(WIDTH/2, 230,
            text='Правила игры "Snake" следующие:\n\
  На поле находится “змейка”, у которой есть\n\
фиксированное количество направлений движения: \n\
“вправо”, ”влево”, ”вверх”, ”вниз”,\n\
а также яблоко, за которым она охотится.\n\
  С каждым пойманным яблоком длина “змейки” \n\
увеличивается на единицу ее части.\n\
\n Управлять “змейкой” Вы сможете, \n\
используя  клавиши клавиатуры: \n\
       - ”вправо”, \n\
       - ”влево”, \n\
       - ”вверх”, \n\
       - ”вниз”\n\
\n  Главное условие перемещения “змейки” \n\
– не врезаться головой о границы поля и \n\
не “съесть” себя, иначе игра будет окончена.',
                      font="Colibri 10",
                      fill="white")

#----------------------------------------------------------------------------
#функции игры
#------------------------------------------------------------------------------------
#основная функция управления игры
def main_game():
    global FL_GM # флаг состояния игры
    global rec # текущее число заработанных очков
    global record # абсолютный рекорд игры
    
    #проверка состояния игры
    if FL_GM:
        #перемещение змейки
        s.move()
        #определение начала змейки
        head = c.coords(s.parts[-1].instance)
        x1, y1, x2, y2 = head
        
        #проверка на столкновение змейки со стеной
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            FL_GM = False
 
        # Поедание яблок 
        if head == c.coords(BLOCK):
            rec=int(rec+1)#увеличиваем число заработанных очков
            s.add_segment()#увеличиваем длину змейки
            c.delete(BLOCK)#удаляем с поля съеденное яблоко
            create_block()#создаем новое яблоко на поле
 
        # Самоедство
        else:
            # Проходим по всем сегментам змеи
            for index in range(len(s.parts)-1):
                #если координата тела змейки совпала с координатой ее головы
                if c.coords(s.parts[index].instance) == head:
                    #флаг состояния игры = ложь
                    FL_GM = False
        #задержка выполнения функции main_game
        root.after(100, main_game)
    #сообщение об окончании игры
    else:
        #выдаем сообщение об окнчании игры
        c.create_text(WIDTH/2, HEIGHT/3,
                      text="GAME OVER !",
                      font="Colibri 50",
                      fill="red")
        #выдаем количество заработанных очков
        c.create_text(WIDTH/2, HEIGHT/2+50,
                      text="Score %s" % (rec),
                      font="Colibri 20",
                      fill="yellow")

        #указатель на клавишу для перехода в меню
        c.create_text(WIDTH/5, HEIGHT-50,
                      text="[B] ack to Menu",
                      font="Colibri 15",
                      fill="blue")
        #указатель на клавишу для переигровки
        c.create_text(WIDTH/1.2, HEIGHT-50,
                      text="[P] lay again",
                      font="Colibri 15",
                      fill="blue")
        fl_file = True
        #проверка на наличие файла с рекордом
        try:
            #открываем файл, содержащий абсолютный рекорд игры
            f = open('records.txt','r')
        except IOError as e:
            fl_file=False
        else:
          with f:
            #считываем строчку
            line = f.readline()
            #приводим ее к целочисленному типу
            record = int(line)
            f.close()
            #если количество заработанных очков в текущей игре
            #превосходит предыдущий рекорд, то обновляем его
            if rec > record:
              record = int(rec)
              #выдаем сообщение о новом рекорде
              c.create_text(WIDTH/2, HEIGHT/2+100,
                      text="New Record !",
                      font="Colibri 30",
                      fill="yellow")
            #записываем его в файл
            #открываем файл и записываем в него рекорд
            f = open('records.txt','w')
            f.write(str(record))
            #закрываем файл
            f.close()

        #если файла с рекордом не существует, то создаем его
        #и записываем в него результат текущей игры
        if fl_file == False:
          f = open('records.txt', 'w')
          f.write(str(rec))
          f.close()
          #выдаем сообщение о новом рекорде
          c.create_text(WIDTH/2, HEIGHT/2+100,
                      text="New Record !",
                      font="Colibri 30",
                      fill="yellow")
#------------------------------------------------------------------------------------
#создание "яблока"
def create_block():
    global BLOCK
    #рандомное определение координаты нового яблока
    posx = PART_SIZE * random.randint(1, (WIDTH-PART_SIZE) / PART_SIZE)
    posy = PART_SIZE * random.randint(1, (HEIGHT-PART_SIZE) / PART_SIZE)
     
    # блок это яблоко красного цвета
    BLOCK = c.create_oval(posx, posy, posx + PART_SIZE, posy + PART_SIZE,
                          fill="red")

#------------------------------------------------------------------------------------
#класс части змейки
class Part(object):
    #метод создания части змейки заданного размера (PART_SIZE), белого цвета
    def __init__(a, x, y):
        a.instance = c.create_rectangle(x, y, x+PART_SIZE, y+PART_SIZE, fill="white")
#------------------------------------------------------------------------------------
#класс змейки
class Snake(object):
    #метод создания змейки
    def __init__(a, parts):
        #компануем все сегменты змейки
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
              part = a.parts[index].instance#определение сегмента с помощью функции instance
              x1, y1, x2, y2 = c.coords(a.parts[index+1].instance)
              # задаем каждому сегменту позицию сегмента стоящего после него
              c.coords(part, x1, y1, x2, y2)
          
         # получаем координаты сегмента перед "головой"
         x1, y1, x2, y2 = c.coords(a.parts[-2].instance)
          
         # помещаем "голову" в направлении указанном в векторе движения
         c.coords(a.parts[-1].instance, x1 + a.vector[0]*PART_SIZE,
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
        #определяем координаты хвоста змейки
        last_seg = c.coords(a.parts[0].instance)
        x = last_seg[2] - PART_SIZE
        y = last_seg[3] - PART_SIZE
        #добавляем на это место сегмент
        a.parts.insert(0, Part(x, y))
        
#------------------------------------------------------------------------------------
#подготовка окна для перехода в меню
def menu(event):
    #очищаем поле
    c.delete('all')
    #переход к функции меню
    main_menu()
    #определение клавиш для реагирования
    root.bind('s', start)#начало игры
    root.bind('r', records)#рекорд
    root.bind('h', helps)#помощь
    root.bind('e', _exit)#выход
    
#------------------------------------------------------------------------------------
#подготовка окна к началу игры   
def start(event):
    #очищаем поле
    c.delete('all')
    #определение клавиш для реагирования
    root.bind('b', menu)#переход в меню
    root.bind('p', restart)#переиграть

    #помещаем его в "таблицу ячеек" с помощью упаковщика grid 
    c.grid()
    #наведение фокуса на Canvas для определения нажатия на кнопку
    c.focus_set()
    #создание 3 частей змейки (ориентация змейки - горизонтальная)
    parts = [Part(PART_SIZE, PART_SIZE), Part(PART_SIZE*2, PART_SIZE),
         Part(PART_SIZE*3, PART_SIZE)]

    #создание "змейки" с помощью созданных выше ее частей
    global s
    s = Snake(parts)

    #флаг состояния игры
    global FL_GM
    FL_GM = True

    #зануляем текущее количество очков
    rec = 0

    #реакция на нажатие кнопки
    c.bind("<KeyPress>", s.change_direction)

    #создать "яблоко"
    create_block()

    #выполнить основную функцию игры
    main_game()
    
#------------------------------------------------------------------------------------
#подготовка к переходу окна в поле рекорда
def records(event):
    #очищаем поле
    c.delete('all')
    #определение клавиши для реагирования
    root.bind('o', menu)#переход в меню

    #функция поля рекорда
    main_records()
    
#------------------------------------------------------------------------------------
#подготовка окна к переходу в поле помощи
def helps(event):
    #очищаем поле
    c.delete('all')
    #определение клавиши для реагирования
    root.bind('o', menu)

    #функция поля помощи
    main_helps()
    
#------------------------------------------------------------------------------------
#подготовка окна к переигровке
def restart(event):
    #флаг состояния игры
    global FL_GM
    FL_GM = True

    #функция начала игры
    start(event)
    
#------------------------------------------------------------------------------------
#выход из игры   
def _exit(event):
    #удаляем окно
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

#определение клавиш для реагирования
root.bind('s', start)#начало игры
root.bind('r', records)#рекорд
root.bind('h', helps)#помощь
root.bind('e', _exit)#выход

#функция меню
main_menu()

#------------------------------------------------------------------------
#запуск окна
root.mainloop()
