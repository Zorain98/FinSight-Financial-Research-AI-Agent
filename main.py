import os
import streamlit as st
import pickle
import time
import langchain
import unstructured
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

api_key = st.secrets["OPENAI_API_KEY"]

st.title("FinSight: Financial Research AI Agent")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}", placeholder="Enter URL here")
    urls.append(url)
    if url:
        st.session_state[f"url_{i}"] = url

process_url = st.sidebar.button("Analyze")
main_placeholder = st.empty()

if process_url:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Analyzing URLs...")
    data = loader.load()
    # split data 
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ",", " "],
        chunk_size=1000
    )
    main_placeholder.text("Analyzing URLs...")
    docs = text_splitter.split_documents(data)
    # create embeddings
    embeddings = OpenAIEmbeddings()
    # create vector store
    vector_store = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Analyzing...")
    time.sleep(2)
    st.success("Done!")
    # stored in memory, not disk
    st.session_state["vector_store"] = vector_store

query = main_placeholder.text_input("Question: ")
if query:
    # use vector store from session state
    if "vector_store" in st.session_state:
        vector_store = st.session_state["vector_store"]
    # create retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    # create LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, api_key=api_key)
    # create chain
    chain = RetrievalQAWithSourcesChain.from_llm(llm, retriever=retriever)
    # run chain
    with st.spinner("Analyzing..."):
        result = chain({"question": query}, return_only_outputs=True)
        time.sleep(2)
        st.success("Done!")
        st.header(result["answer"])
        st.subheader(result["sources"])
