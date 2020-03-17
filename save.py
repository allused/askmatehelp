@app.route('/answers')
def answers(question_id=1):
    questions = data_handler.read_elements_csv(QUESTION_DATA_FILE_PATH, question_header)
    question_dict = data_handler.find_ids(questions, question_id)
    answers = data_handler.read_elements_csv(ANSWER_DATA_FILE_PATH, answers_header)
    return render_template('answers.html', question=question_dict, answers=answers, )

def find_ids(dict_list, target_id):
    for dict in dict_list:
        if dict['id'] == target_id:
            return dict