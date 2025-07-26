from connection import get_config
from agents import Agent, Runner

run_config = get_config()

greeter_agent = Agent(
    name="Greeter",
    instructions="You are a polite assistant. Your only task is to greet people.",
    model=run_config.model, # Assign the configured model to the agent
    tools=[]
)

agent_input = "Say hello to Sultan."

result = Runner.run_sync(greeter_agent, agent_input)

print(result.final_output)