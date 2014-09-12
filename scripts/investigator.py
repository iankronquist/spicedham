from __future__ import division
import oursql
import subprocess
#from spicedham import splittokenizer
import os

DB_NAME = 'fjord'
DUMP_NAME = 'dump.sql'

def triage_responses():
    connection = oursql.connect(db=DB_NAME, host='127.0.0.1', user='root', passwd='password')
    cursor = connection.cursor()
    falseNeg = cursor.execute('''
        select description
        from feedback_response
        join flags_flag_responses
            on feedback_response.id = flags_flag_responses.response_id
        join flags_flag
            on flags_flag_responses.flag_id = flags_flag.id
        where flags_flag.name = "abuse-wrong";
        ''')
    sort_results(cursor.fetchall())

def sort_results(query_result):
    for id, description in query_result:
        sorted_data = {'low_p': [], 'high_p': []}
        for word in tokenize(description):
            data = cursor.execute('select value from flags_store where key=? and classifier=Bayes', (word,)).fetchone()
            raw_data = json.loads(data)
            if raw_data['spam'] / raw_data['total'] >= 0.5:
                sorted_data['high_p'].append((word, raw_data))
            else:
                sorted_data['low_p'].append((word, raw_data))
        print description[:20], sorted_data
        

# TODO: Just use spicedham's tokenizer once that gets merged, this is just
# a copy pasta
def tokenize(text):
    text = split('[ ,.?!\n\r]', text)
    text = [token.lower() for token in text if token]
    return text
            

def reconstitute_freeze_dried_db():
    os.system('mysql < ', DUMP_NAME)

if __name__ == '__main__':
    triage_responses()
