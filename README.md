# AI Assistant for SOP Verification and Quality Assurance

This project is a Streamlit web application that leverages OpenAI's GPT-3.5 model to verify Standard Operating Procedures (SOPs) and answer quality assurance-related questions. The application also stores interactions in a MongoDB database for record-keeping and analysis.

## Features

- **SOP Verification**: Upload an SOP file and verify its completeness, accuracy, and compliance.
- **Quality Assurance Q&A**: Ask questions related to quality assurance and get answers from the AI model.
- **Easter Egg**: Special response when specific context and question are provided.
- **Data Storage**: Store all interactions in a MongoDB database.

## Installation

### Prerequisites

- Python 3.7 or higher
- MongoDB instance (local or cloud, e.g., MongoDB Atlas)
- OpenAI API key

### Setup

1. Clone the repository:
   
git clone https://github.com/nicoletagorea/SOP-Verification-Assistant.git
cd SOP-Verification-Assistant

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Set up your environment variables:
Create a constants.py file in a .gitignore file in the directory of the project and add your OpenAI API key and MongoDB connection string:

OPENAI_API_KEY=your_openai_api_key
MONGODB_CONNECTION_STRING=your_mongodb_connection_string

### Running the Application

1. Run the Streamlit app:
streamlit run app.py

2. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

## Usage

SOP Verification: Upload a text file containing your SOP (see some testing examples in the folder). The AI will verify its completeness and accuracy.
Quality Assurance Q&A: Enter context (e.g., part of an SOP) and ask any quality assurance-related question.
Easter Egg: Enter the context "Odyssey" and ask "What is Python?" to see a special response.

## Project Structure

SOP-Verification-Assistant/
│
├── app.py                           # Main application script
├── constants.py                     # file for your keys
├── README.md                        # This README file
├── .env                             # Environment variables
├── SOP for scale 4_5.txt            # Model SOP 4/5 rating
├── SOP for pipette 3_5.txt          # Model SOP 3/5 rating
├── SOP for fridge 1_5.txt           # Model SOP 1/5 rating
├── requirements.txt                 # Python dependencies
└── Description.txt                  # Description

## Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.

### Acknowledgments

OpenAI for providing the GPT-3.5 model.
Streamlit for the web application framework.
MongoDB for the database solution.
And ME, I worked my *** off for this project :))

### Notes:
