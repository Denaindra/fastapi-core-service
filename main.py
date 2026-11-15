from fastapi import FastAPI
from fastapi.responses import HTMLResponse




app = FastAPI()
posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

# html response services

@app.get("/posts",response_class=HTMLResponse, include_in_schema=False)
def get_results():
    return f"<H1>{posts[0]["title"]}</H1>"


#end html response services



@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/api/posts")
def get_post():
    return posts