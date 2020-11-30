
def read_data_file(filename, method='lines'):
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

            return data

    except Exception as err:
        print('ERROR reading file', filename)
        print(err)

# print(data_file('day01/input.txt', 'comma'))
