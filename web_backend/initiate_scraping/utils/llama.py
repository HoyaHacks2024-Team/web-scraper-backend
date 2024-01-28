from llama_index.llms import AzureOpenAI
from llama_index.embeddings import VoyageEmbedding
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.storage.storage_context import StorageContext
from llama_index import set_global_service_context
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch

import logging
import sys
import os

import pymongo

from dotenv import load_dotenv
env_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
load_dotenv(dotenv_path=env_path)


from llama_index import download_loader


def create_vector_embedding(data):
    llm = AzureOpenAI(
        model=os.getenv("OPENAI_MODEL_COMPLETION"),
        deployment_name=os.getenv("OPENAI_DEPLOYMENT_COMPLETION"),
        api_key=os.getenv("OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_version=os.getenv("OPENAI_API_VERSION"),
    )

    # Set up the OpenAIEmbedding instance
    embed_model = VoyageEmbedding(model_name=os.getenv("VOYAGE_MODEL_NAME"), voyage_api_key=os.getenv("VOYAGE_API_KEY"))

    # Set up service context
    service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
    set_global_service_context(service_context)


    StringIterableReader = download_loader("StringIterableReader")

    loader = StringIterableReader()
    documents = loader.load_data(texts=[data])

    index = VectorStoreIndex.from_documents(documents)
    return index


if __name__ == '__main__':
    ind = create_vector_embedding("Hello I am John, and my favorite color is indigo blue. My favorite dog is a Golden Retriever.")
    query = "What is the author's favorite color?"
    query_engine = ind.as_query_engine()
    ans = query_engine.query(query)
    
    print(ans.get_formatted_sources())
    print("Query was:", query)
    print("Answer was:", ans)

