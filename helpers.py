
def read_data_file(filename, method='lines', splitStr=None, convert=None):
    with open(filename, encoding = 'utf-8') as f:
        data = []
        for line in f:
            line = line.split('\n')[0]
            if (method == 'lines'):
                if type(splitStr) is str:
                    data.append(list(line.split(splitStr)))
                else:
                    data.append(line)
            elif (method == 'comma'):
                data.append(line.split(','))
            elif (method == 'char'):
                data.append([char for char in line])
            else:
                raise ValueError('Invalid parse method')

        if (convert):
            if (type(data[0]) is str):
                data = list(map(convert, data))
            elif(type(data[0]) is list):
                for i in range(len(data)):
                    if (callable(convert)):
                        data[i] = list(map(convert, data[i]))
                    elif(type(convert) is list):
                        for j in range(len(convert)):
                            data[i][j] = convert[j](data[i][j])
        
        return data
