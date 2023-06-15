from typing import NamedTuple


class Cell(NamedTuple):
    check_in_time: int
    check_out_time: int


def main():
    with open("data/26.txt", encoding="utf-8") as file:
        raw = file.readlines()
        amount_of_cells, amount_of_passengers = map(int, raw[:2])
        passengers = sorted(Cell(*list(map(int, i.split()))) for i in raw[2:])

        locker = [Cell(0, 0)] * amount_of_cells
        counter, last_cell = 0, 0
        for passenger in passengers:
            for cell_id, cell in enumerate(locker):
                if passenger.check_in_time > cell.check_out_time:
                    counter += 1
                    locker[cell_id] = passenger
                    last_cell = cell_id + 1
                    break
        print(counter, last_cell)


main()
