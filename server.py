from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

from database import engine, Base, SessionLocal
from models import Players
from schemas import PlayerName


app = FastAPI()


Base.metadata.create_all(bind=engine)



@app.get("/")
def logining():
   return FileResponse("login.html")


@app.get("/login.js")
def login_script():
   return FileResponse("login.js")



@app.get("/home")
def home():
   return FileResponse("main.html")



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, id: int):

   await websocket.accept()

   print("Player joined:", id)

   try:

      while True:
         message = await websocket.receive_text()

   except WebSocketDisconnect:
      db = SessionLocal()
      player = db.query(Players).filter(Players.id == id).first()

      if player:
         db.delete(player)
         db.commit()

      db.close()






@app.get("/scripts.js")
def script():
   return FileResponse("scripts.js")

@app.get("/styles.css")
def styles():
   return FileResponse("styles.css")






@app.post("/login")
def login(player_data: PlayerName):

   db = SessionLocal()

   player = Players(name=player_data.name)

   db.add(player)
   db.commit()
   db.refresh(player)

   player_id = player.id

   db.close()

   return {
      "success": True,
      "id": player_id
   }






