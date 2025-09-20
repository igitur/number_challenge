from number_extractor import NumberExtractor
from wordifyer import number_to_words

if __name__ == "__main__":
    extractor = NumberExtractor()

    for possible_number in extractor.extract_numbers():
        word_representation = number_to_words(possible_number)
        print(word_representation)
