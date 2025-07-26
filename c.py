from connection import get_config
from agents import Runner

# Get the run configuration
run_config = get_config()

# Define the prompt directly as a string or f-string
# The model will interpret this as a user query in a chat context
prompt_text = "Say hello to Sultan."

# Run the prompt with the configured model
result = Runner.run_sync(run_config.model, prompt_text)

# Access the generated content
print(result.output.content)