import re

from chanreader import const

import validators


class Parser(object):

    def parse_boards(self, results):
        parsed_urls = {}
        for board in const.CHAN_BOARDS:
            parsed_urls[board] = self.parse_board(results[board])
        return parsed_urls

    def parse_board(self, board_data):
        urls = []
        for threads in board_data:
            for posts in threads['threads']:
                for post in posts['posts']:
                    urls.extend(self.parse_comment(post.get('com')))
                    urls.extend(self.parse_comment(post.get('sub')))
        cleaned_urls = self.clean_urls(urls)
        valid_urls = self.get_valid_urls(cleaned_urls)
        return valid_urls

    def parse_comment(self, comment):
        urls = []
        if comment:
            urls = re.findall(const.URL_REGEX, comment)
        return urls

    def clean_urls(self, urls):
        cleaned_urls = []
        for url in urls:
            cleaned_urls.extend(self.clean_url(url))
        return cleaned_urls

    def clean_url(self, url):
        url_data = []
        url_split = url.split('<br>')
        for item in url_split:
            if item.startswith('https://') or item.startswith('http://'):
                is_tag = False
                cleaned_url = ''
                for letter in item:
                    if letter == '<':
                        is_tag = True
                    elif letter == '>':
                        is_tag = False
                        continue
                    if not is_tag:
                        cleaned_url += letter
                url_data.append(cleaned_url)
        return url_data

    def get_valid_urls(self, urls):
        valid_urls = []
        for url in urls:
            if validators.url(url):
                valid_urls.append(url)
        return valid_urls
