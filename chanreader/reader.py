import time

from chanreader import const

import requests

# Number of seconds between requests
RATE_LIMIT = 1


class Reader(object):

    def get_chan_data(self):
        results = {}
        for board in const.CHAN_BOARDS:
            results[board] = self.get_board_data(board)
        return results

    def get_board_data(self, board):
        all_threads = []
        thread_num = 1
        while True:
            try:
                threads = requests.get('https://a.4cdn.org/{}/{}.json'.format(board, thread_num), timeout=5).json()
                all_threads.append(threads)
            except Exception:
                # The connection failed or the page was not found.
                break
            time.sleep(RATE_LIMIT)
            thread_num += 1
        return all_threads
