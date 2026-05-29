import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    loss = 0
    for i in range(len(y_true)):
        correct = y_true[i] # this is the correct class
        prob_correct = y_pred[i][correct] 
        loss += -np.log(prob_correct)
    return loss/len(y_true)
    pass