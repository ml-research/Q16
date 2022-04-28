# Can Machines Help Us Answering Question 16 in Datasheets, and In Turn Reflecting on Inappropriate Content?

> **Can Machines Help Us Answering Question 16 in Datasheets, and In Turn Reflecting on Inappropriate Content?**
>
> Patrick Schramowski, Christopher Tauchmann, Kristian Kersting
>
> Abstract: Large datasets underlying much of current machine learning raise serious issues concerning inappropriate content such as offensive, insulting, threatening, or might otherwise cause anxiety. 
This calls for increased dataset documentation, e.g., using datasheets. They, among other topics, encourage to reflect on the composition of the datasets. So far, this documentation, however, is done manually and therefore can be tedious and error-prone, especially for large image datasets.
Here we ask the arguably "circular" question of whether a machine can help us reflect on inappropriate content, answering Question 16 in Datasheets.
To this end, we propose to use the information stored in pre-trained transformer models to assist us in the documentation process.
Specifically, prompt-tuning based on a dataset of socio-moral values steers CLIP to identify potentially inappropriate content, therefore reducing human labor. We then document the inappropriate images found using word clouds, based on captions generated using a vision-language model.
The documentations of two popular, large-scale computer vision datasets---ImageNet and OpenImages---produced this way suggest that machines can indeed help dataset creators to answer Question 16 on inappropriate image content.

<a href="https://arxiv.org/abs/2202.06675"><img src="https://img.shields.io/badge/arxiv-2202.06675-red" height=22.5></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" height=22.5></a>

<img src="docs/inapp_concepts.jpg" width="800px">

## Getting Started
### Installation
1. Create a virtual environment and install required packages via: 
```
pip install requirements.txt
```
2. For the image description generation clone the repo https://github.com/Aleph-Alpha/magma and follow the installation instructions.

3. In /data we provide the learned model parameters (prompts.p) for three different CLIP variants. By default the largest, more recently released, variant is used (ViT-L/14). To reproduce the paper results please use ViT-B/16. 
### Image classification

- To classify inappropriate image content run
```
python main/clip_classifier/classify/inference_images.py --input_folder <path/to/images> --output_folder <path/output>
```
The script will search for files with the following suffix and directory structure: '/&ast;.JPEG', '/&ast;.png', '/&ast;.jpg', '/&ast;/&ast;.JPEG', '/&ast;/&ast;.png', '/&ast;/&ast;.jpg'. If you need other data types you can apply changes on the *find_images* method located in *main/paper_experiments/experiments.py*.

- If you already computed the CLIP embeddings you can use the package *embedding-reader* (https://github.com/rom1504/embedding-reader) via 
```
pip install embedding_reader
```
and run

```
python main/clip_classifier/classify/inference_embeddings.py --input_folder <path/to/images> --output_folder <path/output>
```


### Content documentation
1. caption generation

#### (copied from https://github.com/Aleph-Alpha/magma/blob/master/example_inference.py):
2. word cloud generation

### Reproducibility
TODO

## Citation
If you use this code for your research, please cite the following:
```
@inproceedings{schramowski2022can,
  title={Can Machines Help Us Answering Question 16 in Datasheets, and In Turn Reflecting on Inappropriate Content?},
  author={Patrick Schramowski and Christopher Tauchmann and Kristian Kersting},
  booktitle = {Proceedings of the ACM Conference on Fairness, Accountability, and Transparency (FAccT)},
  year={2022}
}
```

### TODOS

- wordcloud computation
- notebooks
- train and validate on smid