from langchain_community.document_loaders import PyPDFDirectoryLoader  
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma


loader = PyPDFDirectoryLoader('data/pdfs')
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
chunks = text_splitter.split_documents(docs)

embedding_model = HuggingFaceBgeEmbeddings(model_name = "all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embedding_model, persist_directory="data/chroma_db")
print("Vector database saved successfully")