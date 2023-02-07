def remove_quotes(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    content = content.replace('"', '')

    with open(file_path, "w") as file:
        file.write(content)

file_path = "<file_path>.txt" # specify the file path here
remove_quotes(file_path)
