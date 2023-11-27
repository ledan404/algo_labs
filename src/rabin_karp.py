"""

Serach for a pattern in a given string Karp-Rabin algorithm

"""
D = 256


def search(needele, haystack):
    """

    Rabin-Karp algorithm

    """
    m = len(needele)
    n = len(haystack)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    q = 101
    result = []
    for i in range(m - 1):
        h = (h * D) % q

    for i in range(m):
        p = (D * p + ord(needele[i])) % q
        t = (D * t + ord(haystack[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if haystack[i + j] != needele[j]:
                    break
                else:
                    j += 1

            if j == m:
                result.append(i)

        if i < n - m:
            t = (D * (t - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
            if t < 0:
                t = t + q
    return result


if __name__ == "__main__":
    haystack = "GEEKS FOR GEEKS"
    needele = "GEEK"
    print(search(needele, haystack))
