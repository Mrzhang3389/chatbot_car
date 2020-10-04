import os
import jieba


class GenVocab():
    '''用于生成训练模型的词典数据'''
    def __init__(self, train_data_path, save_vocab_path):
        self.train_data_path_list = list(map(lambda x: os.path.join(train_data_path, x), os.listdir(train_data_path)))
        self.save_vocab_path = save_vocab_path
        print(self.train_data_path_list)

    def get_word(self, str):
        seg_list = jieba.cut(str)
        seg_list = list(seg_list)
        return seg_list

    def open_file(self, file_path):
        with open(file_path, "r") as file:
            for line in file.readlines():
                word_list = self.get_word(line.strip())
        return word_list

    def run(self):
        result_word = []
        for file_path in self.train_data_path_list:
            word_list = self.open_file(file_path)
            result_word.extend(word_list)
        result_word = set(result_word)
        self.write_file(result_word)
        print("write word dict success...")

    def write_file(self, word_list):
        with open(self.save_vocab_path, "w") as file:
            for item in word_list:
                file.write(item + "\n")


if __name__ == '__main__':
    gv = GenVocab("./trainData", "./vocabulary.txt")
    gv.run()
