import torch
from transformers import GPT2LMHeadModel

model_save_path = "/home/lab518/Rownak/MODELS/GPT2"
model = GPT2LMHeadModel.from_pretrained(model_save_path)

def analyze_model_details(model):
    layer_details = []

    for name, param in model.named_parameters():
        layer_info = {}
        if 'transformer.h.' in name:
            layer_num = int(name.split('.')[2])
            param_type = name.split('.')[3]
            num_neurons = param.size(0)

            layer_info['layer'] = layer_num
            layer_info['param_type'] = param_type
            layer_info['num_neurons'] = num_neurons
            layer_info['num_params'] = param.numel()
            layer_info['bit_size'] = param.element_size() * 8  # Size in bits

            layer_details.append(layer_info)

    return layer_details

def print_specific_weights(model, layer_num, start, end):
    layer_name = f"transformer.h.{layer_num}."
    for name, param in model.named_parameters():
        if layer_name in name:
            print(f"Layer: {name}")
            if len(param.data.shape) == 1:  # Check if the tensor is one-dimensional
                print(param.data[start:end])  # Print a slice for 1D tensor
            elif len(param.data.shape) == 2:  # Check if the tensor is two-dimensional
                print(param.data[start:end, start:end])  # Print a 2D slice
            break

layer_details = analyze_model_details(model)

for detail in layer_details:
    print(detail)
    
print_specific_weights(model, layer_num=0, start=0, end=767)
