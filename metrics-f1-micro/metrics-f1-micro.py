def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            tp += 1
    fp = len(y_true) - tp
    fn = len(y_true) - tp
    if 2 * tp + fp + fn == 0:
        return 0.0
    return 2 * tp / (2 * tp + fp + fn)
    
    pass