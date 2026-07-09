from sentence_transformers import SentenceTransformer

MODEL_NAME = 'all-MiniLM-L6-v2'     # model to convert text into numerical vectors called embeddings(semantic meaning)

model = SentenceTransformer(MODEL_NAME) 

print("Loaded successfully")

def generate_embedding(text: str):

    return model.encode(text)       # Convert text into vector embeddings.