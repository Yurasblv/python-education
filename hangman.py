"""Hangman game. Logic build by functions with using list of words.
To start file use command <python hangman.py>"""
import random

HANGMAN = (
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "    ----------\n"
    "    ",
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |    O\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "     |\n"
    "    ----------\n"
    "    ",
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |    O\n"
    "     |    |\n"
    "     | \n"
    "     |   \n"
    "     |    \n"
    "    ----------\n"
    "    ",
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |    O\n"
    "     |   /|\n"
    "     |   \n"
    "     |   \n"
    "     |   \n"
    "    ----------\n"
    "    ",
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |    O\n"
    "     |   /|\\\n"
    "     |   \n"
    "     |   \n"
    "     |     \n"
    "    ----------\n"
    "    ",
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |    O\n"
    "     |   /|\\\n"
    "     |   /\n"
    "     |   \n"
    "     |    \n"
    "    ----------\n"
    "    ",
    "\n"
    "     ------\n"
    "     |    |\n"
    "     |    O\n"
    "     |   /|\\\n"
    "     |   / \\\n"
    "     |   \n"
    "     |   \n"
    "    ----------\n"
    "    ",
)

WORDS = [
    "Театр",
    "Колонка",
    "Парфюмер",
    "Кант",
    "Хроника",
    "Зал",
    "Галера",
    "Мандарин",
    "Шоколад",
    "Пальто",
    "Метро",
    "Балл",
    "Вес",
    "Кафель",
    "Знак",
    "Фильтр",
    "Альбом",
    "Телесериал",
    "Cпрей",
    "Башня",
    "Кондитер",
    "Омар",
    "Подсолнух",
    "Закат",
    "Чан",
    "Пламя",
    "Тетерев",
    "Банк",
    "Муж",
    "Камбала",
    "Груз",
    "Кино",
    "Лаваш",
    "Калач",
    "Геолог",
    "Бальзам",
    "Бревно",
    "Жердь",
    "Борец",
    "Самовар",
    "Карабин",
    "Подлокотник",
    "Барак",
    "Мотор",
    "Шарж",
    "Сустав",
    "Амфитеатр",
    "Скворечник",
    "Подлодка",
    "Затычка,",
    "Ресница",
    "Спичка",
    "Кабан",
    "Муфта",
    "Синоптик",
    "Характер",
    "Мафиози",
    "Фундамент",
    "Бумажник",
    "Библиофил",
    "Дрожжи",
    "Казино",
    "Конечность",
    "Пробор",
    "Дуст",
    "Комбинация",
    "Мешковина",
    "Процессор",
    "Крышка",
    "Сфинкс",
    "Пассатижи",
    "Фунт",
    "Кружево",
    "Агитатор",
    "Формуляр",
    "Прокол",
    "Абзац",
    "Караван",
    "Леденец",
    "Кашпо",
    "Баркас",
    "Кардан",
    "Вращение",
    "Заливное",
    "Метрдотель",
    "Клавиатура",
    "Радиатор",
    "Сегмент",
    "Обещание",
    "Магнитофон",
    "Кордебалет",
    "Заварушка",
]


def get_word():
    """ Func to make game for game """
    word = random.choice(WORDS).lower()
    return word


def menu():
    """ Title of game """
    run = "Начать"
    all_used_words = "Посмотреть прошлые слова"
    close = "Выйти"
    print(f"Меню \n1.{run}\n2.{all_used_words}\n3.{close}")
    print("Введите число: ")
    try:
        p_choice = int(input())
        if p_choice == 1:
            hangman()
        elif p_choice == 2:
            with open("used_words.txt", "r", encoding='utf-8') as used_words:
                print(used_words.read())
        elif p_choice == 3:
            pass
    except ValueError as error:
        print(error, "Введи число: 1,2 или 3")


def helpers():
    """ Hints for playing """
    print(
        "Подсказки:"
        "\nНачинайте угадывать буквы с наиболее часто встречающихся: "
        "о е а и н т с р в л к м д п у я ы ь г з б ч й х ж ш ю ц щ э ф ъ ё."
        "\nКроме того, начав с гласных (о е а...), лучше переключиться на согласные, "
        "потому что именно по ним слово угадывается легче."
    )


def hangman():
    """Main functionality of program"""
    helpers()
    max_wrong = len(HANGMAN)
    word = get_word()
    secret = "_" * len(word)
    wrong = 0
    used = []

    game_cycle(max_wrong, word, secret, wrong, used)

    if wrong == max_wrong:
        print(f"\nТы повешен =(\nЗагаданное слово было: {word}")
    else:
        with open("used_words.txt", "a", encoding="utf-8") as used_words:
            used_words.write(f"{word.capitalize()}\n")
        print("\nТы победил =)")


def game_cycle(max_wrong, word, secret, wrong, used):
    """Func with cycle of guessed letters"""
    while max_wrong > wrong and word != secret:

        lives = max_wrong - wrong
        print(HANGMAN[wrong], f"Жизней осталось: {lives}\n"
                              f"Были использованы: {used}\n"
                              f"{secret} ({len(secret)} букв)")
        guess = input("\nБуква: ").lower()

        if guess in used:
            print(f"Буква {guess} уже отгадана")
            guess = input("Введите своё предположение: ").lower()

        used.append(guess)

        if guess in word:
            print(f"{guess} есть в слове!")
            new = str()
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += secret[i]
            secret = new

        else:
            print(f"Буквы {guess} в слове нет")
            wrong += 1


if __name__ == "__main__":
    menu()
