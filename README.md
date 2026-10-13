# Line Follower Robot — Webots

A Webots project for developing a Python-controlled differential-drive robot that follows a marked path using ground sensor readings.

## Project status

Initial setup. The simulation world is being created; the robot, ground sensors and line-following controller will be added incrementally. Working line-following behavior has not yet been demonstrated in this repository.

## Planned behavior

- Read downward-facing ground sensors to distinguish the line from the surrounding floor.
- Adjust left and right wheel speeds to steer along the path.
- Test straight sections and curves, and observe behavior when the line is lost.

## Requirements

- Webots (development environment: R2025a).
- Python 3 configured in Webots preferences.

Webots provides the `controller` Python module when it launches a controller. Install additional packages only if the future controller requires them.

## Project layout

| Location | Purpose |
| --- | --- |
| `worlds/line_follower.wbt` | Planned simulation world, track and robot placement |
| `controllers/` | Python robot controllers as they are added |
| `protos/` | Optional reusable custom robot models |
| `libraries/` | Optional shared project code |
| `plugins/` | Optional Webots plugins |
| `docs/` | Screenshots, GIF demonstrations and notes as they are added |

Some directories may be empty or absent during initial development. `.gitkeep` files can preserve empty directories in Git.

## Run the simulation

Once the world and controller are added:

1. Open `worlds/line_follower.wbt` in Webots.
2. Set the robot's `controller` field to the implemented controller directory name.
3. Confirm that the device names in the Python code match the robot's motor and sensor names.
4. Start the simulation. Save code changes and reset the simulation to restart the controller.

## Development milestones

- [ ] Create the simulation world and marked track.
- [ ] Add the robot, wheel motors and ground sensors.
- [ ] Read and inspect sensor values on the line and floor.
- [ ] Implement and test line-following control.
- [ ] Handle line loss.
- [ ] Add a GIF of the demonstrated behavior.

## Demonstration

A simulation recording will be added after line following is working.

## Learning reference

This project is being developed alongside this [Webots tutorial](https://www.youtube.com/watch?v=D0jhvFZJ5Ok). Refer to the original tutorial for its instructions and attribution.
