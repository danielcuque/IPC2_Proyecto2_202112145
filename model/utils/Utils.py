import inquirer

def get_file() -> str:
    path_file = input("Introduzca la ruta del fichero: ")
    return path_file


def ask_yes_no(message: str) -> bool:
    questions = [
        inquirer.List('menu',
                      message=message,
                      choices=["1. Si",
                               "2. No"])]
    answer = inquirer.prompt(questions=questions)
    if answer is not None:
        if answer['menu'] == "1. Si":
            return True
        elif answer['menu'] == "2. No":
            return False
    return False
