from django.shortcuts import render
import os
import importlib.util


""" Returns str of long solution title

Takes the id in the form x_y and returns in the form Day x - Part y
This is makes the id easier to interpret by the user
"""
def id_to_name(id):
    return (
        "Day "      + id.split("_")[0] + 
        " - Part "  + id.split("_")[1] )


# ~~~ RENDER METHODS ~~~

def index(request):
    solution_files_list = []

    for file_name in os.listdir("./AoC/solutions"):
        if file_name.endswith(".py"):
            # extract just the x_y part of task_x_y.py
            solution_files_list.append(file_name[5:8])

    solution_files_list.sort()

    context = {
        "solution_files_list" : solution_files_list,
    }

    return render(request, "AoC/index.html", context)

def solve(request, question_id):
    context = {
        "question_id": question_id,
        "question_title" : id_to_name(question_id),
    }

    return render(request, "AoC/solve.html", context)

def result(request, question_id):
    context = {
        "question_title" : id_to_name(question_id),
    }  
    
    input_string = request.POST.get('input_textbox')

    # Dynamically fetch the correct task and import it as task then execute solve
    try:
        spec = importlib.util.spec_from_file_location("task", "AoC/solutions/task_" + question_id + ".py")
        task = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(task)
        context["result_value"] =  task.solve(input_string) 
    except Exception as e :
        context["result_value"] = "There was an issue. " + str(e)

    return render(request, "AoC/result.html", context)