class TrieNode:

    def __init__(self):

        # Used children dictionary for trie nodes.
        self.children = {}

        # Used index to store best matching word index.
        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        # Used root as trie root node.
        root = TrieNode()

        # Used bestIndex for shortest overall word.
        bestIndex = 0

        # Looped through container words.
        for i in range(len(wordsContainer)):

            # Updated shortest word index.
            if len(wordsContainer[i]) < len(wordsContainer[bestIndex]):
                bestIndex = i

        # Looped through container words with indices.
        for i, word in enumerate(wordsContainer):

            # Reversed word for suffix trie.
            reversedWord = word[::-1]

            # Used node to traverse trie.
            node = root

            # Updated root best index if needed.
            if (
                node.index == -1 or
                len(word) < len(wordsContainer[node.index])
            ):
                node.index = i

            # Looped through reversed characters.
            for char in reversedWord:

                # Created trie node if character did not exist.
                if char not in node.children:
                    node.children[char] = TrieNode()

                # Moved to next trie node.
                node = node.children[char]

                # Updated node index using shortest word rule.
                if (
                    node.index == -1 or
                    len(word) < len(wordsContainer[node.index])
                ):
                    node.index = i

        # Used result to store answers.
        result = []

        # Looped through query words.
        for word in wordsQuery:

            # Reversed query word.
            reversedWord = word[::-1]

            # Used node to traverse trie.
            node = root

            # Used answer as default shortest word index.
            answer = node.index

            # Looped through reversed query characters.
            for char in reversedWord:

                # Stopped if suffix path did not exist.
                if char not in node.children:
                    break

                # Moved to next trie node.
                node = node.children[char]

                # Updated answer with deeper suffix match.
                answer = node.index

            # Added answer to result.
            result.append(answer)

        # Returned all query answers.
        return result