from sentence_detail import Sentence
from src.loader import BOOK_LOADER_DICT
from src.translator import MODEL_DICT


def read_data():
    with open('english_chinese.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()
    num = 1
    odd_lines = []
    even_lines = []
    for line in lines:
        if (num % 2) == 0:
            even_lines.append(line.strip())
        else:
            odd_lines.append(line.strip())
        num += 1

    assert len(odd_lines) == len(even_lines), '数据文件格式不对'

    data_list = []
    for index in range(len(odd_lines)):
        sentence = Sentence(odd_lines[index], even_lines[index])
        data_list.append(sentence)

    return data_list


def translate(data_list, translator):
    for data in data_list:
        data.translate(translator)


def main():
    # 读取数据
    data_list = read_data()
    # 翻译每个不常用的词语
    translator = MODEL_DICT.get('caiyun')
    t = translator('key', 'zh')
    translate(data_list, t)
    # 生成文档
    book_loader = BOOK_LOADER_DICT.get('pdf')
    b = book_loader("100_sentences_detail.pdf")
    b.make_book(data_list)


if __name__ == '__main__':
    main()
