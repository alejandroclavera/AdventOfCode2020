"""
Dia 10
"""
from days.day import Day

class Day10(Day):

    def result_puzzle1(self):
        if self.input1 is None:
            return 0
        chain = self.get_chain(self.input1)
        return self.count_diferences(chain)

    def result_puzzle2(self):
        if self.input2 is None:
            return 0
        adapters = [0] + self.load_adapters(self.input2)
        return self.all_chains(adapters)

    def count_diferences(self, chain, dif=(1,3)):
        counters = [0] * len(dif)
        for index in range(len(chain)):
            for counter_idx in range(len(dif)):
                if abs(chain[index] - chain[index - 1]) == dif[counter_idx]:
                    counters[counter_idx] += 1
        mult = 1
        for counter in counters:
            mult *= counter
        return mult


    def get_chain(self, file_adapter, max_difference = 3):
        # Obtiene lista ordenada de los adaptadores
        adapters = self.load_adapters(file_adapter)
        chain = [0] # Cadena de adaptadores(optamos por asumir que la salida es tambien un adaptador)
        for index_adapter in range(len(adapters)):
            """
            # Introduce el siquiente adaptador simpre que la diferecia con el anterior 
            no supere la diferencia maxima
            """
            if len(chain) == 0 and adapters[index_adapter] <= max_difference:
                chain.append(adapters[index_adapter])
            elif abs(chain[-1] - adapters[index_adapter]) <= max_difference:
                chain.append(adapters[index_adapter])
            else:
                return []
        # Añade adaptador del dispositivo
        chain.append(chain[-1] + 3)
        return chain

    def load_adapters(self, file_adapter):
        """
        Lee todos los adaptadores de el archivo y los ordena segun la categoria
        """
        with open(file_adapter) as file_adapters:
            adapters = []
            for adapter in file_adapters:
                adapters.append(int(adapter))
        adapters.sort()
        return adapters

    def all_chains(self, adapters, max_diference = 3):
        """
        Para obtener el numero de combinaciones, es suficiente con contar en cuantas combinaciones
        aparece el adaptador del dispositivo, ya que este dispositivo ha de aparecer siempre.

        Para contarlo cuenta cuantas veces es valido usar cada adaptador de forma iterativa, la suma de
        estos he el numero de veces que aparece el adaptador del dispositivo
        """
        next = [adapters[0]]
        next_valids_for_adapters = {adapters[0]:1}
        for adapter in adapters[1:]:
            count = 0
            values = []
            for next_adapter in next:
                if abs(adapter - next_adapter) <= max_diference and next_adapter in adapters:
                    value = next_valids_for_adapters[next_adapter]
                    values.append(value)
            next_valids_for_adapters[adapter] = sum(values)
            next.append(adapter)
            if len(next) > max_diference:
                del next[0]
        return next_valids_for_adapters[adapters[-1]]




