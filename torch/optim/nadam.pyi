from typing import Tuple

from .optimizer import _params_t, Optimizer

class NAdam(Optimizer):
    def __init__(
        self,
        params: _params_t,
        lr: float = ...,
        betas: Tuple[float, float] = ...,
        eps: float = ...,
        weight_decay: float = ...,
        momentum_decay: float = ...,
        decoupled_weight_decay: bool = ...,
    ) -> None: ...
