def areSimilar(A, B):
    diff_count = 0
    for i, a in enumerate(A):
        if a != B[i]:
            diff_count += 1
    return diff_count <= 2 and sorted(A) == sorted(B)
