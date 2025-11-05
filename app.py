import streamlit as st
from openai import OpenAI

# Set up the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

st.title("Student Chatbot")
st.markdown("### made by rahul, powered by Streamlit")  # or "##" for larger

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful student assistant. Be concise and accurate."}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your question?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        history = st.session_state.messages[-20:]
        completion = client.chat.completions.create(
            model="nvidia/nemotron-nano-12b-v2-vl:free",
            messages=history,
        )
        response = completion.choices[0].message.content
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
