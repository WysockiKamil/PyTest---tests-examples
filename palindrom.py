def ifPalindrome(word):

    normalized_str = word.lower().replace(" ", "")
    return normalized_str == normalized_str[::-1]