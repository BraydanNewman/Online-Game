from flask import Flask, render_template, sessions, redirect, url_for, request
import sqlite3

app = Flask(__name__)


class Player:

    jail = False

    def __init__(self, name, password, game_id):
        self.name = name
        self.password = password
        self.game_id = game_id

    def roll_dice(self):
        pass


class Game:

    def __init__(self, tiles, properties, chance_cards, community_chest_cards, game_id, g_name, g_password):
        self.tiles = tiles
        self.properties = properties
        self.chance_cards = chance_cards
        self.community_chest_cards = community_chest_cards
        self.game_id = game_id
        self.g_name = g_name
        self.g_password = g_password


def game_creator(g_name, g_password, p_name, p_password):
    pass


def game_check(g_name, g_password, p_name, p_password):
    pass


@app.route('/')
def root():
    return render_template("settings.html")


@app.route('/join', methods=["POST"])
def join():
    g_name = request.form["join_game_name"]
    g_password = request.form["join_game_password"]
    p_name = request.form["join_player_name"]
    p_password = request.form["join_player_password"]
    game_check(g_name, g_password, p_name, p_password)
    return redirect("/")


@app.route('/create', methods=["POST"])
def create():
    g_name = request.form["create_game_name"]
    g_password = request.form["create_game_password"]
    p_name = request.form["create_player_name"]
    p_password = request.form["create_player_password"]
    game_creator(g_name, g_password, p_name, p_password)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
