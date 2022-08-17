import pickle
def run_model(mylist):
    X_new=[mylist]
    with open('Flask2/logistic_model.pkl', 'rb') as file:
        model= pickle.load(file)
    predictions=model.predict(X_new)

    if predictions==0:
        name='setosa'
    elif predictions==1:
        name='versicolor'
    elif predictions==2:
        name='virginica'
    else:
        name=''
    return name

