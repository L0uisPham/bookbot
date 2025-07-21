def words_count(text):
    return len(text.split())


def char_counts(raw_text):
    res = dict()
    text = raw_text.lower()

    for c in text:
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1

    return res


def format_results(dict, counts, path="books/frankenstein.txt"):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {counts} total words")
    print("----------- Character Count ----------")
    for key, val in dict.items():
        print(f"{key}: {val}")
    print("============= END ===============")
