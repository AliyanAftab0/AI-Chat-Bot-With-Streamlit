# AI Chatbot

## Overview
This is an AI-powered chatbot built using **Streamlit** and **Google Gemini API**. The chatbot interacts with users in a friendly manner and remembers chat history during a session. It also includes features like recognizing developer-related queries, extracting code snippets, and styling for an enhanced user experience.

## Features
- Conversational AI powered by **Google Gemini API**.
- **Session memory** to maintain chat history.
- **Code block extraction** and display.
- **Custom UI styling** for a smooth chat experience.
- **Sidebar settings** for chat control and history clearing.

## Technologies Used
- **Python**
- **Streamlit** (for UI and frontend logic)
- **Google Generative AI (Gemini API)**
- **Regular Expressions (re module)** (for extracting code blocks)
- **Datetime** (for displaying last active status)

## Installation & Setup
### 1. Clone the repository:
```sh
 git clone https://github.com/your-username/ai-chatbot.git
 cd ai-chatbot
```

### 2. Create a virtual environment (optional but recommended):
```sh
 python -m venv venv
 source venv/bin/activate  # On macOS/Linux
 venv\Scripts\activate  # On Windows
```

### 3. Install dependencies:
```sh
 pip install -r requirements.txt
```

### 4. Set up API key:
Create a `.streamlit/secrets.toml` file and add your **Google Gemini API Key**:
```toml
[GEMINI_API_KEY]
GEMINI_API_KEY = "your_api_key_here"
```

### 5. Run the chatbot:
```sh
 streamlit run app.py
```

## Usage
- Open the chatbot in your browser and start a conversation.
- Clear chat history using the **sidebar settings**.
- View total messages and last active timestamp in the sidebar.
- Code blocks are automatically formatted when AI generates responses.

## Customization
- Modify the **CSS styles** inside the `st.markdown()` function to adjust the chatbot's appearance.
- Update the **generate_response()** function to handle specific queries.
- Enhance functionality by integrating **additional AI models**.

## Author
**Aliyan Aftab**  
[GitHub](https://github.com/AliyanAftab0) | [Portfolio](https://aliyan-dev.vercel.app)
