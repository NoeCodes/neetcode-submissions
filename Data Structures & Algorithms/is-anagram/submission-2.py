class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scannedLettersOne = {}
        scannedLettersTwo = {}

        # Must have same amount of letters
        if len(s) != len(t):
            return False

        # Collect letters and their frequencies for word one
        for letter in s:
            scannedLettersOne[letter] = scannedLettersOne.get(letter, 0) + 1

        # Collect letter and their frequencies for word two
        for letter in t:
            scannedLettersTwo[letter] = scannedLettersTwo.get(letter, 0) + 1

        # Check for any mis matches
        for key in scannedLettersOne:
            if scannedLettersOne.get(key) != scannedLettersTwo.get(key):
                return False

        return True