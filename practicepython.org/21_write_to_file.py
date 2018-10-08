from decode_webpage import nytimes_titles

__author__ = "Geoffrey Bachelot"


def save_nytimes_titles(filename="NYT_titles.txt"):
    with open(filename, 'w', encoding='utf-8') as open_file:
        open_file.write(nytimes_titles())

if __name__ == "__main__":
    save_nytimes_titles()