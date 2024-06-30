# HospitalLogSPCModels

This repository contains all material produced during the writing of the "Evaluation of Subpopulation Process Comparison Techniques for Process Mining" Bachelor Thesis (University of Twente, Technical Computer Science, 2023/24).

## Code

### token.py
Enhanced token-based replay implementation via the PM4Py library. Using the relevant subpopulation files (logs and models), it outputs the results of enhanced token-based replay.

### timestamp.py
File containing processing code which adds to every event in a log an incrementing timestamp. Utilised when logs had missing timestamps (since they are a requirement for the token-based replay function). The timestamps had no effect on the analysis other than indicating the events in the log occurred in the same order as that in which they're registered.

## Subpopulations

### M16/M14
Folders containing all data describing a particular subpopulation based on the diagnosis code. Either M16 (ovarian cancer) or M14 (cancer of the corpus uteri).

### Length Filtered
- **"... Filtered for trace length (X-Y) ..."**: File containing (or referring to in the case of models) only traces which have a length between X and Y inclusive.

### Age Filtered
- **"... under/ over X ..."**: File containing (or referring to in the case of models) only traces which describe the treatment path of a patient with the age higher/lower than X.

### Inductive Visual Miner Models
- **"... (0675 0325) ..."**: Model mined using Inductive Visual Miner using the 0.675 value for the activity slider and 0.325 value for the paths slider.

### No Empty Traces
- **"... no empty traces..."**: File containing (or referring to in the case of models) only traces that are not empty, i.e., which have more than one event.

### No Big Skips
- **"... no big skips..."**: Models which have been processed so that they don't contain a transition directly from the start node to the end node. Such "big skips" might skew results of conformance checking and thus have been removed where necessary.

---

Feel free to reach out to a.victor.alecu@gmail.com for any questions or further information regarding this research.
