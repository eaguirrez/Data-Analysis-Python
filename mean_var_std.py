import numpy as np

def calculate(lst):
    # check the list length
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')

    # reshape the list
    arr = np.array(lst).reshape((3, 3))

    # calculate the items for the dictionary
    mean = [
        np.mean(arr, axis=0).tolist(),
        np.mean(arr, axis=1).tolist(),
        np.mean(arr).tolist()
    ]

    variance = [
        np.var(arr, axis=0).tolist(),
        np.var(arr, axis=1).tolist(),
        np.var(arr).tolist()
    ]

    standard_deviation = [
        np.std(arr, axis=0).tolist(),
        np.std(arr, axis=1).tolist(),
        np.std(arr).tolist()
    ]

    maximum = [
        np.max(arr, axis=0).tolist(),
        np.max(arr, axis=1).tolist(),
        np.max(arr).tolist()
    ]

    minimum = [
        np.min(arr, axis=0).tolist(),
        np.min(arr, axis=1).tolist(),
        np.min(arr).tolist()
    ]

    total = [
        np.sum(arr, axis=0).tolist(),
        np.sum(arr, axis=1).tolist(),
        np.sum(arr).tolist()
    ]

    calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation,
        "max": maximum,
        "min": minimum,
        "sum": total
    }

    return calculations
