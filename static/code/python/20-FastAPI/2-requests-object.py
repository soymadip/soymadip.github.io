from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI Request Object Example", version="1.0.0")


@app.get("/info")
async def get_info(request: Request):

    # URL & Routing Info
    url = request.url  # e.g., http://127.0.0.1:8000/info?search=fastapi
    path = request.url.path  # e.g., "/info"
    query_params = (
        request.query_params  # Access query parameters (e.g., request.query_params.get("search"))
    )

    # Client & Connection Info
    client_ip = request.client.host  # Client's IP address
    method = request.method  # GET, POST, PUT, DELETE, etc.

    # Headers & Cookies
    user_agent = request.headers.get("user-agent")  # Browser or client info
    cookies = request.cookies  # Dictionary of incoming cookies

    # Request Body & State
    body = await request.body()  # Raw bytes of request body
    # json_data = await request.json()  # Parsed JSON payload
    # form_data = await request.form()  # Submitted HTML form data

    return {
        "url": url,
        "path": path,
        "query_params": query_params,
        "client_ip": client_ip,
        "method": method,
        "user_agent": user_agent,
        "cookies": cookies,
        "body": body,
    }


@app.get("/", response_class=HTMLResponse)
def home():
    return "<html><body>flsjfksljLj</body></html>"
