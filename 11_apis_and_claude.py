# =============================================================================
# CHAPTER 11 — APIs & WORKING WITH CLAUDE
# =============================================================================
# An API (Application Programming Interface) is a way for one program
# to talk to another. Instead of a human typing into a website, a program
# sends a structured request and gets a structured response.
#
# Everything in modern software uses APIs:
#   - Your phone app talks to a server via APIs
#   - Claude itself is accessed via an API
#   - Claude Code uses tool APIs to read files, run code, search the web
#
# This chapter explains the concepts using Claude's API as the example.
# You will understand exactly what's happening when Claude responds to you.
# =============================================================================

import json


# =============================================================================
# PART A — WHAT IS AN API?
# =============================================================================

# -----------------------------------------------------------------------------
# 11.1  The request / response model
# -----------------------------------------------------------------------------
# Every API interaction follows the same basic pattern:
#
#   YOUR PROGRAM                     REMOTE SERVER
#       │                                  │
#       │──── REQUEST ─────────────────────▶│
#       │     (what you want)               │ processes
#       │                                  │ your request
#       │◀─── RESPONSE ────────────────────│
#       │     (what you get back)           │
#
# The request includes:
#   - WHERE to go (the URL / endpoint)
#   - WHAT to do (the method: GET, POST, PUT, DELETE)
#   - WHO you are (credentials / API key in headers)
#   - WHAT you want (the body — usually JSON)
#
# The response includes:
#   - STATUS CODE (200 = success, 400 = bad request, 500 = server error)
#   - BODY (the actual data — usually JSON)


# -----------------------------------------------------------------------------
# 11.2  HTTP Status Codes — the universal language of success/failure
# -----------------------------------------------------------------------------
STATUS_CODES = {
    200: "OK — success",
    201: "Created — resource was made",
    400: "Bad Request — your request had an error",
    401: "Unauthorized — missing or wrong API key",
    403: "Forbidden — you don't have permission",
    404: "Not Found — resource doesn't exist",
    429: "Too Many Requests — you hit a rate limit, slow down",
    500: "Internal Server Error — the server broke",
    503: "Service Unavailable — server is down temporarily",
}

def describe_status(code):
    description = STATUS_CODES.get(code, "Unknown status code")
    print(f"  Status {code}: {description}")

print("Common HTTP status codes:")
for code in STATUS_CODES:
    describe_status(code)


# =============================================================================
# PART B — THE CLAUDE API
# =============================================================================

# -----------------------------------------------------------------------------
# 11.3  What a Claude API request looks like
# -----------------------------------------------------------------------------
# When you use Claude.ai, the website sends requests like this behind
# the scenes. When you use Claude Code, the same thing happens.
#
# The actual request (using the requests library — not shown here):
#
#   import requests
#
#   response = requests.post(
#       url="https://api.anthropic.com/v1/messages",
#       headers={
#           "x-api-key": "your-api-key-here",
#           "anthropic-version": "2023-06-01",
#           "content-type": "application/json"
#       },
#       json={
#           "model": "claude-3-5-sonnet-20241022",
#           "max_tokens": 1024,
#           "messages": [
#               {"role": "user", "content": "What is Python?"}
#           ]
#       }
#   )
#
# This sends your message to Claude and gets a response back.

# Let's build the request structure as a Python dict to understand it:
def build_claude_request(user_message, model="claude-3-5-sonnet-20241022",
                         max_tokens=1024, system_prompt=None):
    """Build a Claude API request body as a Python dictionary."""

    request_body = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    if system_prompt:
        request_body["system"] = system_prompt

    return request_body


# What the request looks like:
request = build_claude_request(
    user_message="What are the top 3 benefits of AI in business?",
    system_prompt="You are a concise business consultant. Keep answers brief."
)

print("\nClaude API request structure:")
print(json.dumps(request, indent=2))


# -----------------------------------------------------------------------------
# 11.4  What Claude's response looks like
# -----------------------------------------------------------------------------
# Claude sends back a JSON object. Let's look at its structure.

# This is what a real Claude API response looks like (simulated here):
simulated_response = {
    "id": "msg_01XRtGNTBkNqcCRMjuXLBrJV",
    "type": "message",
    "role": "assistant",
    "content": [
        {
            "type": "text",
            "text": "The top 3 benefits of AI in business are:\n1. Efficiency — automates repetitive tasks\n2. Insights — finds patterns in data humans miss\n3. Scale — handles volume no human team could match"
        }
    ],
    "model": "claude-3-5-sonnet-20241022",
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 28,
        "output_tokens": 47
    }
}

def extract_text_from_response(response):
    """Pull the text out of a Claude API response."""
    content_blocks = response.get("content", [])
    text_parts = [
        block["text"]
        for block in content_blocks
        if block.get("type") == "text"
    ]
    return "\n".join(text_parts)

reply = extract_text_from_response(simulated_response)
print("\nClaude's reply:")
print(reply)
print("\nTokens used:", simulated_response["usage"])


# =============================================================================
# PART C — MULTI-TURN CONVERSATION
# =============================================================================

# -----------------------------------------------------------------------------
# 11.5  How conversation history works
# -----------------------------------------------------------------------------
# Claude has no memory between API calls by default.
# To have a conversation, you keep track of the history yourself
# and send the ENTIRE conversation with each new message.
#
# This is how Claude.ai works — the website stores your chat history
# and includes it in every new request.

def simulate_conversation():
    """Demonstrate how multi-turn conversation is tracked."""

    conversation_history = []     # this grows as the conversation continues

    def chat(user_message):
        """Add user message, get response, add to history."""
        # Add the user's message:
        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # In real code, send to API:
        # response = requests.post(..., json={"messages": conversation_history})

        # Simulating Claude's response:
        simulated_replies = {
            "Hi Claude!": "Hello! How can I help you today?",
            "What did I just say?": "You said 'Hi Claude!' — that was your first message.",
            "Can you summarise our chat?": "We've exchanged three messages so far: you greeted me, asked what you said, and now you've asked for a summary."
        }
        reply = simulated_replies.get(user_message, "I'm not sure how to answer that.")

        # Add Claude's response to history:
        conversation_history.append({
            "role": "assistant",
            "content": reply
        })

        return reply

    # Have a conversation:
    print("\nSimulated multi-turn conversation:")
    for msg in ["Hi Claude!", "What did I just say?", "Can you summarise our chat?"]:
        print(f"\nYou: {msg}")
        response = chat(msg)
        print(f"Claude: {response}")

    print("\nFull conversation history sent with last request:")
    print(json.dumps(conversation_history, indent=2))

simulate_conversation()


# =============================================================================
# PART D — SYSTEM PROMPTS AND PARAMETERS
# =============================================================================

# -----------------------------------------------------------------------------
# 11.6  System prompts — giving Claude a role and rules
# -----------------------------------------------------------------------------
# The system prompt is an instruction given BEFORE the user's message.
# It tells Claude who it is, how to behave, and what it can/can't do.
# This is how companies customise Claude for their specific use case.

system_prompt_examples = {
    "customer_support": """
        You are a helpful customer support agent for AcmeCorp.
        - Only answer questions about our products and services.
        - Be friendly but concise.
        - If you don't know something, say "Let me check that for you."
        - Never mention competitors.
    """,

    "code_reviewer": """
        You are a senior Python developer reviewing code.
        - Identify bugs, security issues, and performance problems.
        - Suggest improvements with specific examples.
        - Be direct and constructive, not harsh.
        - Focus on the most important issues first.
    """,

    "data_analyst": """
        You are a data analyst helping business stakeholders.
        - Explain technical findings in plain language.
        - Always state the practical business implication.
        - Use numbers and percentages when relevant.
        - Keep responses structured with bullet points.
    """
}

print("\nSystem prompt examples:")
for name, prompt in system_prompt_examples.items():
    print(f"\n--- {name} ---")
    print(prompt.strip())


# -----------------------------------------------------------------------------
# 11.7  Key parameters and what they control
# -----------------------------------------------------------------------------
PARAMETERS = {
    "model": {
        "example": "claude-3-5-sonnet-20241022",
        "explanation": "Which version of Claude to use. Different models have different capabilities and costs."
    },
    "max_tokens": {
        "example": 1024,
        "explanation": "Maximum length of Claude's response. A token is roughly 4 characters or 0.75 words."
    },
    "temperature": {
        "example": 0.7,
        "explanation": "Controls randomness. 0 = very consistent/predictable. 1 = more creative/varied."
    },
    "system": {
        "example": "You are a helpful assistant.",
        "explanation": "Instructions given to Claude before the conversation starts."
    },
    "messages": {
        "example": [{"role": "user", "content": "Hello"}],
        "explanation": "The conversation history. Each message has a role ('user' or 'assistant') and content."
    }
}

print("\nClaude API parameters:")
for param, info in PARAMETERS.items():
    print(f"\n  {param}")
    print(f"    Example: {info['example']}")
    print(f"    What it does: {info['explanation']}")


# =============================================================================
# PART E — CLAUDE CODE: TOOLS AND FUNCTION CALLING
# =============================================================================

# -----------------------------------------------------------------------------
# 11.8  What "tools" are in Claude Code
# -----------------------------------------------------------------------------
# Claude Code gives Claude access to TOOLS — Python functions it can call
# to interact with your computer: read files, run code, search the web, etc.
#
# You define a tool as a Python function. Claude sees its name and description.
# When Claude decides it needs to run that tool, it sends back a structured
# "tool use" response — and your code actually executes the function.

# This is what a tool definition looks like (the structure Claude sees):
tool_definition_example = {
    "name": "read_file",
    "description": "Read the contents of a file at the given path.",
    "input_schema": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The absolute or relative path to the file."
            }
        },
        "required": ["path"]
    }
}

print("\nExample tool definition (what Claude sees):")
print(json.dumps(tool_definition_example, indent=2))

# When Claude decides to use it, the response looks like:
tool_use_response = {
    "type": "tool_use",
    "id": "toolu_01A09q90qw90lq917835lq9",
    "name": "read_file",
    "input": {
        "path": "/project/main.py"
    }
}

print("\nClaude's tool use response:")
print(json.dumps(tool_use_response, indent=2))
print("→ Your code runs: read_file('/project/main.py')")
print("→ The result is sent back to Claude as a tool_result message.")
print("→ Claude reads the file content and continues its work.")


# =============================================================================
# KEY TAKEAWAYS
# =============================================================================
# - An API is a program-to-program communication channel
# - Every request needs: endpoint URL, method, headers (API key), body
# - HTTP status codes: 200=OK, 401=auth error, 429=rate limit, 500=server error
# - Claude's API endpoint is: POST https://api.anthropic.com/v1/messages
# - The request body: model, max_tokens, messages (with role + content)
# - Claude has no memory — you send the full conversation history each time
# - System prompts set Claude's role, rules, and behaviour
# - temperature controls creativity (0=consistent, 1=creative)
# - Claude Code tools are Python functions Claude can call
# - Understanding this helps you write better prompts and debug Claude's behaviour
# =============================================================================
