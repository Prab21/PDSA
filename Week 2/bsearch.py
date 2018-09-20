# Binary Search

def bsearch(seq, v, l, r):
    ''' Search for v in seq[l:r], seq is sorted '''
    if (r-l == 0):
        return(False)

    mid = (r+l)//2
    if (v == seq[mid]):
        return(True)

    if( v < seq[mid]):
        return(bsearch(seq, v, l, mid))
    else:
        return(bsearch(seq, v, mid+1, r))
