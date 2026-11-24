corpus = [
    ["l", "o", "w"],
    ["l", "o", "w", "e", "r"],
    ["l", "o", "w", "e", "s", "t"],
    ["l", "o", "w"],
    ["l", "o", "w", "e", "r"]
]

def get_pair_frequencies(corpus):
    '''
    Count frequences of adjacent token pairs.

    Args:
        corpus: List of tokenized words

    Returns:
        Dictionary mappign adjacent token pairs to frequencies
    '''
    pair_frequency = {}
    for word in corpus:
        for i in range(len(word) - 1):

            pair = (word[i], word[i+1])

            pair_frequency[pair] = pair_frequency.get(pair, 0) + 1
            # get method checks wheter a key exisits in a dict. if it does then it returns the value of the key else it makes a key with a initialized value. in our case the initialize value is 0

    return pair_frequency


def merge_pair(corpus, pair):
    left_token, right_token = pair

    merged_token = left_token + right_token

    new_corpus = []

    for word in corpus:
        merged_word = []
        i = 0

        while i < len(word):
            if i+1 < len(word) and word[i] == left_token and word[i+1] == right_token:
                merged_word.append(merged_token)
                i+=2
            else:
                merged_word.append(word[i])
                i+=1
        new_corpus.append(merged_word)

    # print(corpus)
    return new_corpus

def train_bpe(corpus, num_merges: int):
    """
    Train BPE by repeatedly merging the most frequent pair.

    Returns:
        merges: Ordered list of learned merge rules.
        corpus: Final tokenized corpus.
    """

    if num_merges < 0:
        raise ValueError('num_merges must be non-negative')
    
    merges = []
    for i in range(num_merges):
        frequecies = get_pair_frequencies(corpus)

        if not frequecies:
            break

        # print(frequecies)
        
        max_frequency = max(frequecies.items(), key=lambda item: item[1])
        pair, _ = max_frequency

        # append pair in merges
        merges.append(pair)

        corpus = merge_pair(corpus, pair)

    # vocab = set(corpus)
    # print(vocab)
    print(corpus)
    return merges, corpus

if __name__ == '__main__':
    # get_pair_frequencies(corpus=corpus)

    # pair = ('l', 'o')
    # new_corpus = merge_pair(corpus, pair)
    # print(new_corpus)

    merges, corpus = train_bpe(corpus, 5)
    print('------------------merges------------------------')
    print(merges)
    print('------------------corpus------------------------')
    print(corpus)

