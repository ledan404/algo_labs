"""
Search for a pattern in a text using Rabin-Karp algorithm.
"""


def rabin_karp(text, pattern):
    """
    Args:
    text : Text to be searched.
    pattern : Pattern to be searched.
    """
    m = len(pattern)
    q = 101
    result = []

    pattern_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * q + ord(pattern[i])) % q
    text_hash = 0
    for i in range(m):
        text_hash = (text_hash * q + ord(text[i])) % q

    for i in range(len(text) - m + 1):
        if pattern_hash == text_hash and text[i : i + m] == pattern:
            result.append(i)

        if i < len(text) - m:
            text_hash = (
                text_hash * q - ord(text[i]) * (q ** (m - 1)) + ord(text[i + m])
            ) % q
    return result


if __name__ == "__main__":
    HAYSTACK = "abracadabraabra"
    NEEDLE = "abra"
    output = rabin_karp(HAYSTACK, NEEDLE)
    print("All elements finded:", output)
