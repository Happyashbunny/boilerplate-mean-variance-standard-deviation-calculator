import numpy as np

def calculate(list):
    try:
        if len(list) < 9:
            raise ValueError('List must contain nine numbers.')
        array = np.array(list)
        matrix = array.reshape(3,3)
        Dict = {
            'mean' : [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(array).tolist()],
            'variance' : [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(array).tolist()], 
            'standard deviation' : [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(array).tolist()],
            'max' : [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(array).tolist()],
            'min' : [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(array).tolist()],
            'sum' : [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(array).tolist()]
        }

        return Dict

            
    except ValueError:
        raise ValueError('List must contain nine numbers.')