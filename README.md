# HW 2: Waypoint Following PID

In this HW, you need to implement PID controller to follow waypoints along a path.

## Code structure

```
.
+-- gem_waypoint_pid
|  +-- waypoints
|  |  +-- wps.csv              # waypoints list
|  |  +-- records_wps          # visualization of waypoints
|  +-- scripts
|  |  +-- gen_waypoint.py      # for generating waypints
|  |  +-- pid.py               # for implementing PID controller
|  |  +-- follow_waypoints.py  # main script to interact with the simulator
```

## To be implemented

All code snippets to be implemented by yourself has been marked with `# TODO: ...`

### 1. PID controller

Please implement PID controller in `gem_waypoint_pid/scripts/pid.py`.

### 2. Application of PID controller

Please complete the following parts in `gem_waypoint_pid/scripts/follow_waypoints.py`:

- transforming the goal point into the vehicle coordinate frame in function `start_drive`
- define your feedback value for PID control in function `start_drive`
- Set your own sets of weights for P, I, D terms in `__init__`.

## Note

The `/gem/ackermann_cmd` publishing topic is changed to `/ackermann_cmd`

## How to run

Assume your ROS workspace locates at `$WS_ROOT`. Please place folder `gem_waypoint_pid` under `$WS_ROOT/src/POLARIS_GEM_e2/polaris_gem_drivers_sim`.

- Start Simulator: `roslaunch gem_launch gem_init.launch world_name:="track1.world"`
- Move Vehicle: `rosrun gem_waypoint_pid follow_waypoints.py`. You should see vehicle move in the middle of the road in the simulator.
- Reset: `python3 set_pos.py`

## What to be submitted

Please submit the following:

1. Your completed `gem_waypoint_pid`
2. Two videos showing the running of your PID contollers with **two sets of P, I, D terms**.

## Demo Videos

- Perfectely tuned PID parameters: **Kp=0.5, Ki=0.01, Kd=0.05**
- [![Perfectely tuned PID parameters](https://img.youtube.com/vi/4thNQFfdHeM/0.jpg)](https://youtu.be/4thNQFfdHeM)
