def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code herek
    k = min(k, len(recommended))
    count = 0
    for i in range(k):
        if recommended[i] in relevant:
            count += 1
    return [count / k, count / len(relevant)]