from fastapi import FastAPI
from model import TextInput
import bl

# Create FastAPI instance
app = FastAPI(title="Example API", description="A simple FastAPI with Swagger UI", version="1.0")


# Define a simple GET endpoint
@app.get("/welcome")
def read_root():
    return {"message": "Welcome to the FastAPI example!"}


# Define a simple GET endpoint
@app.get("/get-entities")
def get_entities(text: str):
    print(f"========= input get_entities: {text}")
    result = bl.get_entities(text)
    return {"entities": result}


@app.get("/get-person")
def get_person(text: str):
    print(f"========= input get_person: {text}")
    result = bl.get_person(text)
    return {"people": result}


@app.post("/get-lemma")
def get_lemma(input_data: TextInput):
    print(f"========= input get_lemma: {input_data.text}")
    result = bl.get_lemma(input_data.text)
    return {"lemma": result}


@app.post("/get-unstop-words")
def get_unstop_words(input_data: TextInput):
    print(f"========= input get-unstop-words: {input_data.text}")
    result = bl.get_unstop_words(input_data.text)
    return {"unstop_words": result}


@app.get("/get-stop-words")
def get_stop_words(text: str):
    print(f"========= input get_stop_words: {text}")
    result = bl.get_stop_words(text)
    return {"stop_words": result}


@app.get("/get-matcher")
def get_matcher(text: str):
    print(f"========= input get_matcher: {text}")
    result = bl.get_matcher(text)
    return {"matcher": result}


@app.get("/get-tag-pos")
def get_tag_pos(text: str):
    print(f"========= input get_tag_pos: {text}")
    result = bl.get_tag_pos(text)
    return {"tag_pos": result}


@app.get("/get-sentence-separator")
def get_sentence_separator(text: str):
    print(f"========= input get_sentence_separator: {text}")
    result = bl.get_sentence_separator(text)
    return {"sentence_separator": result}