from pathlib import Path

def write_file(file_name, file_content):
    convert_to_string = str(file_name)
    f_name = Path(convert_to_string+".txt")
    with open(f_name, encoding="UTF 8", mode="w") as new_file:
        new_file.write(file_content)

def append_file(file_name, append_content):
    convert_to_str = str(file_name)
    f_name = Path(convert_to_str+'.txt')
    with open(f_name, encoding="UTF 8", mode="a") as append_file:
        append_file.write(append_content)



def read_file(file_name):
    convert_to_str= str(file_name)
    f_name = Path(convert_to_str+".txt")
    with open(f_name, encoding="UTF 8") as read_file:
        content = read_file.read()
        return content
