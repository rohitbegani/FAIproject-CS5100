def getRating(score):
    if score == 0:
        return 0
    elif 0 <= score < 1:
        return 0.5
    elif 1 <= score < 2:
        return 1
    elif 2 <= score < 3:
        return 1.5
    elif 3 <= score <4:
        return 2
    elif 4 <= score < 5:
        return 2.5
    elif 5 <= score < 6:
        return 3
    elif 6 <= score < 7:
        return 3.5
    elif 7 <= score < 8:
        return 4
    elif 8 <= score < 9:
        return 4.5
    elif 9 <= score < 10:
        return 5

def MAE(pred, b):
    sum = 0
    count = len(pred)
    for p in pred:
        ur = p.findHighestUserRating(b)
        pr = getRating(p.predictionScore)
        sum += abs(pr - ur)
    return sum/count