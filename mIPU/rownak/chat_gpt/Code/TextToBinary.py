def save_text_to_binary_file(text, file_path):
    with open(file_path, 'wb') as file:
        file.write(text.encode('utf-8'))

print("Please enter your query:")
Text_query = input()
binary_file_path = r"/home/lab518/DATA/Query.bin"
save_text_to_binary_file(Text_query, binary_file_path)
