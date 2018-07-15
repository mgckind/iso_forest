# iso_forest

This is a simple package implementation for the isolation forest method described (among other places) in this [paper](icdm08b.pdf) for detecting anomalies and outliers from a data point distribution.

# Extended isolation forest

For an extended version of this algorithm that produces more precise scoring maps please visit this repository

[https://github.com/sahandha/eif](https://github.com/sahandha/eif)/


## Installation

  pip install git+https://github.com/mgckind/iso_forest.git
 
It supports python2 and python3 

## Requirements

No extra requirements are needed, It also contains means to draw the trees created using the [igraph](http://igraph.org/) library.

## Use Examples

See these 2 notebooks examples on how to use it

- [basics](demo_iforest.ipynb)
- [tree visualization and anomaly PDFs](demo_vis_pdf.ipynb)

## Releases 

### v1.0.1

- Initial Release

