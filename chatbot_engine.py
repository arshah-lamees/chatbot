from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatbotEngine:
    def __init__(self, model_name="microsoft/DialoGPT-small"):
        print("Loading model and tokenizer from Hugging Face Hub...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None
        self.attention_mask = None
        print("Model and tokenizer loaded.")

    def generate_response(self, user_message: str) -> str:
        # 1. Tokenize the new user input, and this time, get the attention_mask
        new_inputs = self.tokenizer(user_message + self.tokenizer.eos_token, return_tensors='pt')
        new_user_input_ids = new_inputs.input_ids
        new_attention_mask = new_inputs.attention_mask

        # 2. Append the new user input and attention_mask to the chat history
        if self.chat_history_ids is not None:
            # Use an assert statement as a strong hint for the type checker
            assert self.attention_mask is not None, "Attention mask and chat history should be synced."
            bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1)
            bot_attention_mask = torch.cat([self.attention_mask, new_attention_mask], dim=-1)
        else:
            bot_input_ids = new_user_input_ids
            bot_attention_mask = new_attention_mask

        # 3. Generate a response, passing the attention mask
        self.chat_history_ids = self.model.generate(
            bot_input_ids,
            attention_mask=bot_attention_mask,
            max_length=1000,
            pad_token_id=self.tokenizer.eos_token_id,
            no_repeat_ngram_size=3,
            do_sample=True,
            top_k=100,
            top_p=0.7,
            temperature=0.8
        )
        
        # 4. Update the attention mask for the next turn to match the new history
        self.attention_mask = torch.ones_like(self.chat_history_ids)

        # 5. Decode the last response from the bot
        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

    def reset_history(self):
        self.chat_history_ids = None
        self.attention_mask = None 