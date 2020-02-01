from django.shortcuts import render
import os

def index(request):
    context = {}
    solution_files_list = []

    for file_name in os.listdir("./AoC/solutions"):
        if file_name.endswith(".py"):
            solution_files_list.append(file_name[:3])

    solution_files_list.sort()
    context["solution_files_list"] = solution_files_list

    return render(request, "AoC/index.html", context)

def solve(request, question_id):
    context = {}
    split_question_id = question_id.split("_")

    context["question_title"] = "Day " + split_question_id[0] + " - Part " + split_question_id[1]
    context["question_id"] = question_id

    return render(request, "AoC/solve.html", context)

def result(request, question_id, user_input):
    context = {}  
      
    result_value = 12
    context["result_value"] = result_value

    return render(request, "AoC/result.html", context)