import sanic
from sanic.response import html, json. file

bp_content = sanic.Blueprint("learncon_content", url_prefix="/learning_content")
bp_api = sanic.Blueprint("learncon_api", url_prefix="/learning_content")

@bp_api.route("/static", methods=["GET", "POST", "DELETE", "PATCH"])
async def learncon_upload(request: sanic.Request):
    async def __get():
        try:
        filename = request.headers.get("SOFT-Filename")
        
        if not filename:
            return json({"Error": "헤더에 누락된 속성이 있음"}, status=400)
        
        file_path = f"data/static/{filename}"
        
        if not os.path.isfile(file_path):
            return json({"Error": "게시글이 존재하지 않음"}, status=404)
        
        return await file(file_path)
    
    except Exception as e:
        return json({"Error": str(e)}, status=500)

    async def __post():
    try:
        if "SOFT-Filename" not in request.headers or "SOFT-Article" not in request.headers:
            return json({"Error": "헤더에 누락된 속성이 있음"}, status=400)
        
        filename = request.headers["SOFT-Filename"]
        article = request.headers["SOFT-Article"]
        
        uploaded_files = request.files.getlist('file')
        
        save_path = f"data/static/{filename}"
        for file in uploaded_files:
            file.save(save_path + file.name)
        
        db = Database()
        db.query("INSERT INTO StaticFiles (filename, article) VALUES (:filename, :article)", {
            "filename": filename,
            "article": article
        })
        
        return json({}, status=201)
    
    except Exception as e:
        return json({"Error": str(e)}, status=500)

    async def __delete():
         try:
        filename = request.headers.get("SOFT-Filename")
        
        if not filename:
            return json({"Error": "헤더에 누락된 속성이 있음"}, status=400)
        
        file_path = f"data/static/{filename}"
        
        if not os.path.isfile(file_path):
            return json({"Error": "파일을 찾지 못함"}, status=404)
        
        os.remove(file_path)
                
        return json({}, status=200)
    
    except Exception as e:
        return json({"Error": str(e)}, status=500)

    async def __patch():
        try:
        if "SOFT-Filename" not in request.headers or "SOFT-Article" not in request.headers:
            return json({"Error": "헤더에 누락된 속성이 있음"}, status=400)
        
        filename = request.headers["SOFT-Filename"]
        article = request.headers["SOFT-Article"]
        
        uploaded_files = request.files.getlist('file')
        
        save_path = f"data/static/{filename}"
        for file in uploaded_files:
            file.save(save_path + file.name)
                
        return json({}, status=200)
    
    except Exception as e:
        return json({"Error": str(e)}, status=500)

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
