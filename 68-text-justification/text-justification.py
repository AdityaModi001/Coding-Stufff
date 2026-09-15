class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
            """
        n = len(words)
        final_res = []
        i = 0

        while i < n:

            dumm_res = []
            total_len = 0

            # Find words that fit in this line
            while i < n:

                word = words[i]
                gap = 1 if dumm_res else 0

                if total_len + gap + len(word) <= maxWidth:
                    dumm_res.append(word)
                    total_len += gap + len(word)
                    i += 1
                else:
                    break

            # Last line
            if i == n:
                line = " ".join(dumm_res)
                line += " " * (maxWidth - len(line))
                final_res.append(line)
                break

            # Calculate spaces
            total_len = 0
            count_word = 0

            for each_word in dumm_res:
                total_len += len(each_word)
                count_word += 1

            required_gap = maxWidth - total_len
            required_num_gaps = count_word - 1

            if required_num_gaps == 0:
                line = dumm_res[0] + " " * required_gap
                final_res.append(line)
                continue

            gaps = required_gap // required_num_gaps
            extra = required_gap % required_num_gaps

            line = ""

            for j in range(len(dumm_res)):
                line += dumm_res[j]

                if j < len(dumm_res) - 1:
                    line += " " * gaps

                    if j < extra:
                        line += " "

            final_res.append(line)

        return final_res
