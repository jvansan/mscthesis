## Jeffrey van Santen - Master of Science Thesis

Final version of Master of Science Thesis in Chemistry at UBC Okanagan.

Full Text also available online at [UBC cIRcle](https://open.library.ubc.ca/search?q=*&sort=6&circle=y&campus=UBCO&affiliation=Chemistry,%20Department%20of%20(Okanagan)&program=Chemistry&degree=Master%20of%20Science%20-%20MSc).

### Abstract 

Hydrogen atom transfer (HAT) reactions are a fundamental step in many biological processes, but can initiate the free-radical induced oxidation of biomaterials. Although HAT reactions appear fundamentally elementary, there are many poorly understood factors that influence HAT. In this thesis, three aspects of HAT reactivity are investigated using quantum chemical technique.

First, the importance of pre-reaction complex formation in considering the kinetics of HAT reactions was investigated. For a set of nearly-thermoneutral HAT reactions involving oxygen-centred radicals, the relationship between pre-reaction complex non-covalent binding energies and Arrhenius pre-exponential factors (A-factors) is investigated. It is demonstrated that for HAT reactions that take place through similar mechanisms, there is a strong correlation between pre-reaction complex binding energies and A-factors. This suggests that non-covalent interactions may directly affect the kinetics of certain HAT reactions.

Next, the relationship between bond dissociation energies (BDEs) and reaction rates for abstraction of a hydrogen from a C-H bond by the CumO radical are investigated in the context of the Bell-Evans-Polanyi (BEP) principle. The applicability of the BEP principle is examined by exploring a hypothesis: If the BEP principle is a valid linear free-energy relationship, there should exist two linear relationships for BDE against the logarithm of HAT rate constant, one for incipient radicals that are allylic or benzylic, and one for alkyl radical. It is demonstrated that there is a reasonably strong correlation for allylic/benzylic C-H bonds, however not for alkyl ones. The BEP principle should not be used for quantitative prediction, however it remains useful as a conceptual framework.

Finally, the effect of non-redox active metal cations on HAT reactions involving small models for proteins and oxygen-centred radicals is studied. Previous experimental evidence demonstrated that Lewis acid-base interactions between metal cations and substrates can inhibit HAT reactions, and that the cations may serve as a form of chemo-protection in biological systems. The results herein demonstrate that metal-substrate interactions can deactivate certain C-H bonds, however metal-radical interactions may promote HAT reactions. On the basis of these limited results, non-redox active metal cations may not act as natural chemo-protective agents.


### Template Details
June 2, 2013 by Yves Lucet

To produce a thesis WITHOUT index and glossary use ubc_2010_spring_doe_jane.tex
To produce a thesis WITH index and glossary use ubc_2010_spring_doe_jane-index-glossary.tex 

NOTE: The template works with pdflatex NOT with latex. If you use .eps
pictures and compile with latex .tex->.dvi->.ps->.pdf the template is
currently not compiling i.e. you are on your own.

The followings need separate tools to be setup:
- bibliography: bibtex
- index: makeindex [optional]
- glossary: makeglossaries [optional]
These tools are installed with any LaTeX distribution.

If you use TeXnicCenter, makeindex and bibtex are already
setup. makeglossaries is easily added. See instructions at

http://www.latex-community.org/index.php?option=com_content&view=article&id=263%3Aglossaries-nomenclature-lists-of-symbols-and-acronyms&catid=55%3Alatex-general&Itemid=112

There is an ERROR in the instructions: - use makeglossaries.exe in
C:\Program Files\MiKTeX 2.9\miktex\bin\x64 - the option is "%tm" NOT
"%bm" - on my installation makeindex crashes TeXNicCenter so I put it
in the postprocessing (executable makeindex; Arguments: "%tm.idx" -t
"%tm.ilg" -o "%tm.ind"); This comes after the Glossary postprocessor
(Executable makeglossaries; Arguments: %tm) Afterwards it all works!

As for writing properly, note the following on correctly formatting tables:
http://www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf
