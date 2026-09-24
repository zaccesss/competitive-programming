class TrieNode:

    def __init__(self):

        # used children dictionary for trie nodes.
        self.children = {}

        # used index to store best matching word index.
        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        # used root as trie root node.
        root = TrieNode()

        # used bestIndex for shortest overall word.
        bestIndex = 0

        # looped through container words.
        for i in range(len(wordsContainer)):

            # updated shortest word index.
            if len(wordsContainer[i]) < len(wordsContainer[bestIndex]):
                bestIndex = i

        # looped through container words with indices.
        for i, word in enumerate(wordsContainer):

            # reversed word for suffix trie.
            reversedWord = word[::-1]

            # used node to traverse trie.
            node = root

            # updated root best index if needed.
            if (
                node.index == -1 or
                len(word) < len(wordsContainer[node.index])
            ):
                node.index = i

            # looped through reversed characters.
            for char in reversedWord:

                # created trie node if character did not exist.
                if char not in node.children:
                    node.children[char] = TrieNode()

                # moved to next trie node.
                node = node.children[char]

                # updated node index using shortest word rule.
                if (
                    node.index == -1 or
                    len(word) < len(wordsContainer[node.index])
                ):
                    node.index = i

        # used result to store answers.
        result = []

        # looped through query words.
        for word in wordsQuery:

            # reversed query word.
            reversedWord = word[::-1]

            # used node to traverse trie.
            node = root

            # used answer as default shortest word index.
            answer = node.index

            # looped through reversed query characters.
            for char in reversedWord:

                # stopped if suffix path did not exist.
                if char not in node.children:
                    break

                # moved to next trie node.
                node = node.children[char]

                # updated answer with deeper suffix match.
                answer = node.index

            # added answer to result.
            result.append(answer)

        # returned all query answers.
        return result