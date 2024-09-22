from conllu import parse

paths = {
    "bokmaal": "norne/ud_aligned/nob",
    "nynorsk": "norne/ud_aligned/nno",
}
lang_map = {
    "bokmaal": "nob",
    "nynorsk": "nno",
}


def get_file(lang, split):
    fp = f"{paths[lang]}/no_{lang}-ud-{split}.conllu"
    data = None
    with open(fp, "r", encoding="latin1") as f:
        data = parse(f.read())
    return data


def get_aligned_file(lang, split):
    # UD-NARC\output\aligned\no-narc_bokmaal\narc_bokmaal_dev.conllu
    fp = f"UD-NARC/output/aligned/no-narc_{lang}/narc_{lang}_{split}.conllu"
    data = None
    with open(fp, "r", encoding="latin1") as f:
        data = parse(f.read())

    return data


def get_tags():
    sample = get_file("bokmaal", "train")
    tags = set()
    # already verified: bokmaal contains all tags in the full dataset
    for sentence in sample:
        for token in sentence:
            ner_tag = token["misc"]["name"]
            tags.add(ner_tag)
    return tags


if __name__ == "__main__":
    print(get_tags())
