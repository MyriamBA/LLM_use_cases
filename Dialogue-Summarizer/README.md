# Dialogue-Summarizer

## Project Overview
This project leverages the power of **Flan-T5**, a Transformer-based model from Google, to build an efficient Dialogue Summarizer. Utilizing the **Hugging Face API**, the summarizer processes conversations and generates concise, meaningful summaries, making it ideal for distilling key points from dialogues quickly and accurately. Whether you’re analyzing customer support chats, summarizing meeting transcripts, or exploring conversational AI, this tool simplifies the process by automating summary generation with state-of-the-art NLP techniques.😊😎

## Project Structure
```
Dialogue-Summarizer/
│── peft-dialogue-summarizer-checkpoint/
│   │── adapter_config
│   │── adapter_model.bin
│   │── special_tokens_map
│   │── tokenizer
│   │── tokenizer_config
│── Dialogue_Summarizer.ipynb
│── app.py
```

## Technology Stack

### **Model:**
- Utilizes [Flan-T5-Large](https://huggingface.co/google/flan-t5-large) (783M parameters), a powerful variant of the Flan-T5 family, to deliver high-quality abstractive summarization. For more details on Flan-T5 variants, check out the [official documentation](https://huggingface.co/docs/transformers/model_doc/flan-t5).
### **Framework:**
- Built with Hugging Face’s [transformers library](https://huggingface.co/docs/transformers/index) for seamless model integration and inference. 
### **Dataset**:
- [DialogSum](https://huggingface.co/datasets/knkarthick/dialogsum), which is a large-scale dialogue summarization dataset (English dialogues).
### **Training**: 
- Parameter-Efficient Fine-tuning (PEFT) with **LoRA** configuration to adapt the model efficiently, tuning **0.6%** of parameters to save resources, speed up training, and avoid overfitting.
### **WandB Integration:**
- Integrated with Weights & Biases (WandB) from the project’s outset to track and visualize the training process. All training metrics, evaluation results, and performance logs are reported to WandB, enabling real-time monitoring and analysis of the model’s progress. Explore the [dashboard](https://wandb.ai/site/) for detailed insights into experiments and hyperparameter tuning.

### **Streamlit for UI:**
- The frontend is built using Streamlit, providing an interactive and user-friendly interface for your dialogue and generating the summary. 

## How It Works
The **Flan-T5-large** model has already been fine-tuned using **PEFT: LoRA**, enhancing its summary generation performance, as demonstrated in the table of ROUGE enhancements. In this project, we utilize the saved checkpoint from the fine-tuned PEFT model to ensure improved efficiency and accuracy.
| Metric | Original-model | Improvement |
|----------|----------|----------|
| rouge 1   | 0.4122  | 2.96%   |
| rouge 2   | 0.1137   | 5.03%  |
| rougeL  | 0.2795   | 4.22%   |
| rougeLsum  | 0.2182   | 4.12%   |



## Installation
To set up and run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MyriamBA/NLP_Projects.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate 
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements
- Incorporate multilingual dialogue, as this project currently generates summaries only in English.
- Enhance UI/UX with better visualization tools.

## Contributions
Feel free to open issues and submit pull requests for improvements.


