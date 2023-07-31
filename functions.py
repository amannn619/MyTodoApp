def count(phrase):
    return phrase.count('.')

def getTodos(filepath = "todos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos
    
def writeTodos(todos, filepath = "todos.txt"):
    with open(filepath, "w") as file:
            file.writelines(todos)

    