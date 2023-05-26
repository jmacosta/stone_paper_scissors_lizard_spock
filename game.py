import random
import os

# CONSTANTS
STONE = 1
SCISSORS = 2
PAPER = 3
EXIT = 0


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
        clear_screen()
        print("""
               Make your move, 
                            1.- Stone
                            2.- Paper
                            3.- Scisors
                            h.- Help
                            0.- Exit
               """)
        user_choice = input('Please select an option: ')
        if is_number(user_choice):
            if int(user_choice) >= 0 and int(user_choice) < 4:
                result = int(user_choice)
                break
        else:
            if user_choice.lower() == 'h':
                show_help()
    return result


def is_exit(user_choice):
    """
    predicado que devuelve True si el usuario quiere salir y False si quiere seguir Jugando
    """
    return int(user_choice) == EXIT


def generate_computer_choice():
    """
    Genera y devuelve una jugada aleatoria del ordenador
    """
    return random.randint(1, 3)


def evaluate_move(user_choice, comp_choice):
    """
    Evalua las jugadas del usuario y el ordenador y devuelve un texto con el resultado
    """
    winner = None
    if user_choice == STONE:
        if comp_choice == SCISSORS:
            winner = 'User wins'
        elif comp_choice == PAPER:
            winner = 'Computer wins'
        else:
            winner = 'User and Computer draws'
    if user_choice == SCISSORS:
        if comp_choice == PAPER:
            winner = 'User wins'
        elif comp_choice == STONE:
            winner = 'Computer wins'
        else:
            winner = 'User and Computer draws'
    if user_choice == PAPER:
        if comp_choice == STONE:
            winner = 'User wins'
        elif comp_choice == SCISSORS:
            winner = 'Computer wins'
        else:
            winner = 'User and Computer draws'

    return winner


def print_result(result):
    """
    Muestra en pantalla el resultado de la jugada entre usuario y ordenador
    """
    print(result)
    input('Press any key to continue...')

    return None


def show_help():
    """
    Muestra en pantalla información de ayuda
    """
    # muestra en pantalla ayuda acerca de las jugadas y quien gana a quien
    print("to do ayuda ")
    return None


def clear_screen():
    os.system('clear')
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


if __name__ == "__main__":
    game_loop()
