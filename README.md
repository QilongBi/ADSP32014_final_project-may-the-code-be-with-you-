## Project Name:
Comparing U.S. household disaster preparedness across natural hazard risks: A Hierarchical Bayesian Item Response Theory (IRT) analysis of protective motivation and sociodemographic factors
## Group Member: 
Qilong Bi; Yunhao"Jairus"Jia
## Project Summary:
Understanding how households prepare for different types of natural hazard risks is critical for effective and inclusive disaster risk reduction (DRR). This study investigates the variations in U.S. household disaster preparedness across five major risk types based on nationally representative data from the 2023 FEMA National Household Survey (NHS).
Conceptual Framework
We develop a “predictability–destructiveness” typology to classify risk types and integrate Protection Motivation Theory (PMT) to examine the cognitive and sociodemographic mechanisms behind preparedness behaviors.
Methodology
To address gaps in cross-risk comparison and the limitations of traditional additive measures, we employ a Hierarchical Bayesian Item Response Theory (IRT) model, allowing us to account for the latent difficulty of specific preparedness actions.
Key Findings
1. **Consistency Across Risks**  
   Although preparedness actions differ in difficulty, overall preparedness levels remain relatively consistent across risk types.

2. **Coping Appraisal Dominance**  
   Coping appraisal emerges as a consistent and significant predictor of preparedness (CIs>0, PDs=1), while the effect of threat appraisal is limited.

3. **Heterogeneous Socioeconomic Effects**  
   Sociodemographic factors such as education and income show heterogeneous effects depending on the risk types—particularly for wildfire and riverine flood—while other variables, including gender and rurality, have minimal impact in certain risk contexts.

Implications
These findings highlight the importance of tailored, risk-specific DRR strategies and suggest the value of integrating interdisciplinary theory with context-specific measurements to assess and support household resilience more accurately in multi-hazard environments.

## Project details:
Because all of our work—including computation, visualization, and modeling—was executed directly on UChicago’s Midway cluster rather than in Jupyter Notebook, we were unable to submit step-by-step Jupyter code as instructed. To compensate, we consolidated all visualizations, methodological details, and final model outputs into a comprehensive written analysis. All results and discussion can be found in the accompanying file: `final_report.docx`.
Our project was implemented using two programming languages. All preprocessing, preliminary model inference, and visualization of outputs were conducted in R, with relevant script files located in the `code` directory, specifically `Natrual_hazard.Rproj` and `natural_harard.qmd`. For the final model estimation, we transitioned to Python to better leverage the Midway cluster, with core model code contained in `fancy_model.py`, resulting model output in `fitted_model_correct.csv`, the multithreaded workflow submitted through `job.sbatch`, and the cluster’s computation output recorded in `final_correct.out`. Due to GitHub’s file size limitations, we did not upload all intermediate files (such as failed or erroneous model runs), and we also did not embed detailed explanatory comments within the code. All methodological reasoning and model interpretation are thoroughly documented in `final_report.docx`.


