# Extracting Kds from FACS + deep sequencing data published in Chevalier et al. 2017

## File descriptions

### Notebooks

* `iSee_analysis.ipynb` - Analysis of Mutations from the iSEE database to construct a *prior* $P(\Delta \log_{10}K_d)$.

* `Infer_Kds.ipynb` - Round 1 of Kd inference by MCMC sampling: 1M steps, dlog10Kd = 0.3 n_move = 5, P_acc ~ 0.34  

* `Infer_Kds_round2.ipynb` - Rounds 2 and 3 of inference ...

  * Round 2: 1M steps, dlog10Kd = 0.1, n_move = 20, P_acc < 0.1
  * Round 3 (production run): 10M steps, dlog10Kd = 0.05, n_move = 20, P_acc ~ 0.053

* `plot_round2_20230914_distribution.ipynb` - plotting the data for Figure 5 of the main text

### Input files

* `06_HighThroughputDesign_FluH1_Gen2_relax.dat` - sequencing data from Chevalier et al. 2017
* `A8_sequence.afasta` - WT sequence for A8
* `A13_sequence.afasta` - WT sequence for A13 
* `A18_sequence.afasta` - WT sequence for A18 

### Output files

log10_Kd estimates after Round 1: 
* `A8_initial_Log10Kd_estimates_20230913.csv`
* `A13_initial_Log10Kd_estimates_20230913.csv`
* `A18_initial_Log10Kd_estimates_20230913.csv`

log10_Kd estimates after Round 2: 
* `round2_Log10Kd_estimates_20230913.csv`

log10_Kd estimates and traj data after Round 3: 
* `round2_Log10Kd_estimates_20230914.csv`
* `round2_steps_traj.npy`
* `round2_u_traj.npy`


## Reference

Chevalier, Aaron, Daniel-Adriano Silva, Gabriel J. Rocklin, Derrick R. Hicks, Renan Vergara, Patience Murapa, Steffen M. Bernard, et al. “Massively Parallel de Novo Protein Design for Targeted Therapeutics.” Nature 550, no. 7674 (October 2017): 74–79. https://doi.org/10.1038/nature23912.



