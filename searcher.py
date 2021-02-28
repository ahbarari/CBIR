import numpy as np
import csv


def chi2_distance(hist_a, hist_b, eps=1e-10):
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(hist_a, hist_b)])
    return d


class Searcher:
    def __init__(self, index_path):
        self.index_path = index_path

    def search(self, query_features, limit=9):
        results = {}
        with open(self.index_path) as f:
            reader = csv.reader(f)
            for row in reader:
                features = [float(x) for x in row[1:]]
                d = chi2_distance(features, query_features)
                results[row[0]] = d
            f.close()
        results = sorted([(v, k) for (k, v) in results.items()])
        return results[:limit]
