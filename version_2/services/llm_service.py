import os
import logging
from google import genai

# Initialize Gemini client with API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Path to your prompt file
PROMPT_FILE = os.path.join("prompts", "mood_prompt.txt")

def refine_query(user_mood: str, artist_name: str = "") -> str:
    """
    Refines the user input (mood + optional artist) into a Spotify-friendly search query.
    Returns original prompt if LLM fails.
    """
    try:
        # Read the prompt template
        with open(PROMPT_FILE, "r") as f:
            prompt_template = f.read()

        # Inject mood and artist into the prompt
        prompt = prompt_template.replace("{MOOD}", user_mood).replace("{ARTIST}", artist_name)

        # Send to Gemini LLM
        response = client.generate(
            model="gemini-2.5",
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=100
        )
        return response.output_text.strip() or f"{user_mood} {artist_name}".strip()
    except Exception as e:
        logging.warning(f"Error refining query: {e}")
        return f"{user_mood} {artist_name}".strip()


# import os
# import logging
# from google import genai

# # Initialize Gemini client with API key from environment
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def refine_query(prompt: str) -> str:
#     """
#     Refines the user input for Spotify search using Gemini 2.5.
#     Returns the original prompt if LLM fails.
#     """
#     try:
#         # Use the current client.generate() API
#         response = client.generate(
#             model="gemini-2.5",
#             prompt=prompt,
#             temperature=0.7,
#             max_output_tokens=100
#         )
#         # Access the generated text
#         refined = response.output_text.strip()
#         if not refined:
#             return prompt
#         return refined
#     except Exception as e:
#         logging.warning(f"Error refining query: {e}")
#         return prompt
