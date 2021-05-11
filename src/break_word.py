import csv
import os
import argparse


def write_to_file(i, words, which_book):
    with open(
        f"..\\data\\word_broken\\{which_book}\\{i}.csv", "w", encoding="utf-8"
    ) as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerows(words)


def break_masnavi():
    if not os.path.exists("../data/word_broken"):
        os.mkdir("../data/word_broken")
    if not os.path.exists("../data/word_broken/masnavi"):
        os.mkdir("../data/word_broken/masnavi")
    if not os.path.exists("../data/word_broken/masnavi/daftar-aval"):
        os.mkdir("../data/word_broken/masnavi/daftar-aval")
    if not os.path.exists("../data/word_broken/masnavi/daftar-dovom"):
        os.mkdir("../data/word_broken/masnavi/daftar-dovom")

    for i in range(1, 173):
        words = []
        with open(
            f"..\\data\\raw\\masnavi\\daftar-aval\\{i}.csv", "r", encoding="utf-8"
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            row_num = 0
            for b in csv_reader:
                if len(b) == 0 or row_num == 0:
                    row_num += 1
                    continue
                words.append(b[0].split(" "))
                if b[1] != "":
                    words.append(b[1].split(" "))
        write_to_file(i, words, "masnavi\\daftar-aval")


def break_divan_shams():
    if not os.path.exists("../data/word_broken"):
        os.mkdir("../data/word_broken")
    if not os.path.exists("../data/word_broken/divan_shams"):
        os.mkdir("../data/word_broken/divan_shams")

    for i in range(1, 306):
        words = []
        with open(
            f"..\\data\\raw\\divan_shams\\{i}.csv", "r", encoding="utf-8"
        ) as csvfile:
            csv_reader = csv.reader(csvfile)
            row_num = 0
            for b in csv_reader:
                if len(b) == 0 or row_num == 0:
                    row_num += 1
                    continue
                words.append(b[0].split(" "))
                if b[1] != "":
                    words.append(b[1].split(" "))
        write_to_file(i, words, "divan_shams")


def main():
    break_masnavi()
    break_divan_shams()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", action="store_true")
    parser.add_argument("-s", action="store_true")
    args = parser.parse_args()

    if args.m:
        break_masnavi()
    elif args.s:
        break_divan_shams()
    else:
        main()
