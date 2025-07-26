from connection import get_config # Import get_config
from agents import Runner
from agents.prompts import chat_prompt

# Get the run configuration
run_config = get_config()

# Define a simple chat prompt
# For simple text generation, you might not even need an explicit Agent class
# but rather directly use the model within a runner.
prompt = chat_prompt.format(
    instructions="You are a helpful assistant.",
    query="Say hello to Sultan."
)

# Run the prompt with the configured model
# The Runner.run_sync method usually takes a runnable and an input.
# Here, we're making the model itself runnable with a prompt.
result = Runner.run_sync(run_config.model, prompt) # Pass the model from run_config

# Access the generated content
print(result.output.content)