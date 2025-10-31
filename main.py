import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) > 1:
        user_prompt = sys.argv[1] if '--verbose' != sys.argv[1] else sys.argv[2]
        messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",contents=messages
        )
        
        print(response.text)
        if '--verbose' in sys.argv:
            print(f"User prompt: \"{user_prompt}\"")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(f"Error: additional input required after 'main.py'")
        return 1


if __name__ == "__main__":
    sys.exit(main())
