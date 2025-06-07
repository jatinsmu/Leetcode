from typing import List


def addBoldTag(s: str, words: List[str]) -> str:
    # create an array of indexes in s where each index will tell if we need to make that character bold or not
    bold_status = [False] * len(s)
    start_index = 0

    for word in words:
        # get the starting index where we find the match for word in s. If there are multiple matches, it'll return the
        # lowest index match. We need to manually loop thrrough the whole s to find all matches
        substirng_occurences = []  # keep all start positions of word in s. Later on loop throught them and assing True to bold_status
        lowest_index_match = 0

        while lowest_index_match != -1:
            lowest_index_match = s.find(word, start_index)
            # start_index will be -1 if word is not found
            if lowest_index_match != -1:
                substirng_occurences.append(lowest_index_match)
                # if length of current word is 1, then dont subtract 1 from it, as in that case we wont move forward
                if len(word) != 1:
                    start_index = lowest_index_match + len(
                        word) - 1  # to get the index from where we have to start the search again in the remaining s
                else:
                    start_index = lowest_index_match + len(word)

        # now substirng_occurences will contain all start indexes where we need to add True for the length of the word
        for start_index in substirng_occurences:
            # for each char starting from start_index until the index of length of current word. mark True
            for i in range(start_index, start_index + len(word)):
                bold_status[i] = True

    # now loop through the bold_status array and add a <b> tag before starting of a true element. if there is a continuation true, add </b> when encounter a false
    final_chars = []
    prev_char = False
    open_bracket = False

    for i in range(len(bold_status)):
        if bold_status[i] and not prev_char:
            # start of a new bold tag
            final_chars.append('<b>')
            open_bracket = True
        elif not bold_status[i] and open_bracket:
            # end of bold tag, as current element is of False status and there was an open bracket before this
            final_chars.append('</b>')
            open_bracket = False

        final_chars.append(s[i])
        prev_char = bold_status[i]  # add value of current status to prev_char

    # edge case, if the last element was also True, then we wouldnt have added the closing tag. So add it now
    if prev_char:
        final_chars.append('</b>')

    return ''.join(final_chars)


assert True if addBoldTag('aaabbb', ['aa', 'b']) == '<b>aaabbb</b>' else False
assert True if addBoldTag('abcxyz123', ['abc', '123']) == '<b>abc</b>xyz<b>123</b>' else False
