#!/bin/bash

# install miniconda if it doesn't exist
if ! command -v conda &> /dev/null
then
    echo "conda command not found, installing miniconda3"
    curl -sL "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh" > "Miniconda3.sh"
    bash Miniconda3.sh
    rm Miniconda3.sh
else
    echo "conda command exists, skipping miniconda3 installation"
fi

# source conda
source $(conda info --base)/etc/profile.d/conda.sh

# create and activate conda environment
conda create -n textgen python=3.10.9 -y
conda activate textgen

# install pytorch
pip3 install torch torchvision torchaudio

# clone the repository
if [ ! -d "text-generation-webui" ]; then
    git clone https://github.com/oobabooga/text-generation-webui
fi

# navigate into the cloned directory
cd text-generation-webui

# install the requirements
pip install -r requirements.txt

# print success message
echo "Installation was successful! You can now run the application with the following command:"
echo "conda activate textgen; cd text-generation-webui; python server.py"
