import PyPDF2
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama

file = "./data/rag_data1.pdf"
folder_path = "./vectordb"

# Read the PDF file
pdf = PyPDF2.PdfReader(file)
pdf_text = ""
for page in pdf.pages:
    pdf_text += page.extract_text()


        

# Split the text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
chunks = text_splitter.split_text(pdf_text)
print("Chunks")

# Create a Chroma vector store
embeddings = OllamaEmbeddings(model="chatboot-game")
print("Embedding")

vector_store = Chroma.from_texts(
        texts=chunks, embedding=embeddings, persist_directory=folder_path
)
print("vector_store")

vector_store.persist()
print("The data is persisted successfully!")








#!!!!!!!
# # setup_chromadb.py

# from langchain_community.llms import Ollama
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.document_loaders import PDFPlumberLoader
# from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
# # import ollama


# # Parameters
# file = "./data/rag_data.pdf"
# folder_path = "./vectordb"

# # Initialize embeddings
# embedding = OllamaEmbeddings(model="chatboot-game")
# # embedding = ollama.embeddings(model='chatboot-game')

# # Initialize text splitter
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=1024, chunk_overlap=80, length_function=len, is_separator_regex=False
# )

# # Load and split documents
# loader = PDFPlumberLoader(file)
# docs = loader.load_and_split()
# print(f"docs len={len(docs)}")

# chunks = text_splitter.split_documents(docs)
# print(f"chunks len={len(chunks)}")

# # Create and persist the vector store
# vector_store = Chroma.from_documents(
#     documents=chunks, embedding=embedding, persist_directory=folder_path
# )

# vector_store.persist()
# print("Vector store has been persisted.")
