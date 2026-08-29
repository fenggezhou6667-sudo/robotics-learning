# Nav2 troubleshooting

## Missing map frame

Symptom:

```text
Invalid frame ID "map"
```

Checks:

1. Confirm the map server lifecycle node is active.
2. Verify that the `/map` topic is publishing.
3. Inspect the TF tree and confirm that the configured fixed frame is `map`.

## AMCL does not publish a pose

1. Set an initial pose in RViz.
2. Verify the `map -> odom -> base_link` transform chain.
3. Confirm that laser scan data and the configured scan topic are available.
4. Ensure `use_sim_time` is consistent across simulation and Nav2 nodes.

## RViz plugin or display errors

ROS 2 and Nav2 distributions may ship different display plugins and panel
settings. Start with `assets/rviz/turtlebot3-navigation.rviz`; use
`assets/rviz/custom-navigation.rviz` when reproducing the custom experiment.
If a plugin cannot be loaded, remove only that display and add the matching
display supplied by the installed Nav2 version.
