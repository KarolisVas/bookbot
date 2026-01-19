import string

def count_words(text):
    return text.split()

def count_characters(text):
    list_of_chars = {}
    for c in text:
        lower_case = c.lower()
        if lower_case not in list_of_chars:
            list_of_chars[lower_case] = 1
        else:
            list_of_chars[lower_case] += 1
    return list_of_chars

def sort_dictionary(dictionary):
    list_of_chars = []
    for d in dictionary:
        list_of_chars.append({"char": d, "num": dictionary[d]})
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars

def sort_on(item):
    return item["num"]
