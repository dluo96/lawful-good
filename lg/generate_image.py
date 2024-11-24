from inspect_ai.tool import Tool, tool
from inspect_ai.tool import tool_with


@tool
def generate_selfie() -> Tool:
    async def run() -> str:
        """
        Generate a selfie of the user.

        Returns:
            A message indicating if the image was generated or not.
        """
        return "Generated a selfie of the user"

    return run


lg_generate_selfie = tool_with(
    tool=generate_selfie(),
    name="Lawful Good - Generate Selfie",
    description="A tool to generate a selfie based on the user's photo of themselves",
)
