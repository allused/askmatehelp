import csv
import os

answers_header = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
question_header = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']

ANSWER_DATA_FILE_PATH = os.getenv('ANSWER_DATA_FILE_PATH') if 'ANSWER_DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
QUESTION_DATA_FILE_PATH = os.getenv('QUESTION_DATA_FILE_PATH') if 'QUESTION_DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'

answer_file_path = 'sample_data/answer.csv'
question_file_path = 'sample_data/question.csv'


ANSWER_CSV_LENGTH = sum(1 for row in csv.reader('sample_data/data.csv'))
QUESTION_CSV_LENGTH = sum(1 for row in csv.reader('sample_data/data.csv'))


TEMPLATE_HEADER = ['TITLE', 'DATE', 'VIEWS', 'VOTES']


def read_elements_csv(path, header):
    temp_lst = []
    with open(path) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dictionary = {key: value for key, value in zip(header, row)}
            temp_lst.append(dictionary)
        return temp_lst


def add_element_csv(path, row, csv_length, filepath):
    print(csv_length)
    temp_lst = insert_element_csv(row, csv_length, path)

    with open(filepath, 'w') as file:
        csv_writer = csv.writer(file)
        for line in temp_lst:
            csv_writer.writerow(line.values())


def insert_element_csv(path, row, index, csv_length):
    temp_lst = read_elements_csv(path)
    zip_row = zip(temp_lst[0].keys(), row)
    dict_row = dict((key, value) for key, value in zip_row)
    print(dict_row)
    if index == csv_length:
        temp_lst.append(dict_row)
    else:
        temp_lst[index] = dict_row
    return temp_lst


def get_id(path):
    return len(read_elements_csv(path))


def get_element_by_id(path, user_id, header):
    for elt in read_elements_csv(path, header):
        if elt['id'] == str(user_id):
            return elt

def find_ids(dict_list, target_id):
    for dict in dict_list:
        if dict['id'] == target_id:
            return dict

print(find_ids(read_elements_csv(answer_file_path, question_header), 1))
