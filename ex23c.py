import sys
script, input_encoding, error = sys.argv

def main(language_file):
    line = language_file.readline().encode('raw_unicode_escape')

    if line:
        print_line(line)
        return main(language_file)

def print_line(line):
    lang = line.strip()
    mystring = lang.decode()
    mybytes = mystring.encode('utf-8')

    print(mystring, "<===>", mybytes)

languages = open("languages.txt", 'r', encoding="unicode_escape")

main(languages)

languages.close()
