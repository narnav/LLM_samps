import gpt4all

def main():
    # Load the GPT for All model
    model_path = "C:/Users/rabak/AppData/Local/nomic.ai/GPT4All/qwen2.5-coder-7b-instruct-q4_0.gguf"  # Replace with the actual path to your GPT model
    llm = gpt4all.GPT4All(model_path)

    # Interact with the model
    print("Welcome to GPT for All!")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Generate a response
        response = llm.generate(user_input)
        print(f"GPT: {response}")

if __name__ == "__main__":
    main()
