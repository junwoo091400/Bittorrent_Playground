'''

http://www.bittorrent.org/beps/bep_0003.html

'''

from enum import Enum

class BT_BEncoding:
    class BE_Types(Enum):
        NONE = 0
        STRING = 1
        INTEGER = 2
        LIST = 3
        DICTIONARY = 4
    
    def __init__(self):
        self._current_idx = -1
        self._current_type = self.BE_Types.NONE
        self._decoded_result = None


    def decode_torrent(txt):



fname = 'onboarding_0-0-3.v1.torrent'
file_text = open(fname).read()
