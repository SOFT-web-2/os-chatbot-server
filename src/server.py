import sanic
from sanic.response import text

import chatbot
import learncon
import portfolio

app = sanic.Sanic("soft")

sanic.Blueprint.group(
    chatbot.bp_api,
    learncon.bp_api,
    url_prefix="/api")
sanic.Blueprint.group(
    chatbot.bp_content,
    learncon.bp_content)
