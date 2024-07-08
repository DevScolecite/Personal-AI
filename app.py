from transformers import pipeline

# Load a pre-trained model
nlp = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Function to generate text with context
def generate_text(context, prompt):
    combined_prompt = context + "\n" + prompt
    result = nlp(combined_prompt, max_length=150, num_return_sequences=1, temperature=0.7, top_k=50)
    return result[0]['generated_text']

# Main function to handle conversation
def start_conversation():
    context = ""
    print("AI: Hello! Type '/start' to begin the conversation or '/end' to end it.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "/start":
            context = "AI: Conversation started! You can start typing your questions."
            print("AI: Conversation started! You can start typing your questions.")
        elif user_input.strip().lower() == "/end":
            print("AI: Conversation ended. Goodbye!")
            break
        elif context.startswith("AI: Conversation started!"):
            context += "\nYou: " + user_input
            response = generate_text(context, "AI:")
            print(f"AI: {response}")
            context += "\nAI: " + response
        else:
            print("AI: Please type '/start' to begin the conversation or '/end' to end it.")

# Example usage
if __name__ == "__main__":
    start_conversation()
