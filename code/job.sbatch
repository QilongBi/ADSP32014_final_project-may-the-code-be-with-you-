#!/bin/bash
#SBATCH --job-name=fancy_modele2
#SBATCH --output=qiuqiule.out
#SBATCH --error=qiuqiule.err
#SBATCH --account=macs30123
#SBATCH --partition=caslake
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00

module load python/anaconda-2022.05
source activate bambi_env

python fancy_model_corr.py

