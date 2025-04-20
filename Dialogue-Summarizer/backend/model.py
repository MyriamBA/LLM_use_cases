from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig
from peft import PeftModel
import torch

torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.benchmark = True 

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

peft_model_base = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large", torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")

peft_model = PeftModel.from_pretrained(peft_model_base, "./peft-dialogue-summarizer-checkpoint", torch_dtype=torch.bfloat16)
peft_model.to(device)
peft_model = torch.compile(peft_model)

def summarize(dialogue: str) -> str:
    with torch.inference_mode():
        inputs = tokenizer(dialogue, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
        inputs = {k: v.to(device) for k, v in inputs.items()}
        output_ids = peft_model.generate(
            input_ids=inputs["input_ids"],
            generation_config=GenerationConfig(max_new_tokens=100, num_beams=1, do_sample=False)
        )
        return tokenizer.decode(output_ids[0], skip_special_tokens=True)
