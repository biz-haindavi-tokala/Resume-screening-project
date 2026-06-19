from sentence_transformers import SentenceTransformer

MODEL_NAME = 'all-MiniLM-L6-v2' # convert text into numerical vectors called embeddings(semantic meaning)

model = SentenceTransformer(MODEL_NAME) 

print("Loaded successfully")

def generate_embedding(text: str):
    """
    Convert text into vector embedding.
    """

    return model.encode(text)