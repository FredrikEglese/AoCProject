from django.shortcuts import render
import os
import importlib.util

def id_to_name(id):
    return (
        "Day "      + id.split("_")[0] + 
        " - Part "  + id.split("_")[1] )

def index(request):
    context = {}
    solution_files_list = []

    for file_name in os.listdir("./AoC/solutions"):
        if file_name.endswith(".py"):
            solution_files_list.append(file_name[5:8])

    solution_files_list.sort()
    context["solution_files_list"] = solution_files_list

    return render(request, "AoC/index.html", context)

def solve(request, question_id):
    context = {}

    context["question_id"] = question_id
    context["question_title"] = id_to_name(question_id)

    try:
        spec = importlib.util.spec_from_file_location("task", "AoC/solutions/task_" + question_id + ".py")
        task = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(task)
        context["hello"] = task.hello_world
    except FileNotFoundError:
        context["result_value"] = "No algorithm foun"

    return render(request, "AoC/solve.html", context)

def result(request, question_id):
    result_value = 12
    context = {}  
    context["result_value"] = result_value
    context["question_title"] = id_to_name(question_id)

    return render(request, "AoC/result.html", context)