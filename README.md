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
   ```sh
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Set up your environment variables:
Create a .env file in the root directory of the project and add your OpenAI API key and MongoDB connection string:

OPENAI_API_KEY=your_openai_api_key
MONGODB_CONNECTION_STRING=your_mongodb_connection_string
DATABASE_NAME=your_database_name