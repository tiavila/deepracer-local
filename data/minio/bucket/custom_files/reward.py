
import math

def reward_function(params):
    
    all_wheels_on_track = params['all_wheels_on_track']
    dist_center = params['distance_from_center']
    track_width = params['track_width']
    steering_reward = float(score_steer_to_point_ahead(params))
    

    reward = 1.0
    
    return steering_reward
