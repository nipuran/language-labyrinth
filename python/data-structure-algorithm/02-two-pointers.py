# two pointer technique

def isPalindrom(word: str) -> bool:
    firstIndex = 0
    lastIndex = len(word) - 1

    while firstIndex < lastIndex:
        if word[firstIndex] != word[lastIndex]:
            return False

        firstIndex += 1
        lastIndex -= 1
    
    return True


def main():
    print(isPalindrom('abcba'))

if __name__ == '__main__':
    main()
