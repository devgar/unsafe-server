__version__ = "0.1.0"

import uvicorn

app = "unsafe_server.main:app"


def dev():
    print("Running dev server")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True, workers=2)
