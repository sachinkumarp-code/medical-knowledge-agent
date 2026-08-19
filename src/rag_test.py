from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma

embedding_model = HuggingFaceBgeEmbeddings(model_name = 'all-MiniLM-L6-v2')
db = Chroma(persist_directory="data/chroma_db", embedding_function=embedding_model)
query = "What are the guidelines for managing heart failure?"
result = db.similarity_search(query, k=1)
print(result[0].page_content)