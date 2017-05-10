# Interrogation of BEP Principle

## Introduction

* BEP Principle
  - Origins
  - Common uses and examples
* BDEs are important
  - What is a BDE
  - How are BDEs measured
    + How good at these BDEs?
    + How is theoretical treatment better
  - BDEs and HAT reaction
    - All rxns studying here are exothermic CumO-H bond strength greater than all C-H bonds
* Problem statement
  - No recipe for how generally applicable BEP is
* Statement of research
  - Probe applicability using combination of experimental and theoretical results
    + Interested in HAT reactions involving C-H bonds primarily
      * Relates to biological systems
    + Can we use BEP to study relate C-H HAT reactions?
      * Do all rxns fall on single line? NO
      * Is there two general correlations?
        - Appears to be two:
        1) Allylic / Benzylic species
        2) All other species
    - First requires determination of accurate computational procedure usable for large molecule BDEs

## Methods
* Experimental data collected from literature
  - Experimental HAT rate constants are all for CumO* + R-H measured in MeCN with LFP
  - Several different sources
  - Uncited data provided by Massimo Bietti (298K in MeCN by CumO decay trace induced by LFP)
  - Literature BDEs from Luo2002
* Computational Methods - all done in g09
  - Composite procedures
    + W1BD - high level - very computationally expensive
    + CBS
      * QB3 and RO - QB3
      * APNO
    + G4 and G4(MP2)
    + LDBS approach
  - TS calculations - all species tried open and cisoid starting points
    + B3LYP-D3(BJ)/6-31+G* optimisation and frequencies
      * some structures have small imaginary frequiencies which I could not eliminate -> estimate of TS structures
    + LC-wPBE-D3(BJ)/6-311+G(2d,2p) SP
      * B3LYP prone to delocalisation error but gives reasonable geometries

## Results/Discussion
  * Comparison of computational methods
    - W1BD only possible for subset of species (too expensive)
    - Compare to expt and other composite methods
    - Conclusion: ROCBS-QB3 is best
  * Examine BEP plot
    - Two trends still observed centres with are delocalised and those which are not
    - Delocalised species fall onto single relation with R^2 = 0.89
      * Reasonably well correlated - BEP offers predictive power for rate constants of delocalised species (allylic or benzylic)
      * In line with previous results of Pratt \cite{Pratt2003}
    - Theoretical results for non-delocalised species are poorly correlated (R^2 = 0.63) - even worse than expt
      * Seek explanation for this behaviour by calculating TS structures
