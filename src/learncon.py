import sanic
from sanic.response import html, json, file

from util.database import Database
from typing import List
import os

bp_content = sanic.Blueprint("learncon_content", url_prefix="/learning_content")
bp_api = sanic.Blueprint("learncon_api", url_prefix="/learning_content")


@bp_content.get("/")
async def learncon_index(request: sanic.Request):
    return json({}, status=200)  # TODO: 프론트엔드 팀 결과물 반환


@bp_api.route("/post", methods=["POST"])
async def learncon_post(request: sanic.Request):
    async def __post():
        try:
            __content: List[str] = request.body.decode("utf-8").split("\n")
            content: List[str] = __content[:-4]
            parsed_texts: List[List[str]] = list(map(lambda p: p.split(":"), __content[:-5:-1]))

            # parse
            __files = None if parsed_texts[1][0] != "files" else int(parsed_texts[1][1].strip())
            __title = None if parsed_texts[0][0] != "title" else parsed_texts[0][1].strip()
            __author = None if parsed_texts[2][0] != "author" else parsed_texts[2][1].strip()
            __passcode = None if parsed_texts[3][0] != "passcode" else parsed_texts[3][1].strip()

            if (__title is None) or (__files is None) or \
                    (__author is None) or (__passcode is None):
                return json({}, status=400)

            db = Database()
            db.query("INSERT INTO LearnConTable(title, author, content, filecount, passcode) "
                     "VALUES (:title, :author, :content, :filecount, :passcode) ", {
                         "title": __title,
                         "files": __files,
                         "author": __author,
                         "passcode": __passcode,
                         "content": "\n".join(content),
                     })
            return json({}, status=201)
        except Exception as E:
            print(E)
            return json({}, status=500)

    match request.method:
        case "POST":
            return await __post()
        case _:
            return json({
                "Error": "Method Not Allowed"
            }, status=405)


@bp_api.route("/<article:slug>", methods=["GET", "DELETE", "PATCH"])
async def learncon_get(request: sanic.Request, article: str):
    async def __get():
        try:
            with open(f"data/learning_content/{article}.html", 'r') as f:
                return html(f.read())
        except FileNotFoundError:
            return json({
                "Error": "Article Not Found"
            }, status=404)

    async def __delete():
        if "SOFT-Passcode" not in request.headers.keys():
            return json({
                "Error": "Missing Passcode"
            }, status=400)
        try:
            db = Database()
            post_exists = db.query("DELETE FROM LearnConTable WHERE post_id=:post_id AND passcode=:passcode")[0] > 0

            if not post_exists:
                return json({
                    "Error": "Invalid Post ID"
                })

            return json(status=200)
        except Exception as E:
            return json({
                "Error": str(E)
            }, status=404)

    async def __patch():
        if "SOFT-Passcode" not in request.headers.keys():
            return json({
                "Error": "Missing Passcode"
            }, status=400)

        db = Database()
        db.query("")

    match request.method:
        case "GET":
            return await __get()
        case "DELETE":
            return await __delete()
        case "PATCH":
            return await __patch()
        case _:
            return json({
                "Error": "Method Not Allowed"
            }, status=405)


@bp_api.route("/static", methods=["GET", "POST", "DELETE", "PATCH"])
async def learncon_upload(request: sanic.Request):
    async def __get():
        pass

    async def __post():
        pass

    async def __delete():
        pass

    async def __patch():
        pass

    match request.method:
        case "GET":
            return await __get()
        case "POST":
            return await __post()
        case "DELETE":
            return await __delete()
        case "PATCH":
            return await __patch()
        case _:
            return json({
                "Error": "Method Not Allowed"
            }, status=405)
