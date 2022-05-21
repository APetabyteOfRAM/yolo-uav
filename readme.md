# YOLO-Fine



## Keras (TF Backend) implementation of YOLO-Fine
#### Read the paper: https://doi.org/10.3390/rs12152501
<br />
<img src="./imgs/00000674_co.png" alt="674" width="300"/>
<img src="./imgs/674.png" alt="674_detect" width="300"/>

<br />

## What is YOLO-Fine?
YOLO-Fine[[1]](#1) is a novel one-stage detector for detecting and classifying small vehicles from aerial and satellite imagery.

<br />

## Our dataset
We trained YOLO-Fine[[1]](#1) on the VEDAI (https://downloads.greyc.fr/vedai/) dataset. Anchors were generated using k-means clustering, and can be found in the *./vedai_anchors.txt* file. Classes were set to 0 to focus on bounding box classification.

<br />

## Usage:

### Use with sample weights:
Run *./yolo_image.py*
```
python ./yolo_image.py
```

<br/>

## Train on your dataset:


Modify train.py with your:

* Annotations file
* Anchors file 
* Classes file
* Input shape
* Training epochs
* Target batch size

Then run *./train.py*

Note that the model will train with the darknet body frozen, and will then unfreeze those layers and continue training.
```
python ./yolo_image.py
```
<br />

## Acknowledgments
We would like to thank the authors of the originial YOLO-Fine paper as well as @pjreddie and @qqwweee.

<br />

## References
<a id="1">[1]</a> 
Pham, Minh-Tan et al. “YOLO-Fine: One-Stage Detector of Small Objects Under Various Backgrounds in Remote Sensing Images.” Remote Sensing 12.15 (2020): 2501. Available: http://dx.doi.org/10.3390/rs12152501.