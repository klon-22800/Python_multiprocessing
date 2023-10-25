import re
from itertools import starmap
from time import time
from multiprocessing import Pool


def file_read(path: str) -> str:
    f = open(path, "r", encoding="utf-8")
    text = f.read()
    f.close()
    return text


def text_update(text: str) -> list:
    text = re.sub(r"[^\w\s]", "", text)
    text = text.lower()
    text = text.split()
    return text


def find(key_word: str, path: str) -> None:
    text = file_read(path)
    text = text_update(text)
    if key_word in text:
        print(f'keyword "{key_word}" найден в {path}')
    else:
        print(f'keyword "{key_word}" не найден в {path}')
    return None


def main() -> None:
    print(
        "Укажите слово для поиска и название файлов через запятую в фомате: keyword, filename1.txt, ..."
    )
    ## Пример для запроса
    ## Выбор, Demons.txt, War and peace.txt, The gambler.txt, The idiot.txt, The Karamazov brothers.txt, Crime and punishment.txt, The insulted and the injured.txt
    data = input().split(", ")
    key_word = data[0].lower()
    paths = data[1:]
    key_word = [key_word] * len(paths)
    t = time()
    with Pool(4) as p:
        p.starmap(find, zip(key_word, paths))
    print(time() - t)
    input("Нажмите Enter")
    return None


if __name__ == "__main__":
    main()
