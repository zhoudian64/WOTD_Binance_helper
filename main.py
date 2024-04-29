import sys
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('wordnet')

def load_text(filename):
    """加载文本文件，并返回内容"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def filter_words(words, word_length, forbidden_letters, required_letters):
    """过滤单词列表，根据给定的长度、禁止字母和必须包含的字母"""
    lemmatizer = WordNetLemmatizer()
    filtered_words = set()
    for word in words:
        lemmatized_word = lemmatizer.lemmatize(word.lower())
        if (len(lemmatized_word) == word_length and
            (not required_letters or all(char in lemmatized_word for char in required_letters)) and
            (not forbidden_letters or not any(char in lemmatized_word for char in forbidden_letters))):
            filtered_words.add(lemmatized_word)
    return filtered_words

if __name__ == "__main__":
    # 接收命令行参数
    if len(sys.argv) < 3:
        print("Usage: python main.py <filename> <word_length> [<forbidden_letters> <required_letters>]")
        sys.exit(1)

    filename = sys.argv[1]
    word_length = int(sys.argv[2])
    forbidden_letters = sys.argv[3] if len(sys.argv) > 3 else ""
    required_letters = sys.argv[4] if len(sys.argv) > 4 else ""

    # 加载文本并分词
    text = load_text(filename)
    words = set(word_tokenize(text))

    # 过滤单词列表
    result = filter_words(words, word_length, forbidden_letters, required_letters)

    # 打印结果
    print("Filtered Words:")
    for word in sorted(result):
        print(word)