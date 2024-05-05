mode = {'display style' : [False],
        'product'       : [None ],
        'vector'        : [None ],
        'conjugate'     : ['*'],
        'dot product'   : [None ]}

last_selected_mode = None

def push(mode_name, value):
    mode[mode_name].append(value)
    global last_selected_mode
    last_selected_mode = mode_name

        
def pop(mode_name = None):
    global last_selected_mode
    if mode_name == None:
        name = last_selected_mode
    else:
        name = mode_name
    mode[name] = mode[name][:-1]

def get(mode_name):
    return mode[mode_name][-1]
    
