# O(n^3)
def maxCSS3(seq):
    max_so_far = 0
    for start_idx in range(len(seq)):
        for end_idx in range( start_idx, len(seq)):
            seq_sum = 0
            for i in range(start_idx, end_idx+1):
                seq_sum = seq_sum + seq[i]  # seq_sum += seq[i]
            if seq_sum > max_so_far:
                max_so_far = seq_sum

    return max_so_far

# O(n^2)
def maxCSS2(seq):
    max_so_far = 0
    for start_idx in range(len(seq)):
        seq_sum = 0
        for end_idx in range( start_idx, len(seq)):
            seq_sum = seq_sum + seq[end_idx]  # seq_sum += seq[end_idx]
            if seq_sum > max_so_far:
                max_so_far = seq_sum

    return max_so_far

# O(n)
def maxCSS(seq):
    max_so_far = 0
    seq_sum = 0
    for start_idx in range(len(seq)):
        seq_sum = seq_sum + seq[start_idx]  # seq_sum += seq[start_idx]
        if seq_sum > max_so_far:
            max_so_far = seq_sum
        if seq_sum < 0:
            seq_sum = 0

    return max_so_far


if __name__ == '__main__':
    mylist = [-2, 11, -4, 13, -5, 2]

    max = maxCSS(mylist)

    print(max)
