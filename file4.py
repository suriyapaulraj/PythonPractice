file = open("sample.txt", "a")

content= file.write("the file has been appended")

print(content)

file.close()