> This is the folder where my customized files are stored

# Install

## Prep

1. Install conda<br>
    miniconda vs anaconda<br>
    - miniconda is the bare minimum version, while anaconda comes with many packages pre-installed.
    - add conda to path despite the warning
    - uninstall and reinstall conda if httperrors encountered during conda use.
2. Install CUDA
3. Install [PyTorch](https://pytorch.org/get-started/locally/)
   ![pytorch_install](pics/pytorch_install.png)
4. Git clone tortoise-tts repository <br>
5. Prep Conda Env<br>
    1. create env with default python as the starting point.<br>
        `conda create -n TorToiSe python`
    2. activate env<br>
        `conda activate {cutom_env_name}`
    3. run `pip3 install -r requirements.txt` to install dependencies.
    4. Do NOT run `python setup.py install`, as this would install tortoise as a global module in your machine which might not be what you want.
    5. Use pip install missing packages if any during the normal usage.
    6. While in env, test out tts to install other missing dependencies.
    `python tortoise/do_tts.py --text "I'm going to speak this" --voice random --preset fast`
    7. When all dependencies are installed, export the env to yml file for future use in other machines.<br>
        `conda env export > environment.yml`
