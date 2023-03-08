def read_file():
    file = open('recipes.txt', 'r')
    data = {}
    for line in file:
        data[line.strip()] = []
        count = file.readline().strip()
        for i in line:
            ing, me, qua = file.readline().strip().split(' | ')
            data[line.strip()].append('ing': ing, 'me': me, 'qua': qua)
        file.readline()
    file.close()
    return data
  
pprint(read_file(), sirt_dicts = False)
