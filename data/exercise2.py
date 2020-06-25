## From Lesson 7
def complement_base(base):
    """Returns the Watson-Crick complement of a base."""
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq):
    """Compute reverse complement of a sequence."""
    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base)

    return rev_seq
    
## Exercise 2, rewrite reverse_complement() using a for loop, but not using the function reversed()

def reverse_complement_new(seq):
    """Compute reverse complement of a sequence."""
    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    for base in seq[::-1]:
        rev_seq += complement_base(base)

    return rev_seq

def reverse_complement_nofor(seq):
    """Compute reverse complement of a sequence."""
    # Initialize reverse complement

    rev_orig = seq[::-1]
    rev_seq = rev_orig

    # Find indices for A, C, G, T
    index_A = rev_orig.index('A')
    index_C = rev_orig.index('C')
    index_G = rev_orig.index('G')
    index_T = rev_orig.index('T')
    
    rev_seq[index_A] = 'T'
    rev_seq[index_C] = 'G'
    rev_seq[index_G] = 'C'
    rev_seq[index_T] = 'A'

    return rev_seq
