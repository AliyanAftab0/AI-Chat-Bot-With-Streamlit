import streamlit as st
import google.generativeai as genai
from datetime import datetime
import re

# Set page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Initialize Gemini client
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    st.error("Gemini API key not found. Please add it to your Streamlit secrets.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat" not in st.session_state:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        st.session_state.chat = model.start_chat(history=[])
        # Generate initial greeting
        response = st.session_state.chat.send_message(
            "Greet the user in a friendly way."
        )
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.text,
            }
        )
    except Exception as e:
        st.error(f"Failed to initialize chat: {e}")


# Function to generate response using Gemini
def generate_response(user_input):
    # Check for developer-related questions
    developer_questions = [
        "who is your developer",
        "who created you",
        "who is your creator",
        "who made you",
        "who developed you",
    ]

    # Normalize the input for comparison
    normalized_input = user_input.strip().lower()

    # Check if any developer question is asked
    if any(question in normalized_input for question in developer_questions):
        return "Aliyan Aftab"

    try:
        response = st.session_state.chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"


# Function to extract code blocks from text
def extract_code_blocks(text):
    # Pattern to match code blocks with triple backticks and optional language specifier
    pattern = r"```(\w+)?\s*([\s\S]*?)```"

    # Find all code blocks
    code_blocks = re.findall(pattern, text)

    # Return list of tuples (language, code)
    return code_blocks


# Sidebar with settings
with st.sidebar:
    st.header("Settings")
    if st.button("Clear Chat History"):
        # Reset messages and chat session
        st.session_state.messages = []
        model = genai.GenerativeModel("gemini-2.0-flash")
        st.session_state.chat = model.start_chat(history=[])
        # Generate new greeting
        response = st.session_state.chat.send_message(
            "Greet the user in a friendly way."
        )
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.text,
            }
        )
        st.rerun()

    st.markdown("---")
    st.markdown("**Chat History Info**")
    st.write(f"Total Messages: {len(st.session_state.messages)}")
    st.write(f"Last Active: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Custom CSS styling
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
 
    * {
        font-family: 'Poppins', sans-serif !important;
    }
    
    .chat-container {
        max-width: 800px;
        margin: auto;
        padding: 20px;
    }
    .message {
        margin: 12px 0;
        padding: 16px;
        border-radius: 12px;
        animation: fadeIn 0.3s;
        position: relative;
        font-size: 15px;
        line-height: 1.5;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .user-message {
        background:rgb(58, 58, 58);
        color: #FFFFFF;
        margin-left: 15%;
        border-radius: 12px 12px 4px 12px;
    }
    .assistant-message {
        background: rgb(27, 27, 44);
        color:rgb(255, 255, 255);
        margin-right: 15%;
        border-radius: 12px 12px 12px 4px;
    }
    .message-content {
        word-wrap: break-word;
        letter-spacing: -0.01em;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stChatInput {
        border-radius: 12px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }
    .stTitle {
        color: #1E293B !important;
        font-weight: 600 !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Main chat interface
st.title("🤖 AI Chatbot")
st.caption("Made By Aliyan Aftab")

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        message_class = (
            "user-message" if message["role"] == "user" else "assistant-message"
        )

        st.markdown(
            f"""
            <div class="message {message_class}">
                <div class="message-content">{message["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # If assistant message, check for code blocks and display them using st.code
        if message["role"] == "assistant":
            code_blocks = extract_code_blocks(message["content"])
            for lang, code in code_blocks:
                language = lang.strip() if lang else "python"
                st.code(code, language=language)

# User input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    with st.spinner("Thinking..."):
        ai_response = generate_response(prompt)

    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Rerun to update the chat display
    st.rerun()
