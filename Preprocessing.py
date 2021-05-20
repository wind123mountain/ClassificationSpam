import os
import re
from gensim.parsing.preprocessing import (
    strip_multiple_whitespaces,
    strip_numeric,
    strip_punctuation,
    strip_short,
    strip_tags,
    stem_text,
    remove_stopwords,
    preprocess_string
)
from email.parser import Parser


def strip_html_symbols(message):
    html_symbols = [
        '&nbsp;',
    ]
    for symbol in html_symbols:
        message = re.sub(symbol, ' ', message)
    return message


def strip_url(message):
    return re.sub(r'http\S+', ' ', message)


def strip_email_address(message):
    return re.sub(r'\S+@\S+', ' ', message)


def strip_email_header(message):
    message = Parser().parsestr(message)
    subject = message.get('subject', '')
    body = get_email_body(message)

    return '\n'.join((subject, body))


def get_email_body(message):
    payloads = message.get_payload()
    if isinstance(payloads, list):
        return '\n'.join([get_email_body(message) for message in payloads])
    elif isinstance(payloads, str):
        return payloads


def data_preprocessing(raw_message):
    FILTERS = [
        strip_email_header,
        str.lower,
        strip_html_symbols,
        strip_tags,
        strip_url,
        strip_email_address,
        strip_punctuation,
        strip_numeric,
        strip_multiple_whitespaces,
        strip_short,
        remove_stopwords,
        stem_text,
    ]

    tokens = preprocess_string(raw_message, filters=FILTERS)
    return ' '.join(tokens)

def read_process_data(folders_list):
    result = []
    for folder in folders_list:
        files_path = sorted([os.path.join(folder, file_name) for file_name in os.listdir(folder)])

        for file_path in files_path:
            with open(file_path, 'r', encoding='latin') as fi:
                mail = data_preprocessing(fi.read())
                result.append(mail)

    return result

def load_dataset(data_preprocessed=False):
    if data_preprocessed:
        # load processed data
        with open('./data_processed/SpamAssassin/easy_ham.txt', 'r', encoding='utf-8') as fi:
            easy_ham = fi.readlines()
        with open('./data_processed/SpamAssassin/spam.txt', 'r', encoding='utf-8') as fi:
            spam = fi.readlines()
    else:
        # load not processed data
        easy_ham_folders = [
            './dataset/SpamAssassin/easy_ham/20021010_easy_ham',
            './dataset/SpamAssassin/easy_ham/20030228_easy_ham',
            './dataset/SpamAssassin/easy_ham/20030228_easy_ham_2',
        ]
        
        spam_folders = [
            './dataset/SpamAssassin/spam/20021010_spam',
            './dataset/SpamAssassin/spam/20030228_spam',
            './dataset/SpamAssassin/spam/20030228_spam_2',
            './dataset/SpamAssassin/spam/20050311_spam_2',
        ]
        easy_ham = read_process_data(easy_ham_folders)
        spam = read_process_data(spam_folders)

    return (easy_ham, spam)