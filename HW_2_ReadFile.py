def read_from_file():
    list_files_in_dir = ['1.txt', '2.txt', '3.txt']
    string_from_files = []
    for file in list_files_in_dir:
        with open(file, "r", encoding='utf-8') as f:
            tmp = []
            for line in f:
                tmp.append(line.strip())
            tmp.insert(0, str(len(tmp)))
            tmp.insert(0, file)
            string_from_files.append(tmp)
    string_from_files.sort(key=len)

    file = 'merge.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for string in string_from_files:
            for j in string:
                f.writelines(j + '\n')
    return
