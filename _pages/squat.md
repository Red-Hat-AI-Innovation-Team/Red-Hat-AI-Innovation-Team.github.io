---
layout: page
title: SQuat
permalink: /squat/
image: '/images/squat/kvcache.png'
---

# SQuat: Subspace-orthogonal KV Cache Quantization

**Authors:** Hao Wang*, Ligong Han*, Kai Xu, Akash Srivastava  
*Equal contribution  
Red Hat AI Innovation  
Conference on Language Modeling (COLM) 2025

---

## Abstract

We introduce a new KV cache quantization algorithm: SQuat (Subspace-orthogonal KV cache quantization). SQuat is training-free, requires no calibration data, runs on-the-fly, and is grounded in a theoretical framework we developed. Empirically, it reduces GPU peak memory by 2.17× to 2.82×, improves throughput by 2.45× to 3.60×, and achieves more favorable benchmark scores than existing KV cache quantization algorithms.

![KV Cache Quantization Overview](/images/squat/kvcache.png)

## Method

SQuat first constructs a subspace that captures the most critical task-related information. During key tensor quantization, it ensures that the difference between the (de)quantized and original keys remains orthogonal to this subspace, thereby minimizing the impact of quantization errors on the attention mechanism's outputs.

![SQuat Method Overview](/images/squat/results.png)

## Results

Our experimental evaluation demonstrates significant improvements across multiple dimensions:

![Performance Results](/images/squat/table1.png)

![Benchmark Comparison](/images/squat/table2.png)

## Key Contributions

- **Training-free approach**: No need for calibration data or model retraining
- **Theoretical foundation**: Grounded in subspace orthogonality principles
- **Significant efficiency gains**: 2.17× to 2.82× memory reduction and 2.45× to 3.60× throughput improvement
- **Superior performance**: Outperforms existing KV cache quantization methods on standard benchmarks

## Resources

- **Paper**: [https://arxiv.org/abs/2503.24358](https://arxiv.org/abs/2503.24358)
- **Code**: [https://github.com/Red-Hat-AI-Innovation-Team/SQuat](https://github.com/Red-Hat-AI-Innovation-Team/SQuat)

## Citation

```bibtex
@inproceedings{wang2025squat,
  title={SQuat: Subspace-orthogonal KV Cache Quantization},
  author={Wang, Hao and Han, Ligong and Xu, Kai and Srivastava, Akash},
  booktitle={Conference on Language Modeling},
  year={2025}
}
```