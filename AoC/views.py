from django.shortcuts import render
import os

def index(request):
    context = {}
    solution_files_list = []
    for file_name in os.listdir("./AoC/solutions"):
        if file_name.endswith(".py"):
            solution_files_list.append(file_name[:3])
    context["solution_files_list"] = solution_files_list

    return render(request, "AoC/index.html", context)

def solve(request, question_id):
    context = {}
    context["question_id"] = question_id

    return render(request, "AoC/solve.html", context)