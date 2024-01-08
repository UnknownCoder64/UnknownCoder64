import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------
def saveimg():
    save=input("Save As: ")
    plt.savefig(save)
    plt.show()
#--------------------------------------------------------------------------------------
graph_type=input("Enter The Type Of Graph\n[Bar, Line, Pie]\n:")
graph_type=graph_type.lower()

if graph_type=='bar':
    
    x_axis=[]
    range_x=int(input("Enter The X-axis Range: "))
    for i in range(0,range_x):
        x_input=input("Enter The x-axis: ")
        x_axis.append(x_input)
    
    y_axis=[]
    for j in x_axis:
        y_input=int(input(f"Enter The Y-Axis for {j}: "))
        y_axis.append(y_input)

    print("X-axis:", x_axis)
    print("Y-axis:", y_axis)

    label_x =input("Enter The X-label: ")
    label_y =input("Enter The Y-label: ")

    plt.bar(x_axis, y_axis)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    saveimg()

if graph_type=='line':

    x_axis=[]
    range_x=int(input("Enter The X-axis Range: "))
    for i in range(0,range_x):
        x_input=input("Enter The x-axis: ")
        x_axis.append(x_input)
    
    y_axis=[]
    for j in x_axis:
        y_input=int(input(f"Enter The Y-Axis for {j}: "))
        y_axis.append(y_input)

    print("X-axis:", x_axis)
    print("Y-axis:", y_axis)

    label_x =input("Enter The X-label: ")
    label_y =input("Enter The Y-label: ")

    plt.plot(x_axis, y_axis)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    saveimg()

if graph_type=='pie':

    x_axis=[]
    range_x=int(input("Enter The X-axis Range: "))
    for i in range(0,range_x):
        x_input=input("Enter The x-axis: ")
        x_axis.append(x_input)
    
    y_axis=[]
    for j in x_axis:
        y_input=int(input(f"Enter The Y-Axis for {j}: "))
        y_axis.append(y_input)

    print("X-axis:", x_axis)
    print("Y-axis:", y_axis)

    plt.pie(y_axis, labels = x_axis, shadow= True, radius= 1.2, autopct= '%1.1f%%', )
    saveimg()

else:
    print("ERROR!")

# :D