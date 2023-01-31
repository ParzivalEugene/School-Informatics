import turtle as t
from typing import Callable

K = 10


def prepare_turtle(func: Callable) -> None:
    """
    Подготавливает черепаху к рисованию.
    """

    def wrapper() -> None:
        t.color("black", "red")
        t.speed(0)
        t.left(90)
        t.begin_fill()
        func()
        t.end_fill()

    return wrapper


def get_number_of_sides(angel: int) -> int:
    """
    Возвращает количество сторон фигуры по заданному углу.
    """
    return 360 // angel


def up():
    t.up()
    t.end_fill()


def down():
    t.down()
    t.begin_fill()


@prepare_turtle
def draw() -> None:
    """
    Рисует данную в задаче фигуру.
    !Как этот шлак работает я хз, но лучше избегать перекрытия фигуры, то есть пройтись по периметру 1 раз!
    Замените код ниже на условие задачи, при использовании функции перемещения домножьте значение на K.
    При поднятие пера вызовите up(), при опускании пера вызовите down().
    Это необходимо для того чтобы заполнение фигур работало корректно.
    """
    # for _ in range(3):  # В условии было 7
    #     t.forward(10 * K)
    #     t.right(120)

    # for _ in range(3):  # В условии было 10
    #     t.forward(6 * K)
    #     t.right(120)

    # for _ in range(3):  # В условии было 15
    #     t.forward(15 * K)
    #     t.right(120)

    for _ in range(min(15, get_number_of_sides(60))):  # В условии было 15
        t.forward(4 * K)
        t.right(60)


def calculate_dots() -> int:
    """
    Возвращает количество точек внутри фигуры.
    Фигура, рисуемая функцией draw, полностью закрашивает свою площадь.
    Эта функция проходит по сетке с шагом K и считает количество закрашенных точек.
    """
    canvas = t.getcanvas()
    counter, area = (
        0,
        100 * K,
    )  # area можно брать больше для перепроверки, если позволяет железо
    for x in range(-area, area, K):
        for y in range(-area, area, K):
            item = canvas.find_overlapping(x, y, x, y)
            if len(item) == 1 and item[0] == 5:
                counter += 1
    return counter


def main():
    draw()
    dots = calculate_dots()
    print(dots)


if __name__ == "__main__":
    main()
