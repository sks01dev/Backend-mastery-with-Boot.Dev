def find_longest_word(document, longest_word=""):
    # base case
    if document == "":
        return longest_word

    # split in format : [first_word, rest of the document]
    if " " in document:
        first_word, rest = document.split(' ', maxsplit = 1)
    else:
        first_word, rest = document, ""

    if len(first_word) > len(longest_word):
        longest_word = first_word

    # recursively call for the rest of document
    return find_longest_word(rest, longest_word)


