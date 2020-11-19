---
layout: page
permalink: /research/
title: Research
description: 
nav: true
---

Under construction...

## Interests

- **Statistical inference for networks:** latent space models, community detection, spectral graph inference.
- **High-dimensional data analysis:** variable selection, dimensionality reduction, covariance estimation, convex optimization.
- **Statistical machine learning and pattern recognition:** classification, regression, clustering, graph matching.
- **Applications to neuroimaging:** statistical connectomics.

## Overview

I am interested in the statistical, theoretical and computational aspectsof methodologies for problems that arise in "big-data", particularly the ones involving *complex and high-dimensional datasets*. My research focuses on developing new tools to extract meaningful information from large and complex datasets, with focus on network data, including topics such as statistical modeling and machine learning forgraphs, spectral graph inference, and pattern recognition for networks.

- Developing new statistical methodologies for complex and high-dimensional data to make*interpretable* and efficient inferences* by exploiting low-dimensional structures in the data.

- Constructing computationally efficient and robust algorithms for large-scale data analysis, in particular through *spectral methods and convex optimization*.

- Studying the theoretical aspects of the above problems within a formal statistical framework to *quantify uncertainty* and to better *understand their non-asymptotic performanceand limitations*.

- Algo de aplicaciones



<details>
<summary> Network analysis (<i>click to expand</i>) </summary><p>

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid" src="{{ '/assets/img/FB-SPCA.jpg' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid" src="{{ '/assets/img/FB-latentpositions-laplacian.png' | relative_url }}" alt="" title="example image"/>
    </div>
</div>


**Selected publications**

* **Overlapping community detection in networks via sparse spectral decomposition**<br>
**Jesús Arroyo**, Elizaveta Levina<br>
*Sankhya A (Special Issue on Network Analysis), accepted pending minor revisions (2020)*<br>
[[preprint]](https://arxiv.org/abs/2009.10641)[[code]](https://github.com/jesusdaniel/spcaCD)

* **Inference for multiple heterogeneous networks with a common invariant subspace**<br>
**Jesús Arroyo**, Avanti Athreya, Joshua Cape, Guodong Chen, Carey E. Priebe, Joshua T. Vogelstein<br>
*Journal of Machine Learning (2020), to appear.*
 (2019). <br>
[[preprint]](https://arxiv.org/pdf/1906.10026.pdf)[[R code]](https://github.com/jesusdaniel/mase)[[Python code]](https://graspy.neurodata.io/reference/embed.html#multiple-graph-embedding)

* **Joint embedding of graphs**<br>
Shangsi Wang, **Jesús Arroyo**, Joshua T. Vogelstein, Carey E. Priebe<br>
*IEEE Transactions on Pattern Analysis and Machine Intelligence (2019).*<br>
[[journal]](https://ieeexplore.ieee.org/abstract/document/8889404/). 

* **Multiple Network Embedding for Anomaly Detection in Time Series of Graphs**<br>
Guodong Chen, **Jesús Arroyo**, Avanti Athreya, Joshua Cape, Joshua T Vogelstein, Youngser Park, Chris White, Jonathan Larson, Weiwei Yang, Carey E Priebe<br>
[[preprint]](https://arxiv.org/abs/2008.10055)

</p></details>




<details>
<summary>  Statistical Machine Learning (<i>click to expand</i>)</summary> 

Modern high-dimensional settings in statistics and machine learning are often concerned withvariable selection or regularization approaches to reduce the dimension of the problem andto discover meaningful associations between variables. These tasks become more challengingin complex datasets with additional multi-scale structure in the variables, such as networks,tensors or multimodal data. The structure of those datasets often results in strong correlationsand higher-order interactions between variables, which complicate the performance of existingtools, both theoretically and practically. Ecient and scalable algorithms are important toaddress these challenges in big data. As part of my research, I have worked in developingnew techniques to study these problems by introducing novel methodologies that deal with thecomplexity of the data eectively, resulting in improved theoretical and practical performance

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid mx-auto d-block" src="{{ '/assets/img/fMRI-classification.png' | relative_url }}" alt="Graph classification" title="Graph classification"/>
    </div>
</div>
<div class="row justify-content-sm-center">
    <div class="col-sm-4 mt-3 mt-md-0">
        <img class="img-fluid" src="{{ '/assets/img/fMRI1.png' | relative_url }}" alt="" title="example image"/>
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        <img class="img-fluid" src="{{ '/assets/img/Brain_network_steve_ind27_s.png' | relative_url }}" alt="" title="example image"/>
    </div>
</div>

**Selected publications**

* **Network classification with applications to brain connectomics**<br>
**Jesús D. Arroyo Relión**, Daniel Kessler, Elizaveta Levina, Stephan F. Taylor<br>
*The Annals of Applied Statistics, (2019) 13(3), 1648-1677.*<br>
[[journal]](https://projecteuclid.org/euclid.aoas/1571277767) 

* **Efficient distributed estimation of inverse covariance matrices**<br>
*Jesús Arroyo*, Elizabeth Hou<br>
*IEEE Statistical Signal Processing Workshop (SSP) (2016)*<br>
[[conference proceedings]](https://ieeexplore.ieee.org/abstract/document/7551705). In 

* **Simultaneous prediction and community detection for networks with application to neuroimaging**<br>
**Jesús Arroyo**, Elizaveta Levina<br>
[[preprint]](https://arxiv.org/pdf/2002.01645.pdf)[[code]](https://github.com/jesusdaniel/glmblock)


</details>

<details>
<summary>  Pattern Recognition (<i>click to expand</i>)</summary><p> 

Identifying patterns or similarities between nodes in a graph is an important task inthe study of network data. 

*Graph matching* is the problem of finding a meaningful correspondence between the nodes of two or more networks, and has applications rangingfrom neuroscience, image processing or data security. Part of my work has focused in studying this problem from a statistical framework, by developing flexible and tractable statistical models, and .

<div class="row justify-content-sm-center">
    <div class="col-sm mt-3 mt-md-0">
        <img class="img-fluid w-50 mx-auto d-block" src="{{ '/assets/img/GM-problem.png' | relative_url }}" alt="Graph matching problem" title="Graph matching problem"/>
    </div>
</div>

### Selected publications

* **Maximum Likelihood Estimation and Graph Matching in Errorfully Observed Networks**<br>
*Jesús Arroyo*, Daniel L. Sussman, Carey E. Priebe, Vince Lyzinski<br>
*Journal of Computational and Graphical Statistics (2020), to appear.*<br>
[[preprint]](https://arxiv.org/pdf/1812.10519.pdf) [[code]](https://github.com/dpmcsuss/gmmle)
* **Graph matching between bipartite and unipartite networks: to collapse, or not to collapse, that is the question**<br>
**Jesús Arroyo**, Carey E. Priebe, Vince Lyzinski<br>
[[preprint]](https://arxiv.org/abs/2002.01648)


</p></details>
