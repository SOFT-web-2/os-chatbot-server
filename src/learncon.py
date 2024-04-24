import sanic
from sanic.response import html, json, file

bp_content = sanic.Blueprint("learncon_content", url_prefix="/learning_content")
bp_api = sanic.Blueprint("learncon_api", url_prefix="/learning_content")


@bp_content.get("/")
async def learncon_index(request: sanic.Request):
    return html(status=200)  # TODO: 프론트엔드 팀 결과물 반환


@bp_api.route("/post", methods=["POST"])
async def learncon_post(request: sanic.Request):
    async def __post():
        pass

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
        pass

    async def __delete():
        pass

    async def __patch():
        pass

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
