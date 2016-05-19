

def prob(list_of_lists):
    total = 0
    big_list = {}
    for jj in list_of_lists:
        if type(jj) is str:
            total += 1
            if jj not in big_list:
                big_list[jj] = 1
            else:
                big_list[jj] += 1
        else:
            for ii in jj:
                total += 1
                if ii not in big_list:
                    big_list[ii] = 1
                else:
                    big_list[ii] += 1
    for jj in big_list:
        big_list[jj] = big_list[jj]/total
    return big_list


def get_message_probability(tweet: [], target_class: [], other_classes: []) -> float:
    """
    returns the probability that tweet is part of the target class
    :param tweet: tokenized tweet
    :param target_class_counts: list of tweets in the target class
    :param other_classe_counts: list of lists of tweets in all other classes
    :return: probability that tweet is part of the target class
    """

    ham_probs = prob(target_class)
    spam_tweets = []
    for i in other_classes:
        for j in i:
            spam_tweets.append(j)
    spam_probs = prob(spam_tweets)

    H = len(target_class)  # number of tweets in target class
    S = len(spam_tweets)  # number of tweets in all other classes

    M = H + S

    def do_product(text, probabilities):
        prob_product = 1.0
        for hi in text:
            if hi in probabilities:
                prob_product *= probabilities[hi]
            else:
                prob_product *= 0  # TODO: figure out if this is right
                pass
        return prob_product

    prob_siS = do_product(tweet, spam_probs)
    prob_hiH = do_product(tweet, ham_probs)

    final_prob = (H/M * prob_hiH)/((H/M * prob_hiH)+(S/M * prob_siS))

    return final_prob


if __name__ == '__main__':
    positive_tweets = [["happy", "cake", "wonderful", "glad", "good", "good+", "good++"], ["happy", "glad", "good++"]]
    negative_tweets = [["sad", "bad", "cake", "mad", "bad+", "bad++"], ["a_bad_word"]]


    negative_probs = prob(negative_tweets)
    positive_probs = prob(positive_tweets)

    print("positive tweets", positive_probs)
    print("negative tweets", negative_probs)

    test_tweet = ["happy", "bad"]

    print("chance positive:", get_message_probability(test_tweet, positive_tweets, [negative_tweets]))
    print("chance negative:", get_message_probability(test_tweet, negative_tweets, [positive_tweets]))






