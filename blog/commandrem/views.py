from django.shortcuts import render
from .models import CommandRem
from django.views.generic import ListView

class CmdRem(ListView):
    model = CommandRem
    template_name = "./commandrem/cmd.html"