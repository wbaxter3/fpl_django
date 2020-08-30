from fpl import FPL
from django.shortcuts import render
import requests
import asyncio
import aiohttp
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from asgiref.sync import async_to_sync
from prettytable import PrettyTable
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *



async def home(request):


    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players(return_json=True)

    players = sorted(players, key=lambdax: x.goals_scored + x.assists, reverse=True)
    # top_performers = sorted(
    #     players, key=lambda x: x.goals_scored + x.assists, reverse=True)
    #
    # player_table = PrettyTable()
    # player_table.field_names = ["Player", "£", "G", "A", "G + A"]
    # player_table.align["Player"] = "l"
    #
    #
    # for player in top_performers[:10]:
    #     goals = player.goals_scored
    #     assists = player.assists
    #     player_table.add_row([player.web_name, f"£{player.now_cost / 10}",goals, assists, goals + assists])
    #
    #
    # print(player_table)
    return render (request, 'home.html', {'players':players})






sync_home = async_to_sync(home)
