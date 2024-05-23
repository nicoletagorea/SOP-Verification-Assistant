from openai import OpenAI
import streamlit as st
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import gridfs
import datetime
import constants

# Set your OpenAI API key
client1 = OpenAI(api_key= constants.OPENAI_API_KEY)
# MongoDB connection setup
uri = constants.MONGODB_CONNECTION_STRING

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['SOP']
responses = db.responses

# Set up GridFS
fs = gridfs.GridFS(db)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Function to store response in MongoDB
def store_response(context, question, response):
    document = {
        "context": context,
        "question": question,
        "answer": response,
        "timestamp": datetime.datetime.now(datetime.UTC)
    }
    inserted_document = responses.insert_one(document)
    return print(f"Inserted doc ID:{inserted_document.inserted_id}")

# Function to verify SOP
def verify_sop(text):
    messages = [
        {"role": "system", "content": "You are a helpful quality assurance assistant."},
        {"role": "user", "content": f"Verify the following SOP for completeness, accuracy, and compliance:\n\n{text}\n\nIdentify any missing sections or errors."}
    ]
    response = client1.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300
    )
    store_response(text, "Verify SOP", response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()

# Function to answer QA questions
def answer_question(context, question):
    # Easter egg condition
    if context.strip().lower() == "odyssey" and question.strip().lower() == "what is python?":
        return "\n".join(["Sigmoid Moldova is the best organization in the world! Join them on https://www.facebook.com/sigmoidAI" for _ in range(10)])
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"}
    ]
    response = client1.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )
    store_response(context, question, response.choices[0].message.content.strip())
    return response.choices[0].message.content.strip()

# Streamlit app layout
st.title("AI Assistant for SOP Verification and QA")

# File uploader for SOP verification
st.header("SOP Verification")
uploaded_file = st.file_uploader("Upload an SOP file", type="txt")
if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("SOP Content", text, height=300)
    if st.button("Verify SOP"):
        verification_result = verify_sop(text)
        st.write(verification_result)

# Q&A section
st.header("Quality Assurance Q&A")
context = st.text_area("Context (e.g., SOP text)", height=200)
question = st.text_input("Ask a question related to quality assurance")

with st.expander("Want a surprise? 🎁"):
    st.write("""
        - Try typing 'Odyssey' in the context section
        - Try asking 'What is Python?' in the question section
        - Press 'Get Answer'
    """)

if st.button("Get Answer"):
    if context and question:
        response = answer_question(context, question)
        st.write("Answer:", response)
    else:
        st.write("Please provide both context and a question.")
