#  Copyright (c) Meta Platforms, Inc. and affiliates.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
"""
GEMM Specialization: Sigmoid(GEMM_RCR(A, B) + Bias) * D0
"""

from .gemm_rcr_bias_broadcast import gemm_rcr_bias_broadcast

# pylint: disable=C0103, W0223, W0221


class gemm_rcr_bias_sigmoid_mul(gemm_rcr_bias_broadcast):
    """GEMM Specialization: Sigmoid(GEMM_RCR(A, B) + Bias) * D0

    This operator is equivalent to the following pytorch code:

    .. highlight:: python
    .. code-block:: python

        A = torch.randn(M, K).cuda().half()
        B = torch.randn(N, K).cuda().half()
        Bias = torch.randn(N).cuda().half()
        D0 = torch.randn(M, N).cuda().half()

        linear = torch.nn.functional.linear(A, B, bias=Bias)
        y = torch.sigmoid(linear) * D0
    """

    def __init__(self):
        super().__init__()
        self._attrs["op"] = "gemm_rcr_bias_sigmoid_mul"
        self._attrs["num_sources"] = 1