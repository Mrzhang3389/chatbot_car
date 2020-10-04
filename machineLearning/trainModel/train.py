import os
from .generatorVocabulary import GenVocab
from sklearn.naive_bayes import GaussianNB


class Trainer():
    def __init__(self, train_data_path):
        self.train_data_path_list = list(map(lambda x: os.path.join(train_data_path, x), os.listdir(train_data_path)))
        self.vocab_path = "./vocabulary.txt"

    def load_data(self):
        vocab_dict = self.load_vocab_dict()

    def load_vocab_dict(self):
        '''加载vocab词典'''
        dic = {}
        with open(self.vocab_path, "r") as file:
            for index, word in enumerate(file.readlines()):
                dic[word.strip()] = index
        return dic

    def train_model(self):
        pass

    def test_model(self):
        pass

    def save_model(self):
        pass

    def load_model(self):
        pass


if __name__ == '__main__':
    # gv = GenVocab("./trainData", "./vocabulary.txt")
    # gv.run()  # 生成训练数据的 词典
    train = Trainer("./trainData")