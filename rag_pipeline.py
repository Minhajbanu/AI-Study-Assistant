from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

model = SentenceTransformer('all-MiniLM-L6-v2')


# def create_vector_store(text):

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=100
#     )

#     chunks = splitter.split_text(text)

#     embeddings = model.encode(chunks)

#     embeddings = np.array(embeddings)

#     dimension = embeddings.shape[1]

#     index = faiss.IndexFlatL2(dimension)

#     index.add(embeddings)

#     return index, chunks

def create_vector_store(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = FAISS.from_texts(chunks, embeddings)

    return vectorstore, chunks