#autor: Jakub Vano (xvanoj00)

from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS

app = Flask(__name__)
cors = CORS(app)


games = {}
enemy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
id = 0
hitpoints = 0

def create_new_game():
    global id
    games[id] = {"active": False, "pole": [0]
                 * 100, "size": 100, "count": 10}
    id += 1
    return id - 1


@cross_origin()
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@cross_origin()
@app.route("/quickgame", methods=["GET"])
def serach_game():
    global games
    cnt = 0
    for id in games:
        if(games[id]["active"] == False):
            cnt += 1

    id = 0
    if(cnt == 0):
        id = create_new_game()
        while(not games[id]["active"]):
            pass
    else:
        for i in games:
            if(games[i]["active"] == False):
                games[i]["active"] = True
                id = i

    print(games[id])
    return str(id)


@cross_origin()
@app.route("/linkgame", methods=["POST"])
def link_game():
    print(request.is_json)
    content = request.get_json()
    gameid = content["gameid"]
    size = content["size"]
    count = content["count"]

    games[gameid] = {"active": False, "pole": [0]
                     * size * size, "size": size, "count": count}

    while(not games[gameid]["active"]):
        pass

    return str(gameid)


@cross_origin()
@app.route("/linkconnect/<gameid>", methods=["GET"])
def connect_link(gameid):

    games[gameid]["active"] = True

    print(games[gameid])
    return str(gameid)

@app.route("/Play", methods=["POST"])
def Play():
    global enemy
    global hitpoints
    content = request.get_json()
    enemy = content["enemy"]
    hitpoints = content["hitpoints"]
    return "<p>Hello, World!</p>"
    
@app.route("/Logic", methods=["POST"])
def Logic():
    global hitpoints
    content = request.get_json()
    index = content["index"]
    hitmiss = enemy[index]
    print(index)
    if hitmiss == 1:
        print("hit")
        print(hitpoints)
        hitpoints -= 1
        print(hitpoints)
        if hitpoints == 0:
            return str(2)
        return str(1)
    else:
        print("miss")
        return str(0)


if __name__ == '__main__':
    app.run(debug=True)


