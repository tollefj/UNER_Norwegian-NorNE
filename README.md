# NorNE to UNER

Conversion from NorNE to UNER

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
mapping = {
    "B-DRV": "OTH",
    "B-EVT": "OTH",
    "B-GPE_LOC": "LOC",
    "B-GPE_ORG": "ORG",
    "B-LOC": "LOC",
    "B-MISC": "OTH",
    "B-ORG": "ORG",
    "B-PER": "PER",
    "B-PROD": "OTH",
    "I-DRV": "OTH",
    "I-EVT": "OTH",
    "I-GPE_LOC": "LOC",
    "I-GPE_ORG": "ORG",
    "I-LOC": "LOC",
    "I-MISC": "OTH",
    "I-ORG": "ORG",
    "I-PER": "PER",
    "I-PROD": "OTH",
    "O": "O",
}
```