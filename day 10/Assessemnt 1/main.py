def file_extension(file_name):
    path = file_name[::-1]
    for i in range(len(path)):
        if(path[i]=='.'):
            return path[0:i]
    raise Exception("Invalid file name")

    