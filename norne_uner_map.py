# Event and Product tags with Other and mapping GPE_LOC to location and GPE_ORG to Organization.
# {PROD, EVT, MISC, DRV, XXX} to OTH and dealing with GPE as described.

# from norne -> uner tags.
mapping = {
    "B-EVT": "O",
    "B-GPE_LOC": "B-LOC",
    "B-GPE_ORG": "B-ORG",
    "B-LOC": "B-LOC",
    "B-MISC": "O",
    "B-ORG": "B-ORG",
    "B-PER": "B-PER",
    "B-PROD": "O",
    "I-DRV": "O",
    "I-EVT": "O",
    "I-GPE_LOC": "I-LOC",
    "I-GPE_ORG": "I-ORG",
    "I-LOC": "I-LOC",
    "I-MISC": "O",
    "I-ORG": "I-ORG",
    "I-PER": "I-PER",
    "I-PROD": "O",
    "O": "O",
}
