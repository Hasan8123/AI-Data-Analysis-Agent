import os
import sys

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_data_analyst import st

# For Vercel, we need to handle the request via a serverless function
# However, Streamlit usually runs its own server.
# This index.py acts as the entry point that Vercel looks for.

def handler(request):
    # This is a placeholder for Vercel's Python runtime.
    # In a real Streamlit-on-Vercel setup, we'd use a bridge.
    # But since the user might prefer Streamlit Cloud,
    # we provide the files needed for the 'experimental' path.
    return {
        'statusCode': 200,
        'body': 'Streamlit app is configured. Please push to GitHub and connect to Vercel.'
    }
