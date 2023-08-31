
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = [] 
        cur_words, cur_len = [], 0

        for word in words:
            if cur_len + len(word) + len(cur_words) > maxWidth:
                total_spaces = maxWidth - cur_len
                gaps = len(cur_words) - 1
                if gaps == 0:
                    res.append(cur_words[0] + ' ' * total_spaces)
                else:
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    line = ''
                    for i, w in enumerate(cur_words):
                        line += w
                        if i < gaps:
                            line += ' ' * space_per_gap
                            if i < extra_spaces:
                                line += ' '
                    res.append(line)
                cur_words, cur_len = [], 0
            cur_words.append(word)
            cur_len += len(word)

        last_line = ' '.join(cur_words)
        remaining_spaces = maxWidth - len(last_line)
        res.append(last_line + ' ' * remaining_spaces)

        return res
      
