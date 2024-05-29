from flask import Flask, request
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.prompts import PromptTemplate
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(app, cors_allowed_origins="*")

llm = Ollama(model="chatboot-game")

# Parameters
folder_path = "./vectordb"

# Load embedding model
embedding = OllamaEmbeddings(model="chatboot-game")

# Load the persisted vector store
print("Loading vector store")
vector_store = Chroma(persist_directory=folder_path, embedding_function=embedding)

raw_prompt = PromptTemplate.from_template(
    """ 
    <s>[INST] vous etes un generateur des histoirs des jeu video pédagogiques , si l'utilisateur demande d'autre chose deffirent lui dit que "en tant que générateur des histoires de jeu video pedagogique je peux pas vous aider et generer le text en francais et dans un seul ligne !" "  . [/INST] </s>
    [INST] {input}
           Context: {context}
           Answer:
    [/INST]
"""
)

@socketio.on('message')
def chat(msg):
    # Your retrieval and processing logic here
    print(f"prompt: {msg}")

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 4,
            "score_threshold": 0.1,
        },
    )

    document_chain = create_stuff_documents_chain(llm, raw_prompt)
    chain = create_retrieval_chain(retriever, document_chain)

    # Simulate streaming response by splitting the result into chunks
    result = chain.invoke({"input": msg})
    answer = result.get("answer", "")
    
    # Split the answer into chunks for streaming
    chunks = [answer[i:i+50] for i in range(0, len(answer), 50)]
    
    for chunk in chunks:
        socketio.emit('response', chunk)
        socketio.sleep(0.1)  

if __name__ == '__main__':
    socketio.run(app, debug=True)
