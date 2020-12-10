"""
DIA 8
"""
from days.day import Day


class Day8(Day):
    def result_puzzle1(self):
        if self.input1 is None:
            return 0
        return self.acc_value_before_bucle(self.input1)

    def result_puzzle2(self):
        if self.input2 is None:
            return 0
        return self.acc_fixed_program(self.input2)

    def acc_value_before_bucle(self, program_file):
        program = Program()
        # Carga el programa
        program.load_program(program_file)
        # Si la siguiente instruccion ya se ha ejecutado una vez finaliza
        while program.get_next()[1] < 1:
            program.next()
        return program.acc

    def acc_fixed_program(self, program_file):
        """
        Busca la istruccion que provoca el bulce realizando la misma accion
        que el puzzle anterior pero esta vez se guardara el contador de programa para poder
        localizar la instrucción
        """
        program = Program()
        # Carga el programa
        program.load_program(program_file)
        # Guarda todos los valores del pc hasta llegar al bucle
        pcs = []
        while program.get_next()[1] < 2:
           pcs.append(program.next())

        """
        De valor del pc se evalua si la instruacción se puede cambiar para arreglar el bucle.
        Se recorre desde la ultimo valor del pc hasta al primero ya que los ultimos son mas probable
        que lleven al bucle
        """
        for pc in list(reversed(pcs)):
            fix = False
            instruction, n, is_decoded = program.program[pc]
            if instruction[0] == 'nop' and instruction[1] != 0:
                last = instruction[0]
                instruction[0] = 'jmp'
                program.program[pc] = (instruction, 0, is_decoded)
                fix = True
            elif instruction[0] == 'jmp' and instruction[1] < 0:
                last = instruction[0]
                instruction[0] = 'nop'
                program.program[pc] = (instruction, 0, is_decoded)
                fix = True
            if fix:
                program.reset() # restea todos los contadores
                if self.have_loop(program): # No se ha solucionado el bucle
                    # Recupera la anterior instruccion
                    instruction[0] = last
                    program.program[pc] = (instruction, 0, is_decoded)
                else:
                    return program.acc # Se ha solucionado el bucle
        return -1

    def have_loop(self, program):
        while True:
            pc = program.next()
            if pc == -1:
                # Ha llegado al final
                return False
            if program.program[pc][1] > 1:
                return True

class Program:
    def __init__(self):
        self.acc = 0 # Acumulador
        self.pc = 0 # Contador de programa
        self.program = []

    def load_program(self, program_file):
        # Abre el fichero del programa
        with open(program_file) as program:
            # Guarda cada instruccion en la lista
            for instruction in program:
                # Añade la instruccion a la lista mediatne una tupla
                # Tupla (instruccion, numero ejecucione, descodificada o no)
                self.program.append((instruction, 0, False))

    def decode(self, instruction):
        instruction = instruction.split(' ')
        if len(instruction) < 2:
            return instruction
        for index in range(1, len(instruction)):
            instruction[index] = int(instruction[index])
        return instruction

    def next(self):
        # Si el contador de programa esta al final del programa marca -1
        if self.pc >= len(self.program):
            return -1
        # Si hay istrucciones por ejecutar optiene la intrucción
        instruction, n, is_decoded = self.program[self.pc]

        # Si no esta descodificada la descodifica
        if not is_decoded:
            instruction = self.decode(instruction)

        # Acualiza el contador de ejecuciones y se guarada el contador de programa
        self.program[self.pc] = (instruction, n + 1, True)
        pc = self.pc

        # Ejecuta la instruccion
        if instruction[0] == 'acc':
            self.acc += instruction[1]
            self.pc += 1
        elif instruction[0] == 'jmp':
            self.pc += instruction[1]
        elif instruction[0] == 'nop':
            self.pc += 1
            self.next()
        else:
            print('Operacion no valida')
            exit(0)
        return pc

    def get_next(self):
        return self.program[self.pc]

    def reset(self):
        self.pc = 0
        self.acc = 0
        for pc, instrucction in enumerate(self.program):
            self.program[pc] = (instrucction[0], 0, instrucction[2])
