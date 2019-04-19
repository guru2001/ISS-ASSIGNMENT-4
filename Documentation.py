def index(argument1):
    """Summary or Description of the Function
    Parameters:
    An Introduction.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(index.__doc__)
def theory(argument1):
    """Summary or Description of the Function
    Parameters:
    An Theory.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(theory.__doc__)
def objective(argument1):
    """Summary or Description of the Function
    Parameters:
    An Objective.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(objective.__doc__)
def experiment(argument1):
    """Summary or Description of the Function
    Parameters:
    An Experiment.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(experiment.__doc__)
def quizzes(argument1):
    """Summary or Description of the Function
    Parameters:
    An Quizzes.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(quizzes.__doc__)
def procedure(argument1):
    """Summary or Description of the Function
    Parameters:
    An Procedure.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(procedure.__doc__)
def feedback(argument1):
    """Summary or Description of the Function
    Parameters:
    An Feedback.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(feedback.__doc__)
def further(argument1):
    """Summary or Description of the Function
    Parameters:
    An Further_Readings.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(further.__doc__)
def introduction1(argument1):
    """Summary or Description of the Function
    Parameters:
    An INtroduction1.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(introduction1.__doc__)
def reference(argument1):
    """Summary or Description of the Function
    Parameters:
    An Refernces.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(reference.__doc__)
def List_Of_Experiments(argument1):
    """Summary or Description of the Function
    Parameters:
    An List_Of_Experiments.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(List_Of_Experiments.__doc__)
def Target_audience(argument1):
    """Summary or Description of the Function
    Parameters:
    An Target Audience.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(Target_audience.__doc__)
def faq(argument1):
    """Summary or Description of the Function
    Parameters:
    An faq.html page
    Returns:
    Renders template of the page 
   """
    return render_template(argument1)
print(faq.__doc__)
def quiz(argument1):
    """Summary or Description of the Function
    Parameters:
    An quiz post request
    Takes the parameters sent by AJAX request through request.form
    If atleast one input is valid store in the sql database created in the file
    The returned whether is a valid input or not
    """
    return jsonify({'sucess' : 'Response has been recorded'})
print(quiz.__doc__)
def process(argument1):
    """Summary or Description of the function
    Parameters:
    A process post request 
    Takes the parameters sent by AJAX request through request.form
    If something is missing return to give an alert to fill.
    Then implemented logic by comparing inputs and the answer matrix 
    and storing the indices where there is a mismatch and returning a jsonify array
    for further implementations in javascript.
    """
    return jsonify(check)

