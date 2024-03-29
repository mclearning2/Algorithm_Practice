'''
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
'''

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        seq = 0
        for d in data:
            seq = seq << 8 | d
        def dfs(idx, cnt = 0):
            if idx < 0:
                return None
            bits8 = (seq >> (8 * idx)) & 0xff
            if cnt == 0:
                if bits8 >> 3 == 0b11110:
                    r = dfs(idx-1, 3)
                elif bits8  >> 4 == 0b1110:
                    r = dfs(idx-1, 2)
                elif bits8 >> 5 == 0b110:
                    r = dfs(idx-1, 1)
                elif bits8 >> 7 == 0b0:
                    r = 0
                else:
                    r = None
                return None if r is None else r + 1
            elif cnt > 1:
                if bits8 >> 6 == 0b10:
                    r = dfs(idx-1, cnt - 1)
                else:
                    r = None
                return None if r is None else r + 1
            elif cnt == 1:
                if bits8 >> 6 == 0b10:
                    return 1
                else:
                    return None
        
        idx = len(data) - 1
        while 0 <= idx:
            re = dfs(idx)
            if re is None:
                return False
            else:
                idx -= re
        return True
            
            
