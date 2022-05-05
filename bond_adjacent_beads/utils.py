import numpy as np

def create_bonds(arr, prob_cr):
    """ create bonds between [i,i+1] by changing type from 1 to 2"""
    inds0 = np.where(arr==1)[0]
    inds1 = inds0[np.where(inds0[1:]-inds0[:-1]==1)[0]]
    #print(f"create {inds1}")
    np.random.shuffle(inds1)
    skip_lst = []
    for start in inds1:
        if start in skip_lst:
            continue
        if np.random.uniform() < prob_cr:
            arr[start] = 2
            arr[start+1] = 2
            skip_lst.append(start+1)
            skip_lst.append(start-1)

def remove_bonds(arr, prob_br):
    """ remove bonds between [i,i+1] by changing type from 2 to 1"""
    #print(f"all bonded beads {np.where(arr==2)[0]}")
    inds0 = np.where(arr==2)[0][::2]
    #print(f"break1 {inds0}")
    np.random.shuffle(inds0)
    for start in inds0:
        if np.random.uniform() < prob_br:
            arr[start] = 1
            arr[start+1] = 1
            
def a_to_b_and_back(arr, prob_a_to_b, prob_b_to_a):            
    inds_a = np.where((arr==0) & (np.random.uniform(0,1,len(arr)) < prob_a_to_b))[0]
    inds_b = np.where((arr==1) & (np.random.uniform(0,1,len(arr)) < prob_b_to_a))[0]
    arr[inds_a] = 1
    arr[inds_b] = 0
    
#    np.random.shuffle(inds_a)
#    arr[]
#    np.random.shuffle(inds_b)
#    for i in inds_a:
#        if np.random.uniform() < prob_a_to_b:
#            arr[i] = 1
#    for i in inds_b:
#        if np.random.uniform() < prob_b_to_a:
#            arr[i] = 0

def step(arr, prob_cr, prob_br, prob_ab, prob_ba):
    """ The simplest step in simulation """
    remove_bonds(arr, prob_br)
    create_bonds(arr, prob_cr)
    a_to_b_and_back(arr, prob_ab, prob_ba)
    
def find_runs(x):
    """Find runs of consecutive items in an array.
        author: alimanfoo Alistair Miles"""

    # ensure array
    x = np.asanyarray(x)
    if x.ndim != 1:
        raise ValueError('only 1D array supported')
    n = x.shape[0]

    # handle empty array
    if n == 0:
        return np.array([]), np.array([]), np.array([])

    else:
        # find run starts
        loc_run_start = np.empty(n, dtype=bool)
        loc_run_start[0] = True
        np.not_equal(x[:-1], x[1:], out=loc_run_start[1:])
        run_starts = np.nonzero(loc_run_start)[0]

        # find run values
        run_values = x[loc_run_start]

        # find run lengths
        run_lengths = np.diff(np.append(run_starts, n))

        return run_values, run_starts, run_lengths

def nested_list_comprehension(lsts):
    return [item for sublist in lsts for item in sublist]