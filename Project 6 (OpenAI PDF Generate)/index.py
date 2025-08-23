from openai import OpenAI
from reportlab.pdfgen import canvas
import os

# Set your OpenAI API key from the environment variable

client = OpenAI(
    api_key=""
)


# Function to generate responses and create a PDF file
def generate_and_save_to_pdf(prompt):
    # Make API request to GPT-3.5
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)
    # Extract the generated text from the API response
    generated_text = completion.choices[0].message.content

    lines=generated_text.split("/n")

    # # Create a PDF file with the generated text
    with open('textfile.txt', 'w') as file:
        for line in lines:
            file.write(line)


# Example usage


# Sample prompt
prompt = "write a story of 100 words of any topic'"

generate_and_save_to_pdf(prompt)
