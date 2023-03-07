def read_file():
    file = open('recipes.txt', 'r')
    data = []
    for line in file:
      data.append(line.strip())
    file.close()
    # while True:
    #     line = file.readline().strip()
    #     data.append(file.readline().strip())
    # # Если конец файла
    #     if not line:
    #         break  
    return data
  
pprint(read_file())
