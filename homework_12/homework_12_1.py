import codecs
import re

INPUT_FILE_NAME = "draft.html"
OUTPUT_FILE_NAME = "result.txt"


def delete_html_tags(html_file, result_file='cleaned.txt'):
    result_string = ""
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        # the pattern searches for any content as a payload of any teg but avoids only spaces or new row signs
        pattern = r">\s*([^<>\s]+[^<]*)\s*<"
        matched_list = re.findall(pattern, html)

        for row in matched_list:
            result_string += row + "\n"

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(result_string)


delete_html_tags(INPUT_FILE_NAME, OUTPUT_FILE_NAME)