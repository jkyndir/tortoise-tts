> This is the folder where my customized files are stored

# Install

## Prep

1. Install conda<br>
    miniconda vs anaconda<br>
    - miniconda is the bare minimum version, while anaconda comes with many packages pre-installed.
    - add conda to path despite the warning
    - uninstall and reinstall conda if httperrors encountered during conda use.
2. Git clone tortoise-tts repository <br>

## Env Setup

One can either manually setup the env or recreate the env from the yml file with one line.

- Manually Set Up Conda Env<br>
    1. create env with default python as the starting point.<br>
        `conda create -n tts python`
    2. activate env<br>
        `conda activate {cutom_env_name}`
    3. run `pip install -r kyndir/requirements.txt` to install dependencies.<br>
        Note to use the requirements.txt in my folder (copied from setup.py), not the one in the root folder to avoid mistakes.<br>
        Note: Do NOT run `python setup.py install`, as this would install tortoise as a global module in your machine which might not be what you want.
    1. Install [PyTorch](https://pytorch.org/get-started/locally/)<br>
    ![pytorch_install](pics/pytorch_install.png)<br>
    `conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia`<br>
    Note that there's no need to download and install CUDA manually, since conda is gonna do that for you.
    1. Use pip install missing packages if any during the normal usage.
    2. While in env, test out tts to install missing models if any.<br>
    `python -m tortoise.do_tts --text "I'm going to speak this" --voice random --preset fast`<br>
    Note that one should run these files as modules in the root of this repository so that it will be used as one of the sys.path when python searches modules for imports.
    1. When all dependencies are installed, export the env to yml file for future use in other machines.<br>
        `conda env export > kyndir/environment.yml`<br>
        Note that some redundant pip package install requirements are manaully removed and only essential ones are kept in the yml file, so that pip subprocess error can be avoided in the conda env creation from the yml file.
- Recreate Env from the yml file<br>
   `conda env create -f kyndir/environment.yml`
