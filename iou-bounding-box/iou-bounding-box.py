def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    [x1, y1, x2, y2] = box_a
    [a1, b1, a2, b2] = box_b

    inter_x1 = max(x1, a1)
    inter_y1 = max(y1, b1)
    inter_x2 = min(x2, a2)
    inter_y2 = min(y2, b2)

    w = max(0, inter_x2 - inter_x1)
    b = max(0, inter_y2 - inter_y1)
    intersection = w * b
    union = (x2 - x1) * (y2 - y1) + (a2 - a1) * (b2 - b1) - intersection
    if union == 0:
        return 0.0
    iou = intersection / union
    return iou
    pass