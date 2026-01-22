"""Utility functions for MCP NanoBanana server."""

from typing import Any


def format_image_result(data: dict[str, Any]) -> str:
    """Format image generation/edit result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if not data.get("success", False):
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    lines = [
        f"Task ID: {data.get('task_id', 'N/A')}",
        f"Trace ID: {data.get('trace_id', 'N/A')}",
        "",
    ]

    images = data.get("data", [])
    for i, image in enumerate(images, 1):
        lines.extend(
            [
                f"--- Image {i} ---",
                f"Prompt: {image.get('prompt', 'N/A')}",
                f"Image URL: {image.get('image_url', 'N/A')}",
                "",
            ]
        )

    return "\n".join(lines)


def format_task_result(data: dict[str, Any]) -> str:
    """Format task query result for display.

    Args:
        data: API response dictionary

    Returns:
        Formatted string representation of the result
    """
    if "error" in data:
        error = data.get("error", {})
        return f"Error: {error.get('code', 'unknown')} - {error.get('message', 'Unknown error')}"

    request_info = data.get("request", {})
    response_info = data.get("response", {})

    lines = [
        f"Task ID: {data.get('id', 'N/A')}",
        f"Created At: {data.get('created_at', 'N/A')}",
        f"Type: {data.get('type', 'N/A')}",
        "",
        "Request:",
        f"  Action: {request_info.get('action', 'N/A')}",
        f"  Prompt: {request_info.get('prompt', 'N/A')}",
        "",
    ]

    if response_info.get("success"):
        lines.append("Response: Success")
        lines.append("")

        for i, image in enumerate(response_info.get("data", []), 1):
            lines.extend(
                [
                    f"--- Image {i} ---",
                    f"Prompt: {image.get('prompt', 'N/A')}",
                    f"Image URL: {image.get('image_url', 'N/A')}",
                    "",
                ]
            )
    else:
        lines.append(f"Response: {response_info}")

    return "\n".join(lines)
