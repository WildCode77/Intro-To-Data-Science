def counttime(pizza_slices, k):
    # Returns the time for k to finish his pizza_slices give in pizza_slices[k]
    time = 0
    for i in range(len(pizza_slices)):
        for j in range(len(pizza_slices)):
            if pizza_slices[k] == 0:
                return f" student {k} took {time} seconds to finish his portion of pizza"
            elif pizza_slices[i] == 0:
                continue
            else:
                pizza_slices[i] -= 1

pizza_queue = [0,0,0,0]
print(counttime(pizza_queue, 2))