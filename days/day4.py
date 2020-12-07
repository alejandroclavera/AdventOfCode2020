"""
DIA 4
"""
from days.day import Day


class Day4(Day):
    def result_puzzle1(self):
        if self.input1 is None:
            return 0
        return self.valid_passaports(self.input1, check_values=False)

    def result_puzzle2(self):
        if self.input2 is None:
            return 0
        return self.valid_passaports(self.input2, check_values=True)

    def valid_passaports(self, inputfile, check_values=False):
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        # Abre el archivo
        with open(inputfile) as file:
            n_valids = 0
            fields_readed = []
            for line in file:
                # Si la linea no es separadora se trata sus campos
                for field in line.split():
                    field = field.split(':')
                    field_name = field[0]
                    field_value = field[1] if check_values else None
                    # Miramos si ese campo es valido y no esta leido
                    is_valid = self.valid_field(field_name, field_value)
                    if is_valid and field_name not in fields_readed:
                        fields_readed.append(field_name)
                # Si se encuentra en la linea separadora o el ultimo pasaporte se valida
                if line[0] == '\n' or line[-1] != '\n':
                    # Mira si se contienen todos los campos
                    if len(fields_readed) == len(fields):
                        n_valids += 1
                    fields_readed = []
        return n_valids

    def valid_field(self, field, value):
        fields = {
                  'byr': (1920, 2002),
                  'iyr': (2010, 2020),
                  'eyr': (2020, 2030),
                  'hgt': {'cm': (150, 193), 'in': (59, 76)},
                  'hcl': ('0', '9', 'a', 'f'),
                  'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
                  'pid': (0, 9)
                  }
        if value is None:
            return field in fields
        # Campo no valido
        if field not in fields:
            return False
        # Casp hgt
        if field == 'hgt':
            # Comprueba para el caso de cm y el caso de in
            if 'cm' in value:
                return fields[field]['cm'][0] <= int(value.strip('cm')) <= fields[field]['cm'][1]
            elif 'in' in value:
                return fields[field]['in'][0] <= int(value.strip('in')) <= fields[field]['in'][1]
            return False
        # Caso hcl
        if field == 'hcl':
            # Comprueba si hay '#' al principio del valor (se hace de esta forma por si acaso el valor esta vacio)
            if '#' not in value and value[0] != '#':
                return False
            value = value.strip('#')
            # Comprueba que los caracteres sean validos
            for character in value:
                if not (character.isdigit() or fields[field][2] <= character <= fields[field][3]):
                    return False
            # Si todos los caracteres son validos comprueba el número de ellos
            return len(value) == 6
        # Caso elc
        if field == 'ecl':
            return value in fields[field]
        # Caso pid
        if field == 'pid':
            return value.isdigit() and len(value) == 9
        # Resto de campos
        return fields[field][0] <= int(value) <= fields[field][1]






