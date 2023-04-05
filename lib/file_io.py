def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w') as log_file:
        log_file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as log_file:
        log_file.write(append_content)

def read_file(file_name):
    return  open(f'{file_name}.txt').read()
