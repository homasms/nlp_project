from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import csv
import os
import argparse

# def delete_half_space(poem):
#    if '\u200c' in poem:
#        poem.replace('\u200c', ' ')
#    return poem


def addToFile(num, poem, which_book):
    try:
        with open(f"..\\data\\raw\\{which_book}\\{num}.csv", "a", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile,
                                    delimiter=",",
                                    quotechar='"',
                                    quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerows(poem)
            #csvfile.write("%s\n" % (poem))
        #print([0])

    except IOError:
        pass


def extract_poem(title, elements_m1, elements_m2):
    poem = []
    poem.append([title, ""])
    for element, e in zip(elements_m1, elements_m2):
        poem.append([element.text, e.text])
        #poem.append(str(e.text))
    return poem


def divan_shams():
    if not os.path.exists("../data/raw"):
        os.mkdir("../data/raw")
    if not os.path.exists("../data/raw/divan_shams"):
        os.mkdir("../data/raw/divan_shams")

    opts = Options()
    opts.set_headless()
    for i in range(1, 306):
        print(i)
        driver = Chrome(executable_path="e:/chromedriver89", options=opts)
        driver.get(f"https://ganjoor.net/moulavi/shams/ghazalsh/sh{i}/")
        try:
            header = driver.find_element_by_tag_name('h2').text
            elements_m1 = driver.find_elements_by_class_name("m1")
            elements_m2 = driver.find_elements_by_class_name("m2")
            poem = extract_poem(header, elements_m1, elements_m2)
            addToFile(i, poem, "divan_shams")
        except (NoSuchElementException):
            print("got exeption")
            pass
        driver.quit()


def masnavi():
    if not os.path.exists("../data/raw"):
        os.mkdir("../data/raw")
    if not os.path.exists("../data/raw/masnavi"):
        os.mkdir("../data/raw/masnavi")
    if not os.path.exists("../data/raw/masnavi/daftar-aval"):
        os.mkdir("../data/raw/masnavi/daftar-aval")
    if not os.path.exists("../data/raw/masnavi/daftar-dovom"):
        os.mkdir("../data/raw/masnavi/daftar-dovom")

    opts = Options()
    opts.set_headless()
    for i in range(1, 1):
        print(i)
        driver = Chrome(executable_path="e:/chromedriver89", options=opts)
        driver.get(f"https://ganjoor.net/moulavi/masnavi/daftar1/sh{i}/")
        try:
            header = driver.find_element_by_tag_name('h2').text
            elements_m1 = driver.find_elements_by_class_name("m1")
            elements_m2 = driver.find_elements_by_class_name("m2")
            poem = extract_poem(header, elements_m1, elements_m2)
            addToFile(i, poem, "masnavi/daftar-aval")
        except (NoSuchElementException):
            print("got exeption")
            pass
        driver.quit()
        print("daftar aval finished.")
        print("starting daftar dovom...")

    for i in range(1, 116):
        print(i)
        driver = Chrome(executable_path="e:/chromedriver89", options=opts)
        driver.get(f"https://ganjoor.net/moulavi/masnavi/daftar2/sh{i}/")
        try:
            header = driver.find_element_by_tag_name('h2').text
            elements_m1 = driver.find_elements_by_class_name("m1")
            elements_m2 = driver.find_elements_by_class_name("m2")
            poem = extract_poem(header, elements_m1, elements_m2)
            addToFile(i, poem, "masnavi/daftar-dovom")
        except (NoSuchElementException):
            print("got exeption")
            pass
        driver.quit()

def main():
    masnavi()
    divan_shams()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-m', action='store_true')
    p.add_argument('-s', action='store_true')
    args = p.parse_args()

    if args.m:
        masnavi()
    elif args.s:
        divan_shams()
    else:
        main()
