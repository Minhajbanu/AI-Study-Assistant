from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA


def create_chatbot(vectorstore):

    llm = Ollama(model="gemma3:4b")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa_chain


def ask_question(qa_chain, question):

    result = qa_chain.run(question)

    return result