import sanic
from sanic.response import html, json, file
from util.database import Database  # Assuming Database is imported correctly

bp_content = sanic.Blueprint("learncon_content", url_prefix="/learning_content")
bp_api = sanic.Blueprint("learncon_api", url_prefix="/learning_content")

@bp_api.route("/static", methods=["GET", "POST", "DELETE", "PATCH"])
async def learncon_upload(request: sanic.Request):
    async def __get():
        try:
            post_id = request.args.get("post_id")
            
            db = Database()
            result = db.query("SELECT * FROM LearnConTable WHERE post_id=:post_id", {"post_id": post_id})
            
            if not result:
                return json({"Error": "Post not found"}, status=404)
            
            return json(result[0], status=200)
        
        except Exception as e:
            return json({"Error": str(e)}, status=500)

    async def __delete():
        try:
            if "SOFT-Passcode" not in request.headers:
                return json({"Error": "Missing required header"}, status=400)
            
            passcode = request.headers["SOFT-Passcode"]
            post_id = request.args.get("post_id")
                    
            if not passcode:
                return json({"Error": "Missing Passcode"}, status=400)
            
            if not post_id:
                return json({"Error": "Missing post_id parameter"}, status=400)

            db = Database()
            result = db.query("DELETE FROM LearnConTable WHERE post_id=:post_id AND passcode=:passcode", {
                "post_id": post_id,
                "passcode": passcode
            })
            
            if result > 0:
                return json({}, status=200)
            else:
                return json({"Error": "Post not found"}, status=404)
        
        except Exception as e:
            return json({"Error": str(e)}, status=500)

    async def __patch():
        try:
            if "SOFT-Passcode" not in request.headers:
                return json({"Error": "Missing Passcode"}, status=400)
            
            passcode = request.headers["SOFT-Passcode"]
            post_id = request.args.get("post_id")
            updated_content = request.body.decode("utf-8")
            
            if not passcode:
                return json({"Error": "Missing Passcode"}, status=400)
            
            db = Database()
            result = db.query("UPDATE LearnConTable SET content=:content WHERE post_id=:post_id AND passcode=:passcode", {
                "content": updated_content,
                "post_id": post_id,
                "passcode": passcode
            })
            
            if result > 0:
                return json({}, status=200)
            else:
                return json({"Error": "Post not found"}, status=404)
        
        except Exception as e:
            return json({"Error": str(e)}, status=500)

    if request.method == "GET":
        return await __get()
    elif request.method == "POST":
        returna await __post()
    elif request.method == "DELETE":
        return await __delete()
    elif request.method == "PATCH":
        return await __patch()
    else:
        return json({"Error": "Method Not Allowed"}, status=405)
        
