**Project: Talk To CSV**

This repository contains a Streamlit application that leverages Langchain to interact with and visualize data from a CSV file.

**Features:**

- User-friendly interface for uploading a CSV file
- Basic data exploration through plots

**Requirements:**

- Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- Streamlit ([https://streamlit.io/](https://streamlit.io/))
- Langchain ([https://langchain.readthedocs.io/en/latest/](https://langchain.readthedocs.io/en/latest/))
- Dependencies listed in `requirements.txt`

**Installation:**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vrushab-bit/Chat_with_CSV-langchain.git

   cd Chat_with_CSV-langchain
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   - Rename the `.env.local` file to `.env`.
   - Inside the `.env` file, add the following line, replacing `YOUR_OPENAI_API_KEY` with your actual OpenAI API key:

     ```
     OPENAI_API_KEY=YOUR_OPENAI_API_KEY
     ```

     - You can obtain an OpenAI API key from [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys).

**Running the application:**

1. **Start the Streamlit app:**

   ```bash
   streamlit run .\app.py
   ```

   This will launch the application in your web browser, typically at `http://localhost:8501`.

**Usage:**

1. Upload your CSV file using the file upload widget.
2. Explore the generated basic plots of your data.

Refer to the Streamlit and Langchain documentation for further exploration:

- Streamlit: [https://docs.streamlit.io/en/stable/](https://docs.streamlit.io/en/stable/)
- Langchain: [https://langchain.readthedocs.io/en/latest/](https://langchain.readthedocs.io/en/latest/)

**Contributing:**

We welcome contributions to this project! Please feel free to open pull requests with your improvements.
