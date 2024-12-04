file_path = "todos.txt"

def get_todos(path = file_path):
    """read a file"""
    with open(path, "r") as file:
        task = file.readlines()
    return task

def write_todos(todos_local,path = file_path):
    """write in a file"""
    with open(path, "w") as file:
        file.writelines(todos_local)