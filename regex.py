import re
import csv

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data


def remove_line_containing(input_content, argument):
    split_argument = argument.split('|')
    for single_argument in split_argument:
        input_content = re.sub(r'.*?'+single_argument + '.*\n', '', input_content)
    return input_content


def write_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

def save_delimiter(get_delimiter,input_data):
    # print(input_data)
    csv.register_dialect('myDialect',delimiter=',',quoting=csv.QUOTE_ALL,skipinitialspace=True)

    with open('data.csv','w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile,dialect='myDialect')
        for row in input_data.split(sep='\n'):
            row=row.split(sep=" ")
            print("abhihfsbab:: %s"%row)
            writer.writerow(row)
    csvfile.close()





if __name__ == '__main__':
    data_updated = []
    input_filepath = 'readme_elasticsearch.txt'  # input('Path to input file:\t')
    input_data = read_file(input_filepath)
    argument = 'market|helllo'
    # print(input_data)
    input_data = remove_line_containing(input_data, argument)
    write_file(input_filepath, input_data)
    print(input_data)
    # print(re.sub(r'.*?market.*\n', '', input_data))
    save_delimiter(' ',input_data)
    # for line in remove_data:
    #     data=regex_operation(data,line)
    # print(data)
    # write_file('data.txt',data)
