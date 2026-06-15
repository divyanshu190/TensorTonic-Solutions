def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    # Write code here
    indices = sorted(
        range(len(scores)),
        key = lambda i : scores[i],
        reverse = True
    )
    def iou(box1, box2):
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        a = max(0, x2-x1)
        b = max(0, y2-y1)

        area = a * b
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

        union = area1 + area2 - area
        return area / union if union > 0 else 0

    y = []
    while indices:
        maxi = indices.pop(0)
        y.append(maxi)

        remaining = []
        for idx in indices:
            if iou(boxes[maxi], boxes[idx]) < iou_threshold:
                remaining.append(idx)
        indices = remaining
    return y
    pass