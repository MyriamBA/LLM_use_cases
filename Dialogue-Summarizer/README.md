# Dialogue-Summarizer

## Project Overview
This project leverages the power of **Flan-T5**, a Transformer-based model from Google, to build an efficient Dialogue Summarizer. Utilizing the **Hugging Face API**, the summarizer processes conversations and generates concise, meaningful summaries, making it ideal for distilling key points from dialogues quickly and accurately. Whether you’re analyzing customer support chats, summarizing meeting transcripts, or exploring conversational AI, this tool simplifies the process by automating summary generation with state-of-the-art NLP techniques.😊😎

## Project Structure

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
-Integrated with Weights & Biases (WandB) from the project’s outset to track and visualize the training process. All training metrics, evaluation results, and performance logs are reported to WandB, enabling real-time monitoring and analysis of the model’s progress. Explore the [dashboard](https://wandb.ai/site/) for detailed insights into experiments and hyperparameter tuning.
### **Language**:
- Python 3.9+

## How It Works



