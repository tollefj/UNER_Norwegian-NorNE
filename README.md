# NorNE to UNER

Conversion from NorNE to UNER.
Based on alignment from the UD-Norwegian commits:
- bokmaal: `ccbaec859f3947edf90201c725743b9aa4e7c76c`
- nynorsk: `22c02622958f137314c2335b2a5f088d2b12dba0`

## Run

```bash
python download.py
python convert.py
```

## Stats

output from `uner_code/prepare_data.py`:

```latex
\begin{tabular}{llrrrrrrrrrrrr}
 &  & \multicolumn{4}{r}{docs} & \multicolumn{4}{r}{entities} & \multicolumn{4}{r}{tokens} \\
 & split & dev & test & train & All & dev & test & train & All & dev & test & train & All \\
lang & domain &  &  &  &  &  &  &  &  &  &  &  &  \\
nno & norne & 3048 & 2514 & 24494 & 30056 & 1901 & 1524 & 18449 & 21874 & 49227 & 40692 & 418094 & 508013 \\
nob & norne & 3726 & 3293 & 28697 & 35716 & 2400 & 2253 & 18329 & 22982 & 58027 & 50603 & 445727 & 554357 \\
All &  & 6774 & 5807 & 53191 & 65772 & 4301 & 3777 & 36778 & 44856 & 107254 & 91295 & 863821 & 1062370 \\
\end{tabular}

```

## Guidelines

NorNE: <https://github.com/ltgoslo/norne/blob/master/NorNe%20Annotation%20Guidelines.pdf>
UNER: <https://www.universalner.org/guidelines/>

## Mapping

Based on the following mapping:

```python
"B-DRV": "B-OTH",
"B-EVT": "B-OTH",
"B-GPE_LOC": "B-LOC",
"B-GPE_ORG": "B-ORG",
"B-LOC": "B-LOC",
"B-MISC": "B-OTH",
"B-ORG": "B-ORG",
"B-PER": "B-PER",
"B-PROD": "B-OTH",
"I-DRV": "I-OTH",
"I-EVT": "I-OTH",
"I-GPE_LOC": "I-LOC",
"I-GPE_ORG": "I-ORG",
"I-LOC": "I-LOC",
"I-MISC": "I-OTH",
"I-ORG": "I-ORG",
"I-PER": "I-PER",
"I-PROD": "I-OTH",
"O": "O",
```
