import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig
from peft import PeftModel
import torch 

# Load the fine-tuned model and tokenizer

peft_model_base = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large", torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")

peft_model_path = "./peft-dialogue-summarizer-checkpoint"

peft_model = PeftModel.from_pretrained(peft_model_base,
                                       peft_model_path,
                                       torch_dtype=torch.bfloat16,
                                       is_trainable=False)

# Move Model to GPU if available
device = torch.device("cpu")  # Force CPU
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
peft_model.to(device)

def summarize_dialogue(dialogue):
    inputs = tokenizer(dialogue, return_tensors="pt", max_length=(512), truncation=True, padding="max_length")
    inputs = {k: v.to(device) for k, v in inputs.items()}




    summary_ids=peft_model.generate(input_ids= inputs["input_ids"], generation_config=GenerationConfig(max_new_tokens=150, num_beams=1))
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Streamlit App
st.title("Dialogue Summarizer with PEFT")
st.write("Enter a dialogue below to get a summary powered by a fine-tuned PEFT model!:")

#Input Dialogue
dialogue_input = st.text_area("Enter Dialogue:", height=200, placeholder="Paste your dialogue here...")

#trigger the summarization
if st.button("Summarize"):
    if dialogue_input.strip() == "":
       st.warning("Please enter a dialogue to summarize!")
    else:
        with st.spinner("Generating Summary..."):
            summary = summarize_dialogue(dialogue_input)
            st.success("Summary Generated!")
            st.write(summary) 
