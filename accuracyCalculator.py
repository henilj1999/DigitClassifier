import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

dataset = pd.read_csv('C:/Users/Henil Jain\Desktop/Number Identifier/data.csv')

print(len(dataset))

l = []
for i in range(0, 15625):
    l.append(str(i))

X = dataset[l].values
Y = dataset['output'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.025)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
clf = clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test)

for i in range(0, len(Y_pred)):
    print(str(Y_test[i]) + "  " + str(Y_pred[i]))

print("Accuracy:", metrics.accuracy_score(Y_test, Y_pred))
