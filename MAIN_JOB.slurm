#!/usr/bin/bash #sbatch -J Bilby_Job
#SBATCH --ntasks=1 --cpus-per-task=4 --constraint=hasw
#SBATCH --time=4:00:00
#SBATCH --output=%x-%j.out
#SBATCH --mem=4G
#SBATCH --nodes=1

module purge
module load anaconda3/2026.7
conda activate bilby-env

python ./examples/gw_examples/data_examples/GW150914.py #script ur running