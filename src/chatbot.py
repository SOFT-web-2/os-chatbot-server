import sanic
from sanic.response import html

bp_content = sanic.Blueprint("chatbot_content", url_prefix="/chatbot")
bp_api = sanic.Blueprint("chatbot_api", url_prefix="/chatbot")


@bp_content.route("/")
async def chatbot_index(request: sanic.Request):
    return html(status=200)  # TODO: 프론트엔드 팀 결과물 반환


# TODO: 웹소켓 사용한 챗봇 구현 필요
