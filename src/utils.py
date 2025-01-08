from config import CFG_SERVICE

from langchain_openai import ChatOpenAI, AzureChatOpenAI
from neo4j import GraphDatabase

# ==================================================
# LLM
# ==================================================


def get_langchain_chat_llm():
    llm = ChatOpenAI(
        model=CFG_SERVICE.openai.llm_model,
        max_tokens=CFG_SERVICE.openai.llm_max_tokens,
        api_key=CFG_SERVICE.openai.api_key,
        temperature=0,
    )
    return llm


def get_langchain_azure_chat_llm():
    llm = AzureChatOpenAI(
        azure_endpoint=CFG_SERVICE.azure.openai_canada.api_base,
        openai_api_key=CFG_SERVICE.azure.openai_canada.api_key,
        deployment_name=CFG_SERVICE.azure.openai_canada.llm_deployment,
        model=CFG_SERVICE.azure.openai_canada.llm_model,
        openai_api_version=CFG_SERVICE.azure.openai_canada.api_version,
        temperature=0,
        max_retries=0,
    )
    return llm
