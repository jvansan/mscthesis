# Do non-redox active metal cations have the potentials to behave as chemo-protective agents? The Effects on Metal Cations on HAT Reaction Barrier Heights

## Introduction

* Metal cations in biological systems
  - Metals in protein have been studied extensively, and an active crystaligrophic database for protein structures w/ metal is kept\cite{Hsin2006}
  - Metals are present in ~40% of protein structures in PDB\cite{Harding2010, Berman2007}
  - Redox active metals often associated with catalytic activity as co-factors
  - Non-redox active metal cations ubiquitous in biochemical structures
    + Important in protein structures and function (Cite cellular biology textbook\cite{Karp1999})
    + Non-redox active metal cations bond predominantly through electrostatic intreactions
    + Bind predominantly to O centres in metals \cite{Harding1999, Harding2001}
    + Divalent ions tend to bind to protein directly (Ca 4-6 binding sites Mg 1-2 binding sites -> others occupied by water)
    + Monoionic ions tend to be solvated heavily but appear in solvent cavities of proteins (some bind to carbonyl or carboxylates)\cite{Harding2010}
  - Borrow information from studies of Hofmeister series
    + "spectroscopic experiments and molecular simulations show that biologically relevant ions can strongly influence only their immediate solvation shell and do not show any long-range kosmotropic effects in water"\cite{Omta2003, Funker2011}
    + "Cations Bind Only Weakly to Amides in Aqueous Solutions"\cite{Okur2013}
      * No experimental evidence of Na+ or K+ binding in aqua
    + Radial distribution function for Na/K w/ NMA in aq\cite{Heyda2009}
  - Table of ionic concentrations inside mamallian cells (M. C.) and in blood (Units of mM)\cite{Karp1999, Milo2015} (http://book.bionumbers.org/what-are-the-concentrations-of-different-ions-in-cells/)

<center>

| Ion  |  M. C.             |  Blood  |
|------|--------------------|---------|
| K+   |        100         |    4    |
| Na+  |         10         | 100-200 |
| Mg2+ | 10(bound) 0.5(free)|    1    |
| Ca2+ |      0.01-0.1      |    2    |
</center>

* Experimental (and past theoretical) evidence for inhibition of reactivity
  - Recent experimental evidence for metal cation inhibit of HAT reactions b/w CumO* and organic substrates in MeCN at 298 K
  - First paper for CHD, THF, TEA, PMP \cite{Salamone2013a}
  - Second paper for DMF and DMA \cite{Salamone2015metals} (previously w/o metals\cite{Salamone2013})
  - Third paper bulky acetamides/alkanamides \cite{Salamone2016} (previously w/o metals\cite{Salamone2014})
  - Solvent hydrogen bond donation to amide/amine destabilises TS by decreasing electron density at incipient radical (DMSO worse hydrogen bond donor than MeCN)\cite{Salamone2015metals}
  - Metal cations w/ simple amides shown three-distinct regions of HAT reactivity: $k_{0}$ = full deactivation (only CumO beta-scission), $k_{H1}$ = moderate deactivation, $k_{H2}$ = minor deactivation

<center>

| Substrate  | Conditions        | $k_H$ ($M^{-1}s^{-1}$)|
|------------|-------------------|-----------------------|
| CHD        |                   | 6.7 $\times 10^7$     |
|            | LiClO4 1.0 M      | 7.5 $\times 10^7$     |
|            | Mg(ClO4)2 1.0 M   | 7.0 $\times 10^7$     |
| THF        |                   | 5.7 $\times 10^6$     |
|            | LiClO4 1.0 M      | 2.9 $\times 10^6$     |
|            | LiOTf 1.0 M       | 2.8 $\times 10^6$     |
|            | Mg(ClO4)2 1.0 M   | 1.8 $\times 10^6$     |
| TEA        |                   | 2.0 $\times 10^8$     |
|            | LiClO4 1.0 M      | 9.4 $\times 10^7$     |
|            | Mg(ClO4)2 0.005 M | $< 1 \times 10^6$     |
| PMP        |                   | 1.7 $\times 10^8$     |
|            | LiClO4 1.0M       | 9.0 $\times 10^7$     |
|            | Mg(ClO4)2 0.005 M | $< 1 \times 10^6$     |
| DMF        |                   | $1.2 \times 10^6$     |
|            | DMSO              | $2.5 \times 10^6$     |
| DMA        |                   | $1.2 \times 10^6$     |
|            | DMSO              | $2.4 \times 10^6$     |
| DIA        |                   | $3.1 \times 10^5$     |

![DMF/DMA w/ Li](../figures/Amide-Li.png)
![DMF/DMA w/ Na](../figures/Amide-Na.png)
![DMF/DMA w/ Mg](../figures/Amide-Mg.png)
</center>

* Several questions
  - What is the exact physico-chemical nature of C-H bond deactivation in amides?
    + Does binding actually decrease BDE?
    + How do metals effect polarity of TS complex?
    + Does structures of substrate effect ability of deactivation (DIA)
    + How do metal cations effect RO* reactions w/ of solvent molecules used in LFP (DMSO/HMPA)?  
    + Do we observe the same reactivity w/ biologically relevant HO*? ()
  - How well does DFT capture effects of metal cation binding?
    + Do we need counteranion? And does Cl- vs ClO4- matter?
    + Test case: unimolecular decay of CumO*



## Benchmarking DFT for metal cation substrate/radical binding

* Need to "calibrate" DFT-based methods before applying to unknown systems
* Previous studies w/ binding energies
  - Binding Energies Ca2+ with organic substrates\cite{Corral2003, Suarez2011}
  - Binding Enthalpies for Na+ and K+ w/ amides\cite{Siu2001} (Also expt \cite{Klassen1996})
  - Only studied several DFT methods and small variety in substrates
* One other previous study w/ relative conformer energies for Li+ binding to dipeptide models \cite{Baldauf2013}
* Wanted to study dipeptide models
  - Account for different amino acid side chains
  - Computational restrictions of CCSD(T) calculations did not allow for this
  - Still intent to perform these calcs w/ new computers
* Use small models for biomolecules, solvents used in kinetics studies, and radicals

### Methods
* Basis set convergence of metal cations!
* Final method CCSD(T)-F12*/Def2-QZVPPD
* Results - Metal cations approach CBS limit - verify w/ expt

### Results

* Table of CCSD(T)-F12*/Def2-QZVPPD Gas Phase Binding Energies

<center>

|             |   Li+  |   Na+   |    Mg++  |    K+   |   Ca++  |
|-------------|--------|---------|----------|---------|---------|
| H2O         | -34.65 |  -24.38 |  -81.95  |  -17.78 |  -56.80 |   
| NH3         | -39.93 |  -28.16 |  -98.12  |  -19.78 |  -65.34 |
| MeCN        | -44.44 |  -33.01 |  -113.08 |  -24.94 |  -80.72 |
| Formamide   | -50.69 |  -36.89 |  -128.19 |  -28.45 |  -96.05 |
| Formic Acid | -38.38 |  -26.99 |  -101.92 |  -19.96 |  -72.64 |
| HO          | -21.32 |  -16.81 |  -56.97  |  -12.40 |  -40.66 |
| HOO         | -27.12 |  -19.05 |  -72.15  |  -13.91 |  -48.95 |

</center>

* DFT Results - does basis set matter for binding? (Convergence of metals to CBS)

## Effects of metal cations on HAT reactions

### Methods
* On basis of benchmark and QM-ORSA
  - M05-2X/6-31+G** gas-phase optimisations
    + Attempted solvent phase optimisations, but many calculations failed
  - M05-2X/6-311+G(2d,2p) single point in continuum solvent SMD=MeCN to estimate solvent effects

### Can DFT be used to capture unimolecular decay of CumO* w/ metals?
* Main decay path of CumO* (as in BDE Ch.) = CumO* -> Acetophenone + CH3* ($k_\beta = 6.3 \times 10^5 s^{-1}$ \cite{Avila1993, Avila1995} in MeCN @ 298 K)
* Interaction w/ O* results in increase in beta-scission rate -> stabilises TS complex relative to Complex b/c stronger interaction w/ more sp2-like O than sp3
* Exptl (Dependent on Conc. M+) for 1.0M of three salts: LiClO4 ($k_\beta = 1.8 \times 10^6 s^{-1}$), Mg(ClO4)2 ($k_\beta = 1.6 \times 10^6 s^{-1}$), NaClO4 ($k_\beta = 1.1 \times 10^6 s^{-1}$)
* Results: M05-2X-SMD/6-311+G(2d,2p)//M05-2X/6-31+G**

|   Species    |  $k_H$ (Calc)      | $\Delta \Delta G^\ddagger$ |
|--------------|--------------------|----------------------------|
|  TS          |  $2.7 \times 10^5$ |   0.0                      |
|  TS-Na       |  $7.8 \times 10^7$ |  -3.4                      |
|  TS-Mg       |  $5.2 \times 10^6$ |  -1.8                      |
|  TS-Na-ClO4  |                    |                            |
|  TS-Na-Cl    |  $1.8 \times 10^7$ |                            |
| TS-Mg-(ClO4)2|  N/A               |                            |
|  TS-Mg-Cl2   | $2.1\times10^{12}$ |  -9.4                      |          
* Some problems with results

### Does non-redox active metal cation binding decrease BDE
*
