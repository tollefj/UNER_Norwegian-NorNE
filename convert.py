import logging
import os

from norne_uner_map import mapping
from util import get_aligned_file, get_file, lang_map, paths

logging.basicConfig(level=logging.INFO)


for lang in paths.keys():
    for split in ["dev", "test", "train"]:
        for getter in [get_aligned_file, get_file]:
            identifier = "NorNE" if getter == get_file else "NorNE-aligned"
            OUT_PATH = os.path.join(f"UNER_Norwegian_{identifier}")
            os.makedirs(OUT_PATH, exist_ok=True)
            logging.info(f"Fetching {lang} {split} from {getter.__name__}")
            iob2_filename = f"{lang_map[lang]}_norne-ud-{split}.iob2"
            iob2_path = os.path.join(OUT_PATH, iob2_filename)
            logging.info(f"Writing to {iob2_path}")
            with open(iob2_path, "w", encoding="latin-1") as f:
                data = getter(lang, split)
                logging.info(f"Got {len(data)} sentences")
                for sentence in data:
                    meta = sentence.metadata
                    _id = meta["sent_id"]
                    _text = meta["text"]
                    _newdoc = meta.get("newdoc id", None)
                    new_meta = {
                        "sent_id": _id,
                        "text": _text,
                    }
                    if _newdoc:
                        new_meta["newdoc id"] = _newdoc
                    # sort it alphabetically, as text follows sentid follows newdoc/newpar
                    new_meta = dict(sorted(new_meta.items(), key=lambda item: item[0]))
                    for k, v in new_meta.items():
                        f.write(f"# {k} = {v}\n")

                    for tok_idx, token_info in enumerate(sentence):
                        norne_tag = token_info["misc"].get("name", "-")
                        uner_tag = mapping.get(norne_tag, "-")

                        uner_line = "\t".join(
                            [
                                str(tok_idx + 1),
                                token_info["form"],
                                uner_tag,
                                norne_tag,
                                "-",  # annotator unknown
                            ]
                        )
                        f.write(uner_line + "\n")
                    f.write("\n")
