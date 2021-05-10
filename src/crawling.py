from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import csv
import argparse

# def delete_half_space(poem):
#    if '\u200c' in poem:
#        poem.replace('\u200c', ' ')
#    return poem


def addToFile(num, poem):
    try:
        with open(f"{num}.csv", "a", encoding="utf-8") as csvfile:
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
    opts = Options()
    opts.set_headless()

    for i in range(200, 201):
        print(i)
        driver = Chrome(executable_path="e:/chromedriver89", options=opts)
        driver.get(f"https://ganjoor.net/moulavi/shams/ghazalsh/sh{i}/")
        try:
            header = driver.find_element_by_tag_name('h2').text
            elements_m1 = driver.find_elements_by_class_name("m1")
            elements_m2 = driver.find_elements_by_class_name("m2")
            poem = extract_poem(header, elements_m1, elements_m2)
            addToFile(i, poem)
        except (NoSuchElementException):
            print("got exeption")
            pass
        driver.quit()


def masnavi():
    opts = Options()
    opts.set_headless()

    for i in range(1, 173):
        print(i)
        driver = Chrome(executable_path="e:/chromedriver89", options=opts)
        driver.get(f"https://ganjoor.net/moulavi/masnavi/daftar1/sh{i}/")
        try:
            header = driver.find_element_by_tag_name('h2').text
            elements_m1 = driver.find_elements_by_class_name("m1")
            elements_m2 = driver.find_elements_by_class_name("m2")
            poem = extract_poem(header, elements_m1, elements_m2)
            addToFile(i, poem)
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
