
def read_data_file(filename, method='lines', convert=None):
    try:
        with open(filename, encoding = 'utf-8') as f:
            data = []
            for line in f:
                line = line.split('\n')[0]
                if (method == 'lines'):
                    data.append(line)
                elif (method == 'comma'):
                    data.append(line.split(','))
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

    except Exception as err:
        print('ERROR reading file', filename)
        print(err)
