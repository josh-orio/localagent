from dotenv import load_dotenv
load_dotenv()

from ollama import chat
import importlib
import os
import json
import httpx

messages = []
tool_lib = {}


# original_send = httpx.Client.send


# def send_and_log(self, request, **kwargs):
#     print("=== OLLAMA REQUEST ===")
#     body = request.content.decode("utf-8")
#     print("\x1b[38;5;14m" + json.dumps(json.loads(body), indent=2), "\x1b[0m")
#     print("=====================")
#     return original_send(self, request, **kwargs)


# httpx.Client.send = send_and_log


def main():
    # load tools
    for filename in os.listdir("tools"):
        if filename.endswith(".py") and filename != "__init__.py":
            # print(filename)
            module_name = filename[:-3]  # strip .py
            # print(module_name)
            module = importlib.import_module("tools." + module_name)
            # print(module)
            # print()

            for name in getattr(module, "__all__", []):
                # print(module, "- ", name)
                # print(name)
                tool_lib[name] = getattr(module, name)

    condition = True
    while condition:
        messages.append({"role": "user", "content": input("> ")})

        # print(json.dumps(messages, indent=4))
        # exit()

        if messages[-1]["content"].lower() == "quit":
            condition = False
            continue

        if messages[-1]["content"].lower() == "stackdump":
            print("\x1b[38;5;91m" + json.dumps(str(messages), indent=4) + "\x1b[0m")
            continue

        # print(json.dumps(messages, indent=2))

        while True:
            stream = chat(
                # model="qwen3.5:4b",
                # model="gemma4:e2b",
                model="gemma4:e4b",
                messages=messages,
                tools=tool_lib.values(),
                stream=True,
                think=True,
                # options={
                #     "repeat_penalty": 1.35,
                #     "repeat_last_n": 200,
                #     "temperature": 0.4,
                # }
            )

            thinking = ""
            content = ""
            tool_calls = []

            done_thinking = False
            # accumulate the partial fields
            for chunk in stream:
                if chunk.message.thinking:
                    thinking += chunk.message.thinking
                    print(
                        "\x1b[2m" + chunk.message.thinking + "\x1b[0m",
                        end="",
                        flush=True,
                    )

                if chunk.message.content:
                    if not done_thinking:
                        done_thinking = True
                        print("\n")
                    content += chunk.message.content
                    print(chunk.message.content, end="", flush=True)

                if chunk.message.tool_calls:
                    tool_calls.extend(chunk.message.tool_calls)
                    print("\x1b[38;5;10m" + str(chunk.message.tool_calls) + "\x1b[0m")



            # append accumulated fields to the messages
            if thinking or content or tool_calls:
                messages.append(
                    {
                        "role": "assistant",
                        "thinking": thinking,
                        "content": content,
                        "tool_calls": tool_calls,
                    }
                )

            # If no tool calls, we're done — break to get next user input
            if not tool_calls:
                break

            for call in tool_calls:
                if call.function.name in tool_lib:
                    result = tool_lib[call.function.name](**call.function.arguments)

                else:
                    result = "Unknown tool"
                messages.append(
                    {"role": "tool", "tool_name": call.function.name, "content": result}
                )


if __name__ == "__main__":
    main()
