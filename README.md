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

### Image classification
TODO

### Content documentation
1. caption generation

#### (copied from https://github.com/Aleph-Alpha/magma/blob/master/example_inference.py):
```
from magma import Magma
from magma.image_input import ImageInput

temperature = 0.4

model = Magma.from_checkpoint(
    config_path = "configs/MAGMA_v1.yml",
    checkpoint_path = "./mp_rank_00_model_states.pt",
    device = 'cuda:0'
)

inputs =[
    ## supports urls and path/to/image
    ImageInput('https://www.art-prints-on-demand.com/kunst/thomas_cole/woods_hi.jpg'),
    'Describe the painting:'
]

## returns a tensor of shape: (1, 149, 4096)
embeddings = model.preprocess_inputs(inputs)  

## returns a list of length embeddings.shape[0] (batch size)
output = model.generate(
    embeddings = embeddings,
    temperature = temperature
)  

print(output[0]) ##  A cabin on a lake
```

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