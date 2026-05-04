from openai import OpenAI
from rich.console import Console

console = Console()
SGLANG_URL = "http://sglang-server:8000/v1"
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

console.print("[bold green]🔌 Connecting to SGLang RadixAttention backend...[/bold green]")

client = OpenAI(base_url=SGLANG_URL, api_key="EMPTY")

# yhanks to RadixAttention, if we run this loop 100 times, 
# SGLang will cache the system prompt and only compute the new user input
def run_agent():
    messages = [
        {"role": "system", "content": "You are a highly efficient AI agent running on SGLang."},
        {"role": "user", "content": "Explain RadixAttention in one sentence."}
    ]
    
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
    )
    console.print(f"[bold cyan]🤖 Agent:[/bold cyan] {response.choices[0].message.content}")

if __name__ == "__main__":
    run_agent()