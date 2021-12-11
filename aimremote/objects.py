from aim import Distribution as AimDistribution
from aim import Image as AimImage
from torch import tensor
import numpy as np

# TODO: support image
# TODO: dont inherit from AimDistribution but convert in server on track

class Distribution(AimDistribution):
    def __init__(self, distribution = tensor([])):
        super().__init__(distribution)
        self.distribution = distribution

    def __setstate__(self, data):
        try:
            np_histogram = np.histogram(data, bins=self.storage['bin_count'])
        except TypeError:
            raise TypeError(f'Cannot convert to aim.Distribution. Unsupported type {type(distribution)}.')
        self._from_np_histogram(np_histogram)
        self.distribution = data

    def __getstate__(self):
        return self.distribution