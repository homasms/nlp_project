import csv
import argparse
import math
from os import device_encoding
import matplotlib.pyplot as plt


def number_of_beits():
    num_of_beits = 0
    for i in range(1, 173):
        with open(
            f"..\\data\\raw\\masnavi\\daftar-aval\\{i}.csv", "r", encoding="utf-8"
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            num_of_beits += int(sum(1 for r in csv_reader) / 2) - 1

    # for i in range (1,116):
    #   with open(f"..\\data\\raw\\masnavi\\daftar-dovom\\{i}.csv", 'r', encoding="utf-8") as csvfile:
    #      csv_reader = csv.reader(csvfile)
    # num_of_beits += int(sum(1 for r in csv_reader)/2) - 1

    print(f"number of beits in masnavi is: {num_of_beits}")

    num_of_beits = 0
    for i in range(1, 306):
        with open(
            f"..\\data\\raw\\divan_shams\\{i}.csv", "r", encoding="utf-8"
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            num_of_beits += int(sum(1 for r in csv_reader) / 2) - 1
    print(f"number of beits in divan-e shams is: {num_of_beits}\n")


def number_of_words():
    # masnavi
    masnavi_words = []
    for i in range(1, 173):
        with open(
            f"..\\data\\word_broken\\masnavi\\daftar-aval\\{i}.csv",
            "r",
            encoding="utf-8",
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for word in row:
                    masnavi_words.append(word)

    # divan-e shams
    shams_words = []
    for i in range(1, 306):
        with open(
            f"..\\data\\word_broken\\divan_shams\\{i}.csv", "r", encoding="utf-8"
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                for word in row:
                    shams_words.append(word)

    # for i in range (1,116):
    #    with open(f"..\\data\\word_broken\\masnavi\\daftar-dovom\\{i}.csv", 'r', encoding="utf-8") as csvfile:
    #       csv_reader = csv.reader(csvfile)
    # num_of_words += sum(len(row) for row in csv_reader)
    print(f"number of words in masnavi is: {len(masnavi_words)}")
    print(f"number of words in divan-e shams is: {len(shams_words)}\n")
    return masnavi_words, shams_words


def unique_words():
    # masnavi
    masnavi_words, shams_words = number_of_words()
    unique_set_masnavi = set(masnavi_words)
    unique_set_shams = set(shams_words)
    print(f"number of unique words of masnavi is: {len(unique_set_masnavi)}")

    print(f"number of unique words of divan-e shams is: {len(unique_set_shams)}")
    return unique_set_masnavi, unique_set_shams


def common_words():
    words_masnavi, words_shams = unique_words()
    commons = words_masnavi.intersection(words_shams)
    in_masnavi = list(words_masnavi - words_shams)
    in_shams = list(words_shams - words_masnavi)

    print(f"number of common of words is: {len(commons)}")
    print(
        f"number of unqiue words in masnavi those are not in divan-e shams: {len(in_masnavi)}"
    )
    print(
        f"number of unique words in divan-e shams those are not in masnavi: {len(in_shams)}"
    )
    return commons, in_masnavi, in_shams


def repetitive_words():
    masnavi_words, shams_words = number_of_words()
    commons = set(masnavi_words).intersection(set(shams_words))

    word_count_masnavi = {}
    for word in masnavi_words:
        if word in commons or word in word_count_masnavi.keys():
            continue
        word_count_masnavi[word] = masnavi_words.count(word)

    word_count_shams = {}
    for word in shams_words:
        if word in commons or word in word_count_shams.keys():
            continue
        word_count_shams[word] = shams_words.count(word)

    word_list_masnavi = sorted(
        word_count_masnavi, key=word_count_masnavi.get, reverse=True
    )
    word_list_shams = sorted(word_count_shams, key=word_count_shams.get, reverse=True)

    with open("most-common.txt", "a", encoding="utf-8") as file:
        csv_writer = csv.writer(file)

        csv_writer.writerow(word_list_masnavi[0:9])
        csv_writer.writerow(word_list_shams[0:9])
    print("the most repetitive words are saved in most_common.txt file.")
    return word_count_masnavi, word_count_shams


def relative_normalize_frequency():
    masnavi_words, shams_words = number_of_words()
    masnavi_num_of_words = len(masnavi_words)
    shams_num_of_words = len(shams_words)
    commons = set(masnavi_words).intersection(set(shams_words))
    word_count_masnavi = {word: masnavi_words.count(word) for word in commons}
    word_count_shams = {word: shams_words.count(word) for word in commons}

    masnavi_RNF = {
        word: (word_count_masnavi[word] * shams_num_of_words)
        / (masnavi_num_of_words * word_count_shams[word])
        for word in commons
    }

    shams_RNF = {
        word: (word_count_shams[word] * masnavi_num_of_words)
        / (shams_num_of_words * word_count_masnavi[word])
        for word in commons
    }

    sorted_masnavi_RNF = sorted(masnavi_RNF, key=masnavi_RNF.get, reverse=True)
    sorted_shams_RNF = sorted(shams_RNF, key=shams_RNF.get, reverse=True)

    with open("RNF.txt", "a", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(sorted_masnavi_RNF[0:9])
        csv_writer.writerow(sorted_shams_RNF[0:9])

    print("words added to RNF.txt file in current directory.")
    return masnavi_RNF, shams_RNF


def tf_idf():
    masnavi_words, shams_words = number_of_words()
    masnavi_num_of_words = len(masnavi_words)
    shams_num_of_words = len(shams_words)
    tf_idf_masnavi = {
        word: 0
        if word in shams_words
        else (math.log(2) * masnavi_words.count(word)) / masnavi_num_of_words
        for word in masnavi_words
    }
    tf_idf_shams = {
        word: 0
        if word in masnavi_words
        else (math.log(2) * shams_words.count(word)) / shams_num_of_words
        for word in shams_words
    }

    sorted_masnavi = sorted(tf_idf_masnavi, key=tf_idf_masnavi.get, reverse=True)
    sorted_shams = sorted(tf_idf_shams, key=tf_idf_shams.get, reverse=True)

    with open("tf_idf.txt", "a", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(sorted_masnavi[0:9])
        csv_writer.writerow(sorted_shams[0:9])

    print(
        "words with the most tf_idf score added to tf_idf.txt file in current directory."
    )
    return tf_idf_masnavi, tf_idf_shams


def histogram():
    masnavi_words, shams_words = number_of_words()
    # masnavi_num_of_words = len(masnavi_words)
    # shams_num_of_words = len(shams_words)
    # commons = set(masnavi_words).intersection(set(shams_words))
    word_count_masnavi = {word: masnavi_words.count(word) for word in masnavi_words}
    word_count_shams = {word: shams_words.count(word) for word in shams_words}

    sorted_masnavi = sorted(
        word_count_masnavi, key=word_count_masnavi.get, reverse=True
    )[0:100]
    sorted_shams = sorted(word_count_shams, key=word_count_shams.get, reverse=True)[
        0:100
    ]

    counts_masnavi = [word_count_masnavi[word] for word in sorted_masnavi]
    counts_shams = [word_count_shams[word] for word in sorted_shams]

    with open("histogram.txt", "a", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(sorted_masnavi)
        csv_writer.writerow(sorted_shams)
    # plt.hist(masnavi_words, bins=100)

    for i in range(0, 100):
        plt.plot(i, counts_masnavi[i], "bs")
    plt.show()

    for i in range(0, 100):
        plt.plot(i, counts_shams[i], "bs")
    plt.show()


def main():
    number_of_beits()
    number_of_words()
    unique_words()
    common_words()
    repetitive_words()
    relative_normalize_frequency()
    tf_idf()
    histogram()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", action="store_true")
    parser.add_argument("-w", action="store_true")
    parser.add_argument("-u", action="store_true")
    parser.add_argument("-c", action="store_true")
    parser.add_argument("-r", action="store_true")
    parser.add_argument("-rnf", action="store_true")
    parser.add_argument("-tf", action="store_true")
    parser.add_argument("-hist", action="store_true")
    args = parser.parse_args()

    if args.b:
        number_of_beits()
    elif args.w:
        number_of_words()
    elif args.u:
        unique_words()
    elif args.c:
        common_words()
    elif args.r:
        repetitive_words()
    elif args.rnf:
        relative_normalize_frequency()
    elif args.tf:
        tf_idf()
    elif args.hist:
        histogram()
    else:
        main()
