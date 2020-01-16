from chanreader.reader import Reader
from chanreader.parser import Parser


def process_data():
    reader = Reader()
    results = reader.get_chan_data()
    parser = Parser()
    boards_urls = parser.parse_boards(results)
    # TODO: Write somewhere


if __name__ == '__main__':
    process_data()
