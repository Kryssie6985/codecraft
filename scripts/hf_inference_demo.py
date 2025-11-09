"""
A script to demonstrate remote Hugging Face inference
using the huggingface_hub client.

Place a file named `.env` next to this script with:
HF_API_TOKEN=your_token_here

Do NOT commit the real .env file. Use .env.example for repo.
"""

# 1. Imports
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import sys

# 2. Metadata
__version__ = "1.0.0"
__author__ = "Kode_Animator"

# 3. Load Config (as per your instructions)
load_dotenv()
HF_TOKEN = os.getenv("HF_API_TOKEN")

# 4. Code Logic
def analyze_sentiment_api(text_to_analyze: str, model: str = "distilbert-base-uncased-finetuned-sst-2-english") -> None:
    """
    Runs remote sentiment analysis using the HF Inference API.
    Prints the result as returned by the InferenceClient.
    """
    if not HF_TOKEN:
        print("Error: HF_API_TOKEN not found in environment. Create a .env with HF_API_TOKEN or export it.")
        return

    print("Initializing API client...")
    client = InferenceClient(token=HF_TOKEN)

    try:
        print(f"Analyzing (model={model}): '{text_to_analyze}'")
        # text_classification returns a list of labels with scores for this model
        result = client.text_classification(model=model, inputs=text_to_analyze)
        print("--- Result ---")
        print(result)

    except Exception as e:
        print(f"An API error occurred: {e}")


# 5. CLI entrypoint
if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = "This is a fantastic idea and a perfect example!"
    analyze_sentiment_api(text)
