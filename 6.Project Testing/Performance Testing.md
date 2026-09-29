EDUGENIE — PERFORMANCE TESTING

Test scope
API validation, module behavior, request/response handling and integrated browser workflow.

Automated tests
Health endpoint behavior.
Q&A endpoint with mocked AI output.
Summary input validation.
Quiz response structure.
Module-level validation and JSON parsing.

Performance considerations
Gemini latency depends on network/provider response time. The local explanation model has initial load cost and can reuse the cached model in later requests within the environment.

Run
pytest -q