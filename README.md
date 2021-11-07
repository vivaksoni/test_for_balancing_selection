# test_for_balancing_selection

#Updated on Nov 07th, 2021

This is the list of files included for the manuscript titled "A new test of balancing selection and its application to data from humans" by Soni et al., which can be found here - https://www.biorxiv.org/content/10.1101/2021.02.08.430226v2 . Contact vsoni@sussex.ac.uk for questions.

S1.xlsx // Supplementary file S1, containing results of the GO category analysis.

S2.xlsx // Supplementary file S2, containing results of the Gene level analysis.

coding_snps_freqs.zip // Zipped tab-delimited file of human polymorphism data from 1000 genomes Grch37 build. Only stop lost, stop gain, synonymous and missense polymorphisms are included.

data_analysis.ipynb // Jupyter script to calculate Z for each of the superpopulations from the file coding_snps_freqs.txt

get_z_table.py // Python script to calculate Z for MAF categories from simulation output.

simple_demography.slim // SLiM script to run simulations under vicariance or dispersal scenarios.

simple_demography.slim // SLiM script to run simulations under vicariance or dispersal scenarios, with a single balanced polymorphism inserted into the middle of the simulated region.
