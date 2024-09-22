# NorNE to UNER

Conversion from NorNE to UNER

## Run

```bash
python download.py
python convert.py
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