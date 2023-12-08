import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def read_prompt_from_binary_file(file_path):
    with open(file_path, 'rb') as file:
        binary_content = file.read()
    return binary_content.decode('utf-8')

def generate_text(prompt, max_length=50, temperature=0.7):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, temperature=temperature, do_sample=True, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

def save_text_to_binary_file(text, file_path):
    with open(file_path, 'wb') as file:
        file.write(text.encode('utf-8'))

model_save_path = "/home/lab518/Rownak/MODELS/GPT2"
model = GPT2LMHeadModel.from_pretrained(model_save_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_save_path)
model.eval()

QueryFile = r"/home/lab518/DATA/Query.bin"
user_prompt = read_prompt_from_binary_file(QueryFile)
Generated_Text = generate_text(user_prompt, max_length=50, temperature=0.7)
print("Response:")
print(Generated_Text)
ResponseFile = r"/home/lab518/DATA/Response.bin"
save_text_to_binary_file(Generated_Text, ResponseFile)
