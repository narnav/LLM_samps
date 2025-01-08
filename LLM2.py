from gpt4all import GPT4All
model = GPT4All("C:/Users/rabak/AppData/Local/nomic.ai/GPT4All/qwen2.5-coder-7b-instruct-q4_0.gguf") # downloads / loads a 4.66GB LLM
with model.chat_session():
    print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))

    