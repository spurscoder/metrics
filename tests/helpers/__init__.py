import random

import numpy
import torch

from torchmetrics.utilities.imports import _TORCH_LOWER_1_4, _TORCH_LOWER_1_5, _TORCH_LOWER_1_6

_MARK_TORCH_MIN_1_4 = dict(condition=_TORCH_LOWER_1_4, reason="required PT >= 1.4")
_MARK_TORCH_MIN_1_5 = dict(condition=_TORCH_LOWER_1_5, reason="required PT >= 1.5")
_MARK_TORCH_MIN_1_6 = dict(condition=_TORCH_LOWER_1_6, reason="required PT >= 1.6")


def seed_all(seed):
    random.seed(seed)
    numpy.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
