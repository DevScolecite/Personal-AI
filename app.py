from transformers import pipeline

# Load a pre-trained model
nlp = pipeline("text-generation", model="gpt2")

# Function to generate text
# Function to generate text with adjusted parameters
def generate_text(prompt):
    result = nlp(prompt, max_length=50, num_return_sequences=1, temperature=0.7, top_k=50)
    return result[0]['generated_text']

# Main function to handle conversation
def start_conversation():
    print("AI: Hello! Type '/start' to begin the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "/start":
            print("AI: Conversation started! You can start typing your questions.")
        elif user_input.strip().lower() == "/end":
            print("AI: Conversation ended. Goodbye!")
            break
        else:
            response = generate_text(user_input)
            print(f"AI: {response}")

# Example usage
if __name__ == "__main__":
    start_conversation()