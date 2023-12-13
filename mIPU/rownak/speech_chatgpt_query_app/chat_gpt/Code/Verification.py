def binary_file_to_text(file_path):
    with open(file_path, 'rb') as file:
        binary_content = file.read()
    return binary_content.decode('utf-8')

QueryFile = r"/home/lab518/DATA/Query.bin"
ResponseFile = r"/home/lab518/DATA/Response.bin"

Query = binary_file_to_text(QueryFile)
Response = binary_file_to_text(ResponseFile)

print("Query:")
print(Query)
print("Response:")
print(Response)