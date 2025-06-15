def get_entities(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Get all named entities along with their labels
    result = []
    for ent in doc.ents:
        result.append(f" {ent.text} {ent.label_}")

    return result


def get_person(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Get all entities that have PERSON label
    result = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            result.append(ent.text)

    return result


def get_lemma(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Get all words with their lemma
    result = []
    for token in doc:
        result.append((token.text, token.lemma_))

    return result

def get_unstop_words(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Get all the words which are not stop loss
    filtered_words = [token.text for token in doc if not token.is_stop]

    return filtered_words

def get_stop_words(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    nlp.vocab["powerful"].is_stop = True

    # Get all stop words after marked powerful as a stop word
    stop_words = [token.text for token in doc if token.is_stop]

    return stop_words

def get_matcher(text: str):
    import spacy
    from spacy.matcher import PhraseMatcher

    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(nlp.vocab)

    # Use PhraseMatcher to identify the phrase "artificial intelligence" in a sentence and print matches

    phrase = ["artificial intelligence", "Artificial Intelligence"]
    patterns = [nlp(text) for text in phrase]
    matcher.add("AI_PHRASE", patterns)

    doc = nlp(text)

    # Get all words that match the define pattern
    result = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        result.append(doc[start:end].text)

    return result


def get_tag_pos(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Get all tag and pos of each word
    result = [
        {"text": token.text, "pos": token.pos_, "description": spacy.explain(token.pos_)}
        for token in doc
    ]

    return result

def get_sentence_separator(text: str):
    import spacy
    from spacy.language import Language
    nlp = spacy.load("en_core_web_sm")

    @Language.component("custom_separator")
    def custom_separator(doc):
        for token in doc[:-1]:
            if token.text == '^':
                doc[token.i + 1].is_sent_start = True
        return doc

    nlp.add_pipe('custom_separator', before='parser')

    doc = nlp(text)

    # Get all sentences
    result = [sent.text for sent in doc.sents]

    return result