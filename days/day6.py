from days.day import Day


class Day6(Day):

    def result_puzzle1(self):
        if self.input1 is None:
            return 0
        return self.get_answers_group_sum(self.input1)

    def result_puzzle2(self):
        if self.input2 is None:
            return 0
        return self.get_answers_group_sum(self.input2, everyone_answered=True)

    def get_answers_group_sum(self, answers_file, everyone_answered=False):
        # Abre el fichero
        with open(answers_file) as answers_list:
            # Cuenta las respuestas linea a linea
            answers_group = []
            total_answers = 0
            for answers_line in answers_list:
                # Strip answers_line
                answers = answers_line.strip('\n')

                if everyone_answered:
                    answers_group = self.count_everyone_answered(answers, answers_group)
                else:
                    answers_group = self.count_answers_group(answers, answers_group)

                # Comprueba si se ha llegado al final del grupo
                if answers_line[0] == '\n' or answers_line[-1] != '\n':
                    if len(answers_group) != 0 and answers_group[0] != -1:
                        total_answers += len(answers_group)
                    answers_group = []
        return total_answers

    def count_answers_group(self, answers, current_answers_group):
        for answer in answers:
            if answer not in current_answers_group:
                current_answers_group.append(answer)
        return current_answers_group

    def count_everyone_answered(self, answers, current_answers_group):
        answers_list = []
        # Si no hay respuestas
        if len(answers) == 0:
            return current_answers_group
        # Si no se ha contado ninguna respuesta todavia
        if len(current_answers_group) == 0:
            return self.count_answers_group(answers, current_answers_group)
        """
        Si se encuentra una lista con un -1 marca que todos los miembros
        del grupo no tienen en comun ninguna respuesta
        """
        if current_answers_group[0] == -1:
            return current_answers_group

        # Añade todas las respuestas
        for answer in answers:
            answers_list.append(answer)

        # Elimina de las respustas comunes del grupo actuales las cuales ya no sean
        new_answers_group = []
        for answer in current_answers_group:
            if answer in answers_list:
                new_answers_group.append(answer)
                
        # Si no hay ninguna respuesta en comun en todo el grupo se marca con [-1]
        if len(new_answers_group) == 0:
            new_answers_group = [-1]

        return new_answers_group



