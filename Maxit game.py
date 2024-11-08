import random

class MaxitGame:
    def __init__(self):
        self.board = self.generate_board()
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.last_choice = None  # Хранит последнюю выбранную клетку
        self.is_game_over = False

    def generate_board(self):
        """Генерирует игровое поле 3x3 с числами от 1 до 9"""
        numbers = random.sample(range(1, 10), 9)
        return [numbers[i:i + 3] for i in range(0, 9, 3)]

    def display_board(self):
        """Выводит текущее состояние игрового поля"""
        print("Текущая доска:")
        for row in self.board:
            print(" | ".join(map(str, row)))
        print()

    def get_available_moves(self):
        """Возвращает доступные ходы для текущего игрока"""
        if self.current_player == 1:
            # Игрок 1 выбирает из всей доски
            return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is not None]
        else:
            # Игрок 2 выбирает из столбца последнего хода игрока 1
            col = self.last_choice[1] if self.last_choice else None
            if col is not None:
                return [(i, col) for i in range(3) if self.board[i][col] is not None]
            return []

    def make_move(self, row, col):
        """Исполняет ход, обновляет счет и игровое поле"""
        if self.current_player == 1:
            self.player1_score += self.board[row][col]
        else:
            self.player2_score += self.board[row][col]

        # Убираем число с доски
        self.board[row][col] = None
        self.last_choice = (row, col)
        
        # Меняем игрока
        self.current_player = 2 if self.current_player == 1 else 1

    def check_game_over(self):
        """Проверяет, закончилась ли игра"""
        if not self.get_available_moves():
            self.is_game_over = True

    def display_scores(self):
        """Выводит текущие счеты"""
        print(f"Счет игрока 1: {self.player1_score}")
        print(f"Счет игрока 2: {self.player2_score}")
        print()

    def determine_winner(self):
        """Определяет победителя"""
        if self.player1_score > self.player2_score:
            return "Игрок 1 выигрывает!"
        elif self.player1_score < self.player2_score:
            return "Игрок 2 выигрывает!"
        else:
            return "Ничья!"

    def play(self):
        """Основной игровой цикл"""
        while not self.is_game_over:
            self.display_board()
            self.display_scores()

            available_moves = self.get_available_moves()
            if not available_moves:
                print("Нет доступных ходов для текущего игрока. Ход переходит к сопернику.")
                self.current_player = 2 if self.current_player == 1 else 1
                continue

            print(f"Игрок {self.current_player}, ваш ход. Доступные ходы: {available_moves}")

            # Запрос ввода от игрока
            while True:
                try:
                    move = input("Введите номер строки и номер столбца (например, '0 1' для 1-й строки и 2-го столбца): ")
                    row, col = map(int, move.split())
                    if (row, col) in available_moves:
                        break
                    else:
                        print("Некорректный ход. Попробуйте снова.")
                except (ValueError, IndexError):
                    print("Некорректный ввод, попробуйте еще раз.")
            
            self.make_move(row, col)
            self.check_game_over()

        self.display_board()
        self.display_scores()
        print(self.determine_winner())


if __name__ == "__main__":
    game = MaxitGame()
    game.play()