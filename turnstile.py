# Test Case 1
# time      = [0, 1, 1, 3, 3]
# direction = [0, 1, 0, 0, 1]
# output    = [0, 2, 1, 4, 3]

# Test Case 2

# time 		= [0, 0, 1, 5] 
# direction = [0, 1, 1, 0] 
# output 	= [2,0,1,5]


# Test case 3

# time 		= [0, 0, 0, 0] 
# direction = [0, 1, 1, 0]
# output 	= [2, 0, 1, 3]
			  
def get_time(time, direction):
	result = []
	print time,"time......................."
	print direction,"direction......................"
	details = {}
	default_dir = 1

	selected_items = {}
	prv_time = None
	completed = True
	num_pos = len(direction)

	while completed:

		for p, v in enumerate(time):
			details[p] = {"time":v, "dir":direction[p]}
		
		for pos, val in enumerate(direction):
			if pos in selected_items:
				continue

			if prv_time and prv_time+1 < time[pos]:
				max_pos = pos
				new_dir_list = direction[:max_pos]
				for new_pos, new_val in enumerate(new_dir_list):
					if new_pos not in selected_items:
						if [selected_items[i] for i in selected_items if time[new_pos]]:
							cal_pos = [selected_items[i] for i in selected_items if time[new_pos]][-1] + 1							
							while cal_pos in [selected_items[i] for i in selected_items if time[new_pos]]:
								cal_pos += 1						    		
						else:
							cal_pos = new_pos
							while cal_pos in [selected_items[i] for i in selected_items]:
								cal_pos += 1
						selected_items[new_pos] = cal_pos
				default_dir = 1

			for key, value in details.iteritems():
				if pos != key:
					if value['time'] == time[pos] and value['dir'] == default_dir:
						selected_time = value['time']
						while selected_time in [selected_items[i] for i in selected_items]:
							selected_time += 1
						selected_items[key] = selected_time
			if selected_items:
				if default_dir == val:
					selected_items[pos] = time[pos]
			else:
				selected_items[pos] = time[pos]
				default_dir = val
			prv_time = time[pos]

		for pos, val in enumerate(direction):
			if pos not in selected_items:
				new_time = time[pos]
				while new_time in [selected_items[i] for i in selected_items]:
					new_time += 1
				selected_items[pos] = new_time

		if len(selected_items) == num_pos:
			completed = False

	print selected_items.values(),"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
	return selected_items.values()


if __name__=="__main__":
	# get_time([0, 1, 1, 3, 3], [0, 1, 0, 0, 1])
	# get_time([0, 0, 1, 5], [0, 1, 1, 0])
	get_time([0, 0, 0, 0], [0, 1, 1, 0])