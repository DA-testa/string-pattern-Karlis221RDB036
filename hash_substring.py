# python3

def read_input():
    cmd = input()

    if "I" in cmd:
        P = input()
        T = input()
    elif "F" in cmd:
        fn = input()
        if not "a" in fn:
            f = open("tests/"+fn, "r")
            text = f.readlines()
            P = text[0]
            T = text[1]

    return (P.rstrip(), T.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    pattern_length = len(pattern)
    text_length = len(text)
    result = []
    
    # caveman solution

    # for i in range(text_length-pattern_length+1):
    #     found = True
    #     for j in range(pattern_length-1):
    #         if pattern[j] != text[i+j]:
    #             found = False
    #             break
    #     if found:
    #         result.append(i)

    # Rabin Karp alghoritm
    h = 1
    d = 256
    q = 21
    pattern_hash = 0
    text_hash = 0
    
    for i in range(pattern_length-1):
        h = (d*h) % q

    for i in range(pattern_length):
        pattern_hash = (d*pattern_hash + ord(pattern[i])) % q
        text_hash = (d*text_hash + ord(text[i])) % q

    for i in range(text_length-pattern_length+1):
        if pattern_hash == text_hash:
            for j in range(pattern_length):
                if text[i+j] != pattern[j]:
                    break
            j += 1

            if j == pattern_length:
                result.append(i)

        if i < text_length-pattern_length:
            text_hash = (d*(text_hash-ord(text[i])*h) + ord(text[i + pattern_length]))% q

            if text_hash < 0:
                text_hash = text_hash + q

    return result

# this part launches the functions
if __name__ == '__main__':
    # print_occurrences(get_occurrences(*read_input()))
    # print(read_input())
    print_occurrences(get_occurrences(*read_input()))

