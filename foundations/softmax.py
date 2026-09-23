import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        esum = 0
        m = np.max(z)
        exps = []
        for num in z:
            ans = np.exp(num - m)
            esum += ans
            exps.append(ans)

        softmaxlist = []
        for e in exps:
            softmaxlist.append(e / esum)
        return np.round(np.array(softmaxlist),4)
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)

        pass
