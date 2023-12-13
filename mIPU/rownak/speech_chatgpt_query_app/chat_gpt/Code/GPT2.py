import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model_save_path = "/home/lab518/Rownak/MODELS/GPT2"
model.save_pretrained(model_save_path)
tokenizer.save_pretrained(model_save_path)
model = GPT2LMHeadModel.from_pretrained(model_save_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_save_path)
model.eval()

def generate_text(prompt, max_length=50, temperature=0.7):
    input_ids = tokenizer.encode(prompt, return_tensors = "pt")
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

print("Please enter your query:")
user_prompt = input()
generated_story = generate_text(user_prompt, max_length=50, temperature=0.7)
print("Response:")
print(generated_story)