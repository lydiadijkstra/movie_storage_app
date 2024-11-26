HTML_FILE_PATH = 'templates/index_template.html'


def read_html_file():
    """
    Loads the html-file
    :param html_file_path: index_template.html
    :return: data from html_file
    """
    with open(HTML_FILE_PATH, "r", encoding="utf-8") as fileobject:
        return fileobject.read()


def replace_string_html(output):
    """
    Replaces the placeholder text and returns the new string
    :param html_content: the html-content which will be updated with string
    :param output: string which will be shown on generated website
    :return: new content for generating movie website
    """
    html_content = read_html_file()
    if len(output) >= 1:
        new_html_content = html_content.replace("__TEMPLATE_MOVIE_GRID__", output)
    else:
        new_html_content = html_content.replace("__TEMPLATE_MOVIE_GRID__", "No movies in the database at the moment!")
    return new_html_content


def dump_data_to_html(new_html_content):
    """
    Dumps the new string in a new created html-file,
    afterward the generated website shows chosen movie data
    :param new_html_content: new content which will be shown
    """
    with open("templates/movie_index_template.html", "w", encoding="utf-8") as fileobj:
        fileobj.write(new_html_content)
