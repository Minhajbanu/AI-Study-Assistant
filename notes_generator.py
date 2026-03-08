

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
