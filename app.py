from transformers import pipeline

# Load a pre-trained model
nlp = pipeline("text-generation", model="gpt2")

# Function to generate text
def generate_text(prompt):
    result = nlp(prompt, max_length=50, num_return_sequences=1)
    return result[0]['generated_text']

# Example usage
if __name__ == "__main__":
    prompt = "Once upon a time"
    generated_text = generate_text(prompt)
    print(generated_text)