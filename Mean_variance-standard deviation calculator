import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    

    a = np.array(list).reshape(3, 3)
    flat_a = a.flatten()
    

    calculations = {
        'mean': [
            np.mean(a, axis=0).tolist(), 
            np.mean(a, axis=1).tolist(), 
            np.mean(flat_a).tolist()
        ],
        'variance': [
            np.var(a, axis=0).tolist(), 
            np.var(a, axis=1).tolist(), 
            np.var(flat_a).tolist()
        ],
        'standard deviation': [
            np.std(a, axis=0).tolist(), 
            np.std(a, axis=1).tolist(), 
            np.std(flat_a).tolist()
        ],
        'max': [
            np.max(a, axis=0).tolist(), 
            np.max(a, axis=1).tolist(), 
            np.max(flat_a).tolist()
        ],
        'min': [
            np.min(a, axis=0).tolist(), 
            np.min(a, axis=1).tolist(), 
            np.min(flat_a).tolist()
        ],
        'sum': [
            np.sum(a, axis=0).tolist(), 
            np.sum(a, axis=1).tolist(), 
            np.sum(flat_a).tolist()
        ]
    }
    
    return calculations
