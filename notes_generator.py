# import ollama
# from sentence_transformers import SentenceTransformer
# import numpy as np


# model = SentenceTransformer("all-MiniLM-L6-v2")


# def retrieve_chunks(query, index, chunks, k=3):

#     query_embedding = model.encode([query])

#     distances, indices = index.search(np.array(query_embedding), k)

#     results = [chunks[i] for i in indices[0]]

#     return results


# def generate_notes(index, chunks):

#     query = "Generate exam preparation notes from the study material"

#     relevant_chunks = retrieve_chunks(query, index, chunks)

#     context = "\n".join(relevant_chunks)

#     prompt = f"""
#     You are an AI tutor helping students prepare for exams.

#     Based on the following study material generate structured exam notes.

#     Study Material:
#     {context}

#     Generate the output in the following format:

#     1. Key Concepts
#     2. Important Definitions
#     3. Important Topics
#     4. Possible Exam Questions
#     5. Quick Revision Notes
#     """

#     response = ollama.chat(
#         model="gemma3:4b",
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return response["message"]["content"]

import ollama


def generate_notes(vectorstore, chunks):

    query = "Generate exam preparation notes from the study material"

    # Retrieve most relevant chunks from vector database
    docs = vectorstore.similarity_search(query, k=5)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an AI tutor helping students prepare for exams.

Based on the following study material generate clear, structured exam notes.

Study Material:
{context}

Generate the output in the following format:

# Key Concepts
- Bullet points explaining the most important ideas

# Important Definitions
- Clear definitions students should remember

# Important Topics
- Topics that are likely to appear in exams

# Possible Exam Questions
- 3–5 questions students may be asked

# Quick Revision Notes
- Very short summary for last minute revision

Keep explanations simple and easy for students.
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]