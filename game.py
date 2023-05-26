import random
from enum import Enum


class Move(Enum):
    STONE = 1
    PAPER = 2
    SCISORS = 3


def game_loop():
    """
        Arranca el bucle principal del juego
    """
    while True:
        # Leo la selección del usuario(piedra, papel, tijeras o parar el juego)
        user_choice = read_user_choice()
        # Siempre y cuando no quiera parar
        if not is_exit(user_choice):
            # genero una jugada del ordenador
            comp_choice = generate_computer_choice()
            # evaluo la jugada
            result = evaluate_move(user_choice, comp_choice)
            # muestro el ganador en pantalla y vuelta al principio
            print_result(result)
        else:
            # el humano es un gallina: Salgo
            break


def read_user_choice():
    """
    recibe la entrada del usuario(piedra, papel, tijera, salir)
    """
    result = None
    while True:
        user_choice = input("""Make your move, 
                            1.- Stone
                            2.- Paper
                            3.- Scisors
                            h.- Help
                            0.- Exit
                                                        
                            Please select an option: 
                            """)
        if is_number(user_choice):
            if int(user_choice) >= 0 and int(user_choice) < 4:
                result = translate_move(user_choice)
                break
        else:
            if user_choice.lower() == 'h':
                show_help()
    return result


def is_exit(user_choice):
    """
    predicado que devuelve True si el usuario quiere salir y False si quiere seguir Jugando
    """
    result = False
    if user_choice == 0:
        result = True
    return result


def generate_computer_choice():
    """
    Genera y devuelve una jugada aleatoria del ordenador
    """
    return translate_move(random.randint(1, 3))


def evaluate_move(user_choice, comp_choice):
    """
    Evalua las jugadas del usuario y el ordenador y devuelve un texto con el resultado
    """
    winner = None
    if user_choice == Move.STONE:
        if comp_choice == Move.SCISORS:
            winner = 'User wins'
        elif comp_choice == Move.PAPER:
            winner = 'Computer wins'
        else:
            winner = 'User and Computer draws'
    if user_choice == Move.SCISORS:
        if comp_choice == Move.PAPER:
            winner = 'User wins'
        elif comp_choice == Move.STONE:
            winner = 'Computer wins'
        else:
            winner = 'User and Computer draws'
    if user_choice == Move.PAPER:
        if comp_choice == Move.STONE:
            winner = 'User wins'
        elif comp_choice == Move.SCISORS:
            winner = 'Computer wins'
        else:
            winner = 'User and Computer draws'

    return winner


def print_result(result):
    """
    Muestra en pantalla el resultado de la jugada entre usuario y ordenador
    """
    print(result)
    return None


def show_help():
    """
    Muestra en pantalla información de ayuda
    """
    # muestra en pantalla ayuda acerca de las jugadas y quien gana a quien
    print("to do ayuda ")
    return None


def is_number(user_choice):
    """
    Comprueba si lo que recibe se puede convertir en numero o no
    """
    result = False
    try:
        int(user_choice)
        result = True
    except:
        result = False
    return result


def translate_move(move):
    """
    REcibe un int y devuelve un elemento de Enum con la jugada
    """
    if move == 1:
        result = Move.STONE
    elif move == 2:
        result = Move.SCISORS
    else:
        result = Move.PAPER

    return result


if __name__ == "__main__":
    game_loop()
