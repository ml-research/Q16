import fire
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import fsspec
from main.paper_experiments.experiments import run_model_imagefolder
from argparse import Namespace


clip_model_name = 'ViT-L/14'
prompt_path = f'results/{clip_model_name.replace("/", "-")}/prompts.p'


def main_imagedataset(input_folder, output_folder):
    """main function"""
    fs, relative_output_path = fsspec.core.url_to_fs(output_folder)
    fs.mkdirs(relative_output_path, exist_ok=True)

    args = Namespace(
        language_model='Clip_'+clip_model_name,
        model_type='sim',
        prompt_path=prompt_path,
        only_inappropriate=True,
        input_type='img',
    )
    run_model_imagefolder(args, input_folder, output_folder)


if __name__ == '__main__':
    fire.Fire(main_imagedataset)
