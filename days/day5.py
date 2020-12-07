"""
DIA 5
"""
from days.day import Day


class Day5(Day):

    def result_puzzle1(self):
        if self.input1 is None:
            return -1
        return self.get_maxid(self.input1)

    def result_puzzle2(self):
        max_id, id_seats = self.get_maxid(self.input1, get_all_id=True)
        for id in range(max_id + 1):
            if id not in id_seats and id - 1 in id_seats and id + 1 in id_seats:
                return id
        return -1

    def get_maxid(self, boarding_passes_file, get_all_id=False):
        # Abre el fichero
        all_id = []
        with open(boarding_passes_file) as boarding_passes:
            # Lee uno a uno los pases de embarque
            max_id = -1
            for boarding_pass in boarding_passes:
                # Calcula el id del asiento del pase de embarque actual
                id = self.calc_id(boarding_pass)
                # Compruba si el id es mayor que la mayor actual
                if id > max_id:
                    max_id = id
                # Si se pide obtener todas las id se añade a la lista
                if get_all_id:
                    all_id.append(id)
        if get_all_id:
            return  max_id, all_id
        return max_id

    def calc_id(self, boarding_pass):
        row = 0
        col = 0
        # Definicion de los rangos de la region inicial
        first = 0
        end = 127
        for i in range(7):
            if boarding_pass[i] == 'F':
                end = int((end - first) / 2) + first
            elif boarding_pass[i] == 'B':
                first = int((end - first) / 2) + 1 + first
        row = first
        first = 0
        end = 7
        for i in range(7,10):
            if boarding_pass[i] == 'L':
                end = int((end - first) / 2) + first
            elif boarding_pass[i] == 'R':
                first = int(((end - first) / 2)) + 1 + first
        col = first
        return row * 8 + col



