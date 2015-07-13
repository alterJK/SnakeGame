from tkinter import * # подключение графической библиотеки

#глобальные перменные
WIDTH = 500 #ширина окна
HEIGHT = 500 #высота окна
PART_SIZE = 25 #размер части змейки
FL_GM = True #флаг состаяния игры 

#------------------------------------------------------------------------------------
#основная функция управления игры
def main():
    global FL_GM

    #проверка состояния игры
    if FL_GM:
        #змека начинает свое движение
        s.move()

        #определение начала змейки
        head = cs.coords(s.parts[-1].instance)
        x1, y1, x2, y2 = head
        
        #проверка на столкновение змейки со стеной
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            FL_GM = False

            
        consol.after(100, main)
    #сообщение об окончании игры
    else:
        cs.create_text(WIDTH/2, HEIGHT/3,
                      text="GAME OVER !",
                      font="Colibri 50",
                      fill="red")

#------------------------------------------------------------------------------------
#создание "яблока"

#------------------------------------------------------------------------------------
#класс части змейки
class Part(object):
    #метод создания части змейки заданного размера (PART_SIZE), белого цвета
    def __init__(a, x, y):
        a.instance = cs.create_rectangle(x, y, x+PART_SIZE, y+PART_SIZE, fill="white")

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

#создание частей змейки (ореинтация змейки - горизонтальная)
parts = [Part(PART_SIZE, PART_SIZE), Part(PART_SIZE*2, PART_SIZE), Part(PART_SIZE*3, PART_SIZE)]

#создание "змейки" с помощью созданных выше ее частей
s = Snake(parts)

#реакция на нажатие кнопки
cs.bind("<KeyPress>", s.change_direction)

#выполнить основную функцию игры
main()
#------------------------------------------------------------------------
#запуск окна
consol.mainloop()
