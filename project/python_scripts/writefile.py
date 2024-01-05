def writefile(data: list):
    link = 'project/data/data.txt'
    with open('project/data/data.txt', 'w') as file:
        for element in file:
            file.write(element)
            file.write('\n')

    return link