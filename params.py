
dt = 0.1 #sec
#ITI_fixed_sec = 2
ITI_min_sec = 5  #sec
ITI_max_sec = 10 #sec
holding_min_sec = 0.5
holding_max_sec = 1.5
go_cue_duration_sec=0.2
rew_cue_duration_sec = 0.1
click_strength   = 1.0

#ITI_fixed        = round(ITI_fixed_sec/dt)
ITI_min          = round(ITI_min_sec/dt)
ITI_max          = round(ITI_max_sec/dt)
ITI_fixed        = ITI_min
holding_min      = round(holding_min_sec/dt)
holding_max      = round(holding_max_sec/dt)
go_cue_duration  = round(go_cue_duration_sec/dt)
rew_cue_duration = round(rew_cue_duration_sec/dt)

action_cost    = -0.001 # now engage means performing the task. i.e., all action other than non-engage incur such cost.
latency_engage = 8 # from non-engage to engage
latency_non_engage = 8 # from engage to non-engage
latency_CNI  = 4  # from engage to center-port-in

action_names = ('port_0','port_1','port_2','food_port',\
	            'non_engage','engage','transition')
port_names   = ('port_0','port_1','port_2') # actions for poking one of the three ports
