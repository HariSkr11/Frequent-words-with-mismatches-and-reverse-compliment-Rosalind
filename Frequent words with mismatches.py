def hamming_distance(String1,String2):
    return sum(1 for i in range(len(String1)) if String1[i]!=String2[i])
