x = object()
y = object()

x_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_list = ["A", "B", "C", "D", "E", "F", "G", "J", "K", "L"]
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
